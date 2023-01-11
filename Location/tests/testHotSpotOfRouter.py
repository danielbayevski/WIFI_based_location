import matplotlib.pyplot as plt

from Location.models.dataModels import WifiData
import Location.tests.branchData.yohananofData as yohananofData# import location00, location0003, location0100
from Location.findRouterPoint import findLocationPoints
from Location.models.LocationPoint import LocationPoint
from Location.models.Point import Point
from Location.placmentChecker import LocationUtil

tLocation: list[WifiData] = yohananofData.location00
#loactions.sort(key=sortWifi , reverse=True)
tLocation0003: list[dict] = yohananofData.location0003
tLocation0100 = yohananofData.location0100

tList = [tLocation, tLocation0003, tLocation0100]
listOriginPoints = [Point(0, 0), Point(0, -3), Point(1, 0)]


routersPoints: list[list[LocationPoint]] = []

# for loc in tLocation:
#     bssid = loc['bssid']
#     router: list[LocationPoint] = []
#     point = LocationPoint(listOriginPoints[0],
#                           getDistanceFromSignal(loc))
#     router.append(point)
#     for i in range(len(tList)):
#         for values in tList[i]:
#             if values.get('bssid') == bssid:
#                 point = LocationPoint(listOriginPoints[i + 1],
#                                       getDistanceFromSignal(values))
#                 router.append(point)
#     routersPoints.append(router)
routersPoints = findLocationPoints(tList,listOriginPoints)

for routersPoint in routersPoints[2:3]:
    for points in routersPoint:
        print(points.__dict__.get('OriginPoint').__dict__)
        print(points.__dict__.get('distance'))
    print('\n')
util = LocationUtil()
util.setPointDataMap(routersPoints[0])
j = util.findLoactionPoints()
for point in j:
    print(point.__dict__)

fig, ax = plt.subplots()
ax.set_xlim((-300, 300))
ax.set_ylim((-300, 300))
ax.set_ylabel('Y  axis')
ax.set_xlabel('X axis')

ax.set_title('possible points of a router')

for point in j:
    plt.plot(point.x,point.y , '.', color='r')


#plt.gca().set_aspect('equal', adjustable='box')


plt.show()

plt.close()




