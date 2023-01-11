import threading
import time

from Location.MathUtil import signalToDistance
from Location.activeApp.Animation2 import MatplotlibAnimation
from Location.activeApp.RssiRouters import getRouters, insertOriginPointToRouters
from Location.models.dataModels import WifiData
from Location.models.LocationPoint import LocationPoint

draw = MatplotlibAnimation()


def scanRouter(i):
    while True:
        print('enter')
        routers: list[WifiData] = getRouters()
        #routers: list[WifiData] = stub.brachRouters2615
        routers = insertOriginPointToRouters(routers)
        # font = {'family': 'serif', 'color': 'darkred', 'size': 15}
        # MatplotlibAnimation.ax.set_title('all route points', fontdict=font)
        # MatplotlibAnimation.plotPoint(MatplotlibAnimation.ax, Point(0,20))
        for router in routers:
            router.distance = signalToDistance(router)
            print(router.__dict__)
            if router.originPoint:
                router.distance = signalToDistance(router)
                # print(router.__dict__)
                # MatplotlibAnimation.paintRouter(MatplotlibAnimation.ax, router)

        draw.draw(routers=LocationPoint.RawRotersListToLocationPointsList(routers))
        time.sleep(0.4)
        return routers
        # MatplotlibAnimation.show()

if __name__ == "__main__":

    thread = threading.Thread(target=scanRouter, args=(0,))
    thread.start()
    draw.setSize(15)
    draw.show()



