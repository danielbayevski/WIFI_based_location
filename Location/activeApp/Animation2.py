import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton

from Location.models.dataModels import WifiData
from Location.models.LocationPoint import LocationPoint
from Location.models.Point import Point
import matplotlib.animation as animation
from Location.activeApp.RssiRouters import getRouters
from Location.models.mapPoints import special_point, special_points
from Location.models.Router import routers
import numpy as np

showedOnced: bool = True


def onclick(event):
    if event.dblclick:
        routers_ = None
        while not routers_:
            routers_ = getRouters(True)
        if event.button == MouseButton.RIGHT:
            dist =100
            rout = []
            for router in routers_:
                if router.distance<dist:
                    dist = router.distance
                    rout = router
            routers.update({rout.bssid: Point(event.xdata,event.ydata)})
        else:
            special_points.append(
                special_point({router.bssid: router.signal for router in routers_}, Point(event.xdata,event.ydata)))
        print("buttons pressed at: " + str(event.xdata)+','+str(event.ydata))



class MatplotlibAnimation:
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))

    routers: WifiData
    noticePoints: list[Point]
    mainPoint: Point
    size: int = (66,44)

    def __init__(self, graphConfig = {}, ):
        global fig, ax
        if len(graphConfig) != 0:
            MatplotlibAnimation.fig, MatplotlibAnimation.ax = plt.subplots(nrows=graphConfig['rows'],
                                                                           ncols=graphConfig['cols'],
                                   figsize=(graphConfig['xSize'], graphConfig['ySize']))


        font = {'family': 'serif', 'color': 'darkred', 'size': 15}
        MatplotlibAnimation.ax.set_xlabel('X axis', fontdict=font)
        MatplotlibAnimation.ax.set_ylabel('Y  axis', fontdict=font)
        self.size = 66
        cid = self.fig.canvas.mpl_connect('button_press_event', onclick)

    def draw(self,routers: WifiData = None,
             noticePoints : list[Point] = None , mainPoint: Point = None):
        MatplotlibAnimation.noticePoints = noticePoints
        MatplotlibAnimation.mainPoint = mainPoint
        MatplotlibAnimation.routers = routers

    @staticmethod
    def drawCircle(router:LocationPoint):
        circle = plt.Circle((router.OriginPoint.x, router.OriginPoint.y), router.distance,
                            color='r', fill=False)
        MatplotlibAnimation.ax.add_artist(circle)
        MatplotlibAnimation.drawPoint(point = router.OriginPoint, radius=router.distance)

    @staticmethod
    def drawAllRouters():
        for router in MatplotlibAnimation.routers:
            MatplotlibAnimation.drawCircle(router)

    @staticmethod
    def drawAllRouters():
        for router in MatplotlibAnimation.routers:
            if router.OriginPoint:
                MatplotlibAnimation.drawCircle(router=router)



    @staticmethod
    def drawPoint(point: Point, color='r' ,annotane = True , radius = 0):
        if annotane:
            label = f"({int(point.x)},{int(point.y)}, r={int(radius)})"
            MatplotlibAnimation.ax.annotate(label,  # this is the text
                            (point.x, point.y),  # these are the coordinates to position the label
                            textcoords="offset points",  # how to position the text
                            xytext=(0, 5),  # distance from text to points (x,y)
                            fontsize=5,
                            ha='center')
        MatplotlibAnimation.ax.imshow(plt.imread("C:/Users/Hp/PycharmProjects/WIFI_based_location/yoh-ye-pick up 1-101.png"),extent = [0, 66, 0, 44])
        MatplotlibAnimation.ax.plot(point.x, point.y, '.', color=color)

    def setSize(self, size: float):
        MatplotlibAnimation.size = size

    @staticmethod
    def drawPossiblePoints():
        for point in MatplotlibAnimation.noticePoints:
            MatplotlibAnimation.drawPoint(point)

    @staticmethod
    def generalGraphDesign():
        font = {'family': 'serif', 'color': 'darkred', 'size': 15}
        MatplotlibAnimation.ax.set_xlim((0, MatplotlibAnimation.size[0]))
        MatplotlibAnimation.ax.set_ylim((0, MatplotlibAnimation.size[1]))
        MatplotlibAnimation.ax.set_ylabel('Y  axis', fontdict=font)
        MatplotlibAnimation.ax.set_xlabel('X axis', fontdict=font)

    @staticmethod
    def __animate(i):
        MatplotlibAnimation.ax.clear()
        MatplotlibAnimation.generalGraphDesign()

        if MatplotlibAnimation.routers and len(MatplotlibAnimation.routers):
            MatplotlibAnimation.drawAllRouters()
        if MatplotlibAnimation.noticePoints and len(MatplotlibAnimation.noticePoints):
            MatplotlibAnimation.drawPossiblePoints()
        if MatplotlibAnimation.mainPoint:
            MatplotlibAnimation.drawPoint(MatplotlibAnimation.mainPoint, 'b')

    def show(self):
        # ani = animation.FuncAnimation(MatplotlibAnimation.fig, MatplotlibAnimation.__animate,
        #                               fargs=(), interval=1000)
        global showedOnced

        if showedOnced:
            showedOnced = False
            ani = animation.FuncAnimation(MatplotlibAnimation.fig, MatplotlibAnimation.__animate,
                                          fargs=(), interval=1000)
            plt.show()
            plt.close()
        # plt.show()
        # plt.close()

