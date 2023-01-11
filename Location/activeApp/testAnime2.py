from Location.activeApp.Animation2 import MatplotlibAnimation
from Location.models.dataModels import WifiData
import Location.tests.branchData.yohananofData as yohananofData# import location00, location0003, location0100
from Location.findRouterPoint import findLocationPoints
from Location.models.LocationPoint import LocationPoint
from Location.models.Point import Point

tLocation: list[WifiData] = yohananofData.location00
#loactions.sort(key=sortWifi , reverse=True)
tLocation0003: list[dict] = yohananofData.location0003
tLocation0100 = yohananofData.location0100
tloaction1702 = yohananofData.loaction1702
tloaction0126 = yohananofData.loaction0126
tloaction0901 = yohananofData.loaction0901
tloaction0115 = yohananofData.loaction0115

tList = [tLocation, tLocation0003 , tloaction1702, tloaction0126, tloaction0901, tloaction0115]
listOriginPoints = [Point(0, 0), Point(0, -3), Point(x=17, y=2), Point(1, 26), Point(9, 1), Point(1,15)]


routersPoints: list[list[LocationPoint]] = []

routersPoints = findLocationPoints(tList, listOriginPoints)

chosenRouter = [routersPoints[0]]



draw = MatplotlibAnimation()

draw.draw(routers=chosenRouter[0])

draw.show()