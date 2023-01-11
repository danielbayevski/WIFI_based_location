import time

from Location.RoutersMap import routerMap
from Location.models.dataModels import WifiData
from Location.wifiSignal import getWifiSignalList
import subprocess


routersData = dict()
while True:
    results = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=Bssid"]).decode("utf-8")
    routers: WifiData = getWifiSignalList(results)

    for router in getWifiSignalList(results):
        data: WifiData = routersData.get(router.bssid)
        if routersData.get(router.bssid):
            print(router.__dict__)
            data.signal = router.signal
        else:
            router.originPoint = routerMap.get(router.bssid)
            if router.originPoint is None:
                routersData[router.bssid] = router



    for route in routers:
        print(route.__dict__)
    print('----')
    time.sleep(1.5)

