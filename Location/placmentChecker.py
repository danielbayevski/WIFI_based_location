from Location.models.LocationPoint import LocationPoint
from Location.models.Point import Point
import functools
import Location.MathUtil as mathUtil

import math


# class Point:
#     x: float
#     y: float


class LocationUtil:
    allRaduises = dict()

    # pointsDataMap: list[WifiData] = dict()

    def __init__(self, data: dict = dict()):
        self.pointDataMap: list[LocationPoint] = data.get('pointDataMap') or []

    def setPointDataMap(self, pointDataMap: LocationPoint):
        self.pointDataMap = pointDataMap

    # def findMyLocation(self):
    #     # self.calcAllRadiuses()
    #     # allPosibleLocations: list[Point] = self.findAllPoints()
    #     allPosibleLocations = self.findLoactionPoints()
    #     self.findMostAccurtePoint(allPosibleLocations)

    # @functools.cache
    # def getCirclePointArray(origin : Point, distance) -> list[Point]:
    #     arr: list[Point] = []
    #     for degrees in range(360):
    #         degrees = degrees * np.pi / 180
    #         point = Point()
    #         point.x = distance * np.cos(degrees)
    #         point.y = distance * np.sin(degrees)
    #         arr.append(point)
    #     return arr

    # def getOriginPoint(self, macAdress: str) -> Point:
    #     return Point(1.00, 1.00)

    # def calcAllRadiuses(self):
    #     for wifiData in getLocationList():
    #         self.allRaduises[wifiData.bssid] = self.getCirclePointArray(
    #             self.getOriginPoint(wifiData.bssid),
    #             self.getDistanceFromOrigin(wifiData))

    # def getDistanceFromOrigin(self, data: WifiData) -> list[Point]:
    #     return mathUtil.getDistanceFromSignal(data.signal)

    @functools.cache
    def findLoactionPoints(self) -> list[Point]:
        items: list[LocationPoint] = self.pointDataMap
        possibleLocations: list[Point] = []
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                # possibleLocations.extend(self.getCiceleIntersections(items[i], items[j]))
                possibleLocations.extend(mathUtil.getCiceleIntersections(items[i].OriginPoint, items[i].distance,
                                                                         items[j].OriginPoint, items[j].distance,
                                                                         True))
        return possibleLocations

    def getRouterRangePoints(self, points: list[Point]) -> list[Point]:
        correctPoints: list[Point] = []
        for point in points:
            if self.isPointInRoutersRange(point):
                correctPoints.append(point)
        return correctPoints

    def isPointInRoutersRange(self, point: Point):
        routers: list[LocationPoint] = self.pointDataMap
        for router in routers:
            if not mathUtil.isPointInsideCircle(router, point):
                return False
        return True

    def getDistanceListToRouters(self, point: Point) -> list[float]:
        distances: list[float] = []
        for r in self.pointDataMap:
            distances.append(mathUtil.pointDistanceFromCircle(r, point))
        return distances

    def calcBestPossiblePointFromPoints(self, points) -> Point:
        point: Point
        count = 0
        avg = 0
        for e in points:
            distances = e[1:]
            tempAvg = sum(distances) / len(distances)
            pointInCircleRange = len([element for element in distances if math.fabs(element) < 5])
            if pointInCircleRange > count:
                point = e[0]
                count = pointInCircleRange
                avg = tempAvg
            elif pointInCircleRange == count and avg > tempAvg:
                point = e[0]
                count = pointInCircleRange
                avg = tempAvg
        return point

    def buildPointsDistanceToCircle(self, points: list[Point]) -> list[any]:
        pointAndDistance: list = []
        for p in points:
            pointAndDistance.append([p] + self.getDistanceListToRouters(p))
        return pointAndDistance




    # @functools.cache
    # def getLocationRadiusBetweenTwoPoint(self, item1 : list[Point], item2: list[Point]) -> Point:
    #     min : Point
    #     for sourcePoint in item1:
    #         for targetPoint in item2:
    #             sourcePoint

    # @functools.cache
    def findMostAccurtePoint(self, points: list[Point]) -> Point:
        savedPoint: Point = None
        savedCount: int = 0

        for originPoint in points:
            count = 0
            for point in points:
                dist = mathUtil.getDistanceBetweenPoints(originPoint, point)
                if dist < 3:
                    count += 1
            if savedCount < count:
                savedPoint = point
                savedCount = count
        return savedPoint

    # def pointsInsideCircle

    @staticmethod
    def findDistanceToAllPoint(validPoints : list[Point], circlesItersectionPoints : list[Point]):
        pointsToDistances = {}
        for validPoints in validPoints:
            pointDistances = []
            pointsToDistances[validPoints] = pointDistances
            for p in circlesItersectionPoints:
                pointDistances.append(mathUtil.getDistanceBetweenPoints(validPoints, p))
        return pointsToDistances

    @staticmethod
    def findFinalPoint(pointToDistances: dict, predict):
        savedPoint: Point = None
        savedCount: int = 0
        for key, value in pointToDistances.items():
            lst = list(filter(predict, value))
            if savedCount < len(lst):
                savedPoint = key
                savedCount = len(lst)
                avg = sum(lst) / len(lst)
            elif savedCount == len(lst):
                tempAvg = sum(lst) / len(lst)
                if avg > tempAvg:
                    savedPoint = key
                    savedCount = len(lst)
                    avg = tempAvg
        return savedPoint

    def eliminatePointsThanChoosePoint(self, points: list[Point]) -> Point:
        # validPoints = self.getRouterRangePoints(points)
        # pointToDistances: dict = LocationUtil.findDistanceToAllPoint(validPoints, points)
        # return LocationUtil.findFinalPoint(pointToDistances, lambda x: x < 20)
        validPoints = self.getRouterRangePoints(points)
        return self.calcBestPossiblePointFromPoints(validPoints)
