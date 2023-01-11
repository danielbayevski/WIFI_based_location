from Location.models.dataModels import WifiData
import Location.tests.branchData.yohananofData as yohananofData
from Location.findRouterPoint import findLocationPoints
from Location.models.LocationPoint import LocationPoint
from Location.models.Point import Point
from Location.placmentChecker import LocationUtil

tLocation: list[WifiData] = yohananofData.location00
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

util = LocationUtil()
util.setPointDataMap(chosenRouter[0])
allCircleCrossingPoints = util.findLoactionPoints()
pointsInCircles = util.getRouterRangePoints(allCircleCrossingPoints)
print(pointsInCircles)
print(util.buildPointsDistanceToCircle(pointsInCircles))
print(util.calcBestPossiblePointFromPoints(util.buildPointsDistanceToCircle(pointsInCircles)))