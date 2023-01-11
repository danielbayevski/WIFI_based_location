import os

import pandas

from Location.ApproxmiateMove import ApproxmiateMove
from Location.models.Point import Point
from Location.models.dataModels import WifiData
from Location.activeApp.RssiRouters import getRouters, signalToDistance
from Location.models.LocationPoint import LocationPoint
import matplotlib.pyplot as plt
from Location.activeApp.Animation2 import MatplotlibAnimation
from Location.models.Router import routers
import math
draw = MatplotlibAnimation()

def signalToDistance_depricated(signal):
    Pr = (signal / 2) - 100
    Pi =  27.55
    Lamda = 67.64
    n = 2
    distance = 1 / math.pow(10, (Pr - Pi + Lamda) / (10 * n))

    return distance



def circle_routers():
    cur_path = "wifi mapping"
    excel_List = os.listdir(cur_path)

    routers_mapping = pandas.read_excel(cur_path + "/" + excel_List[0])
    names = []
    for column in routers_mapping.columns:
        if routers_mapping[column].isna().sum() < routers_mapping[column].shape[0]/2:
            names.append(column)
    routers_real_list:list[WifiData] = []
    routers_mapping = [pandas.read_excel(cur_path + "/" + excl)
                       for excl in excel_List]
    if 'Unnamed: 0' in names:
        names.remove('Unnamed: 0')
        if 0 in names:
            names.remove(0)
    for column in names:
        routers: list[WifiData] = []
        calcStep = ApproxmiateMove()
        calcStep.moves.append(Point(0, 0))
        for routerMap in routers_mapping:
            if not column in routerMap.columns:
                continue
            col = routerMap[column]
            col = col.fillna(0)

            for j,k in enumerate(col):
                comma = routerMap[0][j].find(',')
                point = Point(int(routerMap[0][j][1:comma]),int(routerMap[0][j][comma+1:-1]))
                router = WifiData(j, k, 'I', networkType = '802.11ac', originPoint = point)
                router.distance=signalToDistance(router)
                routers.append(router)


        routers = [x for x in routers if x.signal>=50]


        if len(routers)<1:
            continue
        routers.sort()
        routers = routers[:5]
        # for rout,r in enumerate(routers):
        #     if r.distance>20:
        #         routers= [x for x in routers[:rout]]
        calcStep.setRouters(routers)
        routers_: list[
            LocationPoint] = LocationPoint.RawRotersListToLocationPointsList(
            routers)
            # print(calcStep.calcNextMove())
        # for r in routers_:
        #     ax.add_patch(plt.Circle((r.OriginPoint.x,r.OriginPoint.y),r.distance,fill=False))

        for j in range(30):
            calcStep.calcNextMove()
        mainPoint = calcStep.calcNextMove()
        newRouter = WifiData(column,'100','I','802.11ac',
                             Point(mainPoint.x,mainPoint.y))
        routers_real_list.append(newRouter)

    fig, ax = plt.subplots()
    ax.imshow(plt.imread("yoh-ye-pick up 1-101.png"),extent = [0, 66, 0, 44])
    # ax = MatplotlibAnimation.ax.imshow(ax, extent = [-10, 30, -10, 20])
    for r in routers_real_list:
        ax.add_patch(plt.Circle((r.originPoint.x,r.originPoint.y),0.5,fill=True))
        ax.annotate(r.bssid,(r.originPoint.x,r.originPoint.y),textcoords="offset points",  # how to position the text
                            xytext=(0, 5),  # distance from text to points (x,y)
                            fontsize=5,
                            ha='center')
        print("\"" + str(r.bssid)+"\":"+ str(r.originPoint)+", ")
    # ax.add_patch(plt.Circle((mainPoint.x, mainPoint.y), 1,
    #                         fill = True,color = 'r'))

    plt.xlim([0, 66])
    plt.ylim([0, 44])


    fig.show()
    plt.waitforbuttonpress(100000)
    plt.close()
    # nextMove = calcStep.calcNextMove()

    # draw.draw(routers = routers_, mainPoint = calcStep.calcNextMove())

def show_router_strength():
    cur_path = "wifi mapping"
    excel_List = os.listdir(cur_path)
    routers_mapping = [pandas.read_excel(cur_path + "/" + excl)
                       for excl in excel_List]
    calcStep = ApproxmiateMove()

    for excel in routers_mapping:
        router_names=excel.columns
        excel.fillna(0)
        for line in excel.iloc():
            routs=[]
            ax = plt.subplot()
            ax.imshow(plt.imread("yoh-ye-pick up 1-101.png"),
                      extent = [0, 66, 0, 44])
            comma = line[0].find(',')
            point = Point(int(line[0][1:comma]),
                          int(line[0][comma + 1:-1]))
            ax.add_patch(plt.Circle(
                    (point.x, point.y),
                    0.5,
                    fill = True, color = 'b'))
            for i,col in enumerate(line):
                if router_names[i] in routers:
                    if col==0 or math.isnan(col):
                        continue
                    ax.add_patch(plt.Circle((routers[router_names[i]].x, routers[router_names[i]].y), 0.5,
                                   fill = True,color = 'r'))
                    dist = signalToDistance_depricated(col)
                    ax.add_patch(plt.Circle((routers[router_names[i]].x,
                                             routers[router_names[i]].y), dist,
                                            fill = False, color = 'r'))
                    ax.annotate(str(point.x)+","+str(point.y), (point.x, point.y),
                                textcoords = "offset points",
                                # how to position the text
                                xytext = (0, 5),
                                # distance from text to points (x,y)
                                fontsize = 10,
                                ha = 'center')
                    routs.append(WifiData(router_names[i],col,'l','n',routers[router_names[i]]))
            if len(routs)>0:

                calcStep.setRouters(routs)
                p = calcStep.calcNextMove(False)
                print(p)
                ax.add_patch(plt.Circle(
                        (p.x, p.y),
                        0.5,
                        fill = True, color = 'teal'))


                plt.show(block=False)
                plt.waitforbuttonpress(100)
                plt.close()




if __name__ == "__main__":
    show_router_strength()
    # circle_routers()
