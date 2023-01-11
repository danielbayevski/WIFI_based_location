import copy
import math

from Location.models.dataModels import WifiData
from Location.models.Point import Point
from Location.models.mapPoints import getClosestPoint

class ApproxmiateMove:

    def __init__(self):
        self.routers: list[WifiData] = []
        self.routersHistory: dict = {}
        self.moves: list[Point] = [Point(0,0)]

    def setRouters(self, routers: list[WifiData]):
        self.routers = routers
        for router in routers:
            if router.bssid not in self.routersHistory:
                self.routersHistory[router.bssid] = [router.signal]

    def setNewMove(self, move: Point):
        self.moves.append(move)

    def getNewRoutersGrid(self, router: list[WifiData]):
        self.routers = router
        self.moves.append(self.calcNextMove())[-20:]


    def calcNextMove(self,use_special_points = True):
        YAxisCounter, XAxisCounter = (0,) * 2
        point = None if not use_special_points \
            else getClosestPoint({router.bssid:
                                      router.signal for router in self.routers})
        if not point:
            for router in self.routers:
                self.routersHistory[router.bssid].append(router.signal)
                if len(self.routersHistory[router.bssid]) > 10:
                    self.routersHistory[router.bssid] = self.routersHistory[router.bssid][-8:]
                if len(self.moves) > 10:
                    self.moves = self.moves[-8:]
                x,y =self.calcOneAxisDirection2(
                        router,self.moves[-1].x,self.moves[-1].y)
                XAxisCounter+=x
                YAxisCounter+=y

            nextMove = self.createNextMove(xCounter=XAxisCounter/len(self.routers), yCounter=YAxisCounter/len(self.routers))
        else:
            nextMove = point
        self.moves.append(nextMove)
        # if self.moves[-2].x != nextMove.x or self.moves[-2].y != nextMove.y:
            # print(nextMove, self.routers[0].signal)

        return nextMove

    def getThreeCircleIntersection(self,X=[],Y=[],R=[]):

        if len(X)<3 or ((Y[0]-Y[1])*(X[1]-X[2]) -
            (Y[1]-Y[2])*(X[0]-X[1])) == 0 or (
                (Y[0] - Y[1]) * (X[1] - X[2]) - (Y[1]
                                                 - Y[2]) * (X[0] - X[1])) ==0:
            return self.moves[-1].x,self.moves[-1].y

        x = ((Y[1]-Y[2])*((Y[1]*Y[1] - Y[0]*Y[0]) + (X[1]*X[1] - X[0]*X[0]) +
                          (R[0]*R[0] - R[1]*R[1])) -(Y[0] - Y[1])
             * ((Y[2] * Y[2] - Y[1] * Y[1]) + (X[2] * X[2] - X[1] * X[1])
                + (R[1] * R[1] - R[2] * R[2])))/ (2*((X[0]-X[1])*(Y[1]-Y[2]) -
                                                     (X[1]-X[2])*(Y[0]-Y[1])))
        y = ((X[1]-X[2])*((X[1]*X[1] - X[0]*X[0]) + (Y[1]*Y[1] - Y[0]*Y[0]) +
                          (R[0]*R[0] - R[1]*R[1])) -(X[0] - X[1])
             * ((X[2] * X[2] - X[1] * X[1]) + (Y[2] * Y[2] - Y[1] * Y[1])
                + (R[1] * R[1] - R[2] * R[2])))/ (2*((Y[0]-Y[1])*(X[1]-X[2]) -
                                                     (Y[1]-Y[2])*(X[0]-X[1])))
        return x,y


    def calcOneAxisDirection2(self, router, userLocX,userLocY) -> int:
        # tan = math.atan((userLocX-router.originPoint.x)/(userLocY-router.originPoint.y))
        dist = math.sqrt(math.pow(userLocX-router.originPoint.x,2) +
                         math.pow(userLocY-router.originPoint.y,2))
        if math.isnan(router.distance):
            return 0,0
        total_dist = dist - router.distance
        percentage = abs(total_dist/dist)
        # if  0.9<percentage <1.1:
        #     return 0,0
        x = (router.originPoint.x-userLocX) * percentage
        y = (router.originPoint.y-userLocY) *percentage

        # x = total_dist * math.sin(tan)
        # y = total_dist * math.cos(tan)
        return x,y



    def calcOneAxisDirection(self,bssid, routerLoc, userLoc) -> int:
        if self.routersHistory.get(bssid)[-2] == self.routersHistory.get(bssid)[-1]:
            return 0

        value = self.routersHistory.get(bssid)[-1] - self.routersHistory.get(bssid)[-2]
        if userLoc == routerLoc and value > 0:
            return 0
        return value
        if userLoc < routerLoc:
            return value
        else:
            return value * -1

        # if userLoc < routerLoc:
        #     if self.routersHistory.get(bssid)[-2] < self.routersHistory.get(bssid)[-1]:
        #         return +1
        #     else:
        #         return -1
        # else:
        #     if self.routersHistory.get(bssid)[-2] < self.routersHistory.get(bssid)[-1]:
        #         return -1
        #     else:
        #         return +1

    def giveDirectionFromCounter(self, counter):
        return counter
        # return retVal

    def createNextMove(self, xCounter, yCounter):
        nextMove: Point = copy.deepcopy(self.moves[-1])
        nextMove.y += self.giveDirectionFromCounter(yCounter)
        nextMove.x += self.giveDirectionFromCounter(xCounter)
        return nextMove

