import subprocess
import math
import time

from Location.models.dataModels import WifiData,Point
from Location.models.Router import routers
from Location.wifiSignal import getWifiSignalList
import sys

def isWindows():
    return sys.platform == 'win32' or sys.platform == 'win64'



def getRouters(removeUnkownRouters = False) -> WifiData:
    if isWindows():
        results = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=Bssid"])
        results = results.decode("utf-8")
        routers: list[WifiData] = getWifiSignalList(results)
        if len(routers) < 2:
            results = subprocess.Popen("wifi scan", stdout = subprocess.PIPE,
                                       shell = True).communicate()
            results = results[0].decode("utf-8")
            routers: list[WifiData] = getWifiSignalList(results)

    if removeUnkownRouters:
        routers = filterUnkownRouters(routers)
    routers = filterWeakRouters(routers)
    routers = insertOriginPointToRouters(routers)
    return routers

def filterWeakRouters(routers):
    filterdRouters=[]
    for router in routers:
        if router.signal>60:
            filterdRouters.append(router)
    return filterdRouters




def insertOriginPointToRouters(routers : list[WifiData]) -> list[WifiData]:
    for router in routers:
        router.originPoint = getRoutersOriginPoint(router)
        router.distance = signalToDistance(router)
        # print(router.__dict__)
    return routers

def getRoutersOriginPoint(router: WifiData):
    routersData = routers
    return routersData.get(router.bssid) if router.bssid in routersData else None

def filterUnkownRouters(routers: WifiData):
    filterdRouters =[]
    for router in routers:
        if getRoutersOriginPoint(router):
            filterdRouters.append(router)
    return filterdRouters

def _getLamda(network):
    if network=='802.11ac' or network=='802.11a':
        return 74.48
    return 67.64

def _getPidBm():
    return 27.55

def signalToDistance(router: WifiData):
    # Pr = 14*router.signal/100
    Pr = (router.signal / 2) - 100
    # 802.11a/n is 14dbm
    Pi = _getPidBm()
    Lamda = _getLamda(router.networkType) #
    # 2
    n = 2
    # https://www.researchgate.net/publication
    # /239919656_Indoor_Location_Using_Trilateration_Characteristics
    distance = 1 / math.pow(10, (Pr - Pi + Lamda) / (10 * n))
    # return math.sqrt(math.pow(distance,2)-9)
    return distance
    # return 100 - router.signal
