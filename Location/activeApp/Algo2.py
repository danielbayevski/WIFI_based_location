import os
import threading
import time

import matplotlib.pyplot as plt
import pandas

from Location.ApproxmiateMove import ApproxmiateMove
from Location.activeApp.Animation2 import MatplotlibAnimation
from Location.activeApp.RssiRouters import getRouters, signalToDistance
from Location.models.dataModels import WifiData,Point
from Location.models.LocationPoint import LocationPoint
from Location.models.mapPoints import special_point, special_points

draw = MatplotlibAnimation()
# from tkinter import *
#
# class GUI(Frame):
#
#     def __init__(self,master=None):
#         Frame.__init__(self, master)
#         self.grid()
#
#         self.fnameLabel = Label(master, text="First Name")
#         self.fnameLabel.grid()
#
#         self.fnameEntry = StringVar()
#         self.fnameEntry = Entry(textvariable=self.fnameEntry)
#         self.fnameEntry.grid()
#
#         self.lnameLabel = Label(master, text="Last Name")
#         self.lnameLabel.grid()
#
#         self.lnameEntry = StringVar()
#         self.lnameEntry = Entry(textvariable=self.lnameEntry)
#         self.lnameEntry.grid()
#         def buttonClick():
#
#             print("You pressed Submit!")
#             print(self.fnameEntry.get() + " " + self.lnameEntry.get() +",you clicked the button!")
#
#         self.submitButton = Button(master, text="Submit", command=buttonClick)
#         self.submitButton.grid()

# #
# def onclick(event):
#     if event.dblclick:
#         routers = getRouters(True)
#         special_points.append(
#             special_point({router.bssid: router.signal for router in routers}, Point(event.x,event.y)))
#         print("buttons pressed at: " + str(event.x)+','+str(event.y))



def algo2Stpes():
    lastSignal = 0
    calcStep = ApproxmiateMove()
    routers:list[WifiData]=[]
    while True:
        _routers: list[WifiData] = getRouters(removeUnkownRouters=True)
        if len(_routers) == 0:
            continue
        for router in _routers:
            if not router in routers:
                routers.append(router)
            else:
                if routers[routers.index(router)].distance != router.distance/50 + routers[routers.index(router)].distance*49/50:
                    print(router.signal)
                routers[routers.index(router)].distance = router.distance/50 + routers[routers.index(router)].distance*49/50
                routers[routers.index(router)].originPoint = router.originPoint

        calcStep.setRouters(routers)
        routers_: list[LocationPoint] = LocationPoint.RawRotersListToLocationPointsList(routers)
        # print(calcStep.calcNextMove())
        draw.draw(routers=routers_, mainPoint=calcStep.calcNextMove())


#
# def circle_routers():
#     cur_path = "C:/Users/Hp/PycharmProjects\WIFI_based_location/wifi mapping"
#     excel_List = os.listdir(cur_path)
#
#     routers_mapping = pandas.read_excel(cur_path + "/" + excel_List[0])
#     names = []
#     for column in routers_mapping.columns:
#         if routers_mapping[column].isna().sum() < routers_mapping[column].shape[0]/2:
#             names.append(column)
#     routers_real_list:list[WifiData] = []
#     routers_mapping = [pandas.read_excel(cur_path + "/" + excl)
#                        for excl in excel_List]
#     if 'Unnamed: 0' in names:
#         names.remove('Unnamed: 0')
#         if 0 in names:
#             names.remove(0)
#     for column in names:
#         routers: list[WifiData] = []
#         calcStep = ApproxmiateMove()
#         calcStep.moves.append(Point(0, 0))
#         for routerMap in routers_mapping:
#             if not column in routerMap.columns:
#                 continue
#             col = routerMap[column]
#             col = col.fillna(0)
#
#             for j,k in enumerate(col):
#                 comma = routerMap[0][j].find(',')
#                 point = Point(int(routerMap[0][j][1:comma]),int(routerMap[0][j][comma+1:-1]))
#                 router = WifiData(j,k,'I',networkType = '802.11ac',originPoint = point)
#                 router.distance=signalToDistance(router)
#                 routers.append(router)
#
#         routers.sort()
#         if routers[0].distance > 5:
#             continue
#         for r in routers:
#             if r.distance>20:
#                 routers.remove(r)
#         calcStep.setRouters(routers)
#         routers_: list[
#             LocationPoint] = LocationPoint.RawRotersListToLocationPointsList(
#             routers)
#             # print(calcStep.calcNextMove())
#         # for r in routers_:
#         #     ax.add_patch(plt.Circle((r.OriginPoint.x,r.OriginPoint.y),r.distance,fill=False))
#
#         for j in range(200):
#             calcStep.calcNextMove()
#         mainPoint = calcStep.calcNextMove()
#         newRouter = WifiData(column,'100','I','802.11ac',
#                              Point(mainPoint.x,mainPoint.y))
#         routers_real_list.append(newRouter)
#
#     fig, ax = plt.subplots()
#     ax.imshow(plt.imread("C:/Users/Hp/PycharmProjects/WIFI_based_location/yoh-ye-pick up 1-101.png"),extent = [0, 44, 0, 66]) #TODO: change placement
#     # ax = MatplotlibAnimation.ax.imshow(ax, extent = [-10, 30, -10, 20])
#     for r in routers_real_list:
#         ax.add_patch(plt.Circle((r.originPoint.x,r.originPoint.y),0.5,fill=True))
#         ax.annotate(r.bssid,(r.originPoint.x,r.originPoint.y),textcoords="offset points",  # how to position the text
#                             xytext=(0, 5),  # distance from text to points (x,y)
#                             fontsize=5,
#                             ha='center')
#     # ax.add_patch(plt.Circle((mainPoint.x, mainPoint.y), 1,
#     #                         fill = True,color = 'r'))
#
#     plt.xlim([0, 66])
#     plt.ylim([0, 44])
#     plt.show()
#     draw.draw(routers = routers_, mainPoint = calcStep.calcNextMove())



if __name__ == "__main__":
    # guiFrame = GUI()
    # guiFrame.mainloop()
    #circle_routers() #<- function to draw the circles
    thread = threading.Thread(target=algo2Stpes)
    thread.start()
    time.sleep(2)
    # draw.setSize(30)
    draw.show()



