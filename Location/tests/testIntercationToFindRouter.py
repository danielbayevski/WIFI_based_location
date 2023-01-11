import matplotlib.pyplot as plt
import MatplotHelper as matplotHelper
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

tList = [tLocation, tLocation0003 , tloaction1702, tloaction0126, tloaction0901, tloaction0115]
listOriginPoints = [Point(0, 0), Point(0, -3), Point(x=17, y=2), Point(1, 26), Point(9, 1), Point(1,15)]


routersPoints: list[list[LocationPoint]] = []

routersPoints = findLocationPoints(tList, listOriginPoints)

chosenRouter = [routersPoints[0]]
for routersPoint in chosenRouter:
    for points in routersPoint:
        print(points.__dict__.get('OriginPoint').__dict__)
        print(points.__dict__.get('distance'))
    print('\n')
util = LocationUtil()
util.setPointDataMap(chosenRouter[0])
allCircleCrossingPoints = util.findLoactionPoints()
pointsInCircles = util.getRouterRangePoints(allCircleCrossingPoints)
print(len(pointsInCircles), len(allCircleCrossingPoints))
# print(util.eliminatePointsThanChoosePoint(allCircleCrossingPoints))
#point = util.findMostAccurtePoint(allCircleCrossingPoints)
#print(pointsInCircles)
#true = isPointInsideCircle(LocationPoint(Point(0,0), 5), Point(3,3))
# fig, ax = plt.subplots()
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

font = {'family':'serif','color':'darkred','size':15}

ax[0].set_title('all route points', fontdict=font)
ax[1].set_title('after remove points route point', fontdict=font)



def paint(figure, chosenRouter, pointsInCircles, showPoints = True):

    font = {'family': 'serif', 'color': 'darkred', 'size': 15}
    figure.set_xlim((-150, 150))
    figure.set_ylim((-150, 150))
    figure.set_ylabel('Y  axis', fontdict=font)
    figure.set_xlabel('X axis' , fontdict=font)


    colors = plt.get_cmap("Accent").colors
    for routersPoint in chosenRouter:
        for color, point in zip(colors, routersPoint):
            circle = plt.Circle((point.OriginPoint.x, point.OriginPoint.y), point.distance,
                                color=color, fill=False)
            figure.add_artist(circle)
            matplotHelper.plotPoint(figure, point.OriginPoint, color)
            #figure.plot(point.OriginPoint.x, point.OriginPoint.y, '.', color=color)
            # label = f"(circle {int(point.OriginPoint.x)},{int(point.OriginPoint.y)})"
            # figure.annotate(label,  # this is the text
            #                 (point.OriginPoint.x, point.OriginPoint.y),  # these are the coordinates to position the label
            #                 textcoords="offset points",  # how to position the text
            #                 xytext=(0, 5),  # distance from text to points (x,y)
            #                 fontsize=5,
            #                 bbox=dict(boxstyle='round,pad=0.2', fc=color, alpha=0.3),
            #                 ha='center')
            # plt.plot(point.OriginPoint.x, point.OriginPoint.y, '.', color=color)
    # plt.gca().set_aspect('equal', adjustable='box')

    for point in pointsInCircles:
        if showPoints:
            # matplotHelper.plotPoint(figure, point)
            label = f"({int(point.x)},{int(point.y)})"
            figure.annotate(label,  # this is the text
                       (point.x, point.y),  # these are the coordinates to position the label
                       textcoords="offset points",  # how to position the text
                       xytext=(0, 5),  # distance from text to points (x,y)
                       fontsize=5,
                       ha='center')

        figure.plot(point.x, point.y, '.', color='r')

paint(ax[0], chosenRouter, allCircleCrossingPoints, False)
paint(ax[1], chosenRouter, pointsInCircles)
#
# ax[0].set_xlim((-150, 150))
# ax[0].set_ylim((-150, 150))
# ax[0].set_ylabel('Y  axis')
# ax[0].set_xlabel('X axis')
#
# ax[0].set_title('route point')
#
# # for point in allCircleCrossingPoints:
# #     plt.plot(point.x,point.y , '.', color='r')
#
# colors = plt.get_cmap("Accent").colors
# for routersPoint in chosenRouter:
#     for color, point in zip(colors, routersPoint):
#         circle = plt.Circle((point.OriginPoint.x, point.OriginPoint.y), point.distance,
#                             color=color, fill=False)
#         ax[0].add_artist(circle)
#         ax[0].plot(point.OriginPoint.x, point.OriginPoint.y, '.', color=color)
#         #plt.plot(point.OriginPoint.x, point.OriginPoint.y, '.', color=color)
# #plt.gca().set_aspect('equal', adjustable='box')
#
# for point in pointsInCircles:
#     label = f"({int(point.x)},{int(point.y)})"
#
#     ax[0].annotate(label,  # this is the text
#                  (point.x, point.y),  # these are the coordinates to position the label
#                  textcoords="offset points",  # how to position the text
#                  xytext=(0, 5),  # distance from text to points (x,y)
#                  fontsize= 5,
#                  ha='center')
#     ax[0].plot(point.x, point.y, '.', color='r')


plt.show()

plt.close()

