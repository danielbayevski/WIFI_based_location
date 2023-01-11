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
tloaction1702 = yohananofData.loaction1702
tloaction0126 = yohananofData.loaction0126
tloaction0901 = yohananofData.loaction0901
tloaction0115 = yohananofData.loaction0115

tList = [tLocation, tLocation0003 , tloaction1702, tloaction0126, tloaction0901]
listOriginPoints = [Point(0, 0), Point(0, -3), Point(x=17, y=2), Point(1, 26), Point(9, 1), Point(1,15)]


routersPoints: list[list[LocationPoint]] = []

routersPoints = findLocationPoints(tList, listOriginPoints)

chosenRouter = [routersPoints[1]]
for routersPoint in chosenRouter:
    for points in routersPoint:
        print(points.__dict__.get('OriginPoint').__dict__)
        print(points.__dict__.get('distance'))
    print('\n')
util = LocationUtil()
util.setPointDataMap(chosenRouter[0])
j = util.findLoactionPoints()

fig, ax = plt.subplots()
ax.set_xlim((-150, 150))
ax.set_ylim((-150, 150))
ax.set_ylabel('Y  axis')
ax.set_xlabel('X axis')

ax.set_title('possible points of a router')

# for point in j:
#     plt.plot(point.x,point.y , '.', color='r')

colors = plt.get_cmap("Accent").colors
for routersPoint in chosenRouter:
    for color, point in zip(colors, routersPoint):
        circle = plt.Circle((point.OriginPoint.x, point.OriginPoint.y), point.distance,
                            color=color, fill=False)
        ax.add_artist(circle)
        plt.plot(point.OriginPoint.x, point.OriginPoint.y, '.', color=color)
#plt.gca().set_aspect('equal', adjustable='box')

for point in j:
    label = f"({int(point.x)},{int(point.y)})"

    plt.annotate(label,  # this is the text
                 (point.x, point.y),  # these are the coordinates to position the label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 5),  # distance from text to points (x,y)
                 fontsize= 5,
                 ha='center')
    plt.plot(point.x, point.y, '.', color='r')


plt.show()

plt.close()
