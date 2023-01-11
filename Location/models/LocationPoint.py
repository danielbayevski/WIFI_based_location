from Location.models.dataModels import WifiData
from Location.models.Point import Point


class LocationPoint:
    # originPoint: Point
    # distance: float

    def __init__(self, originPoint: Point, distance: float):
        self.OriginPoint = originPoint
        self.distance = distance

    @staticmethod
    def RawRoterToLocationPoint(router: WifiData):
        return LocationPoint(router.originPoint, router.distance)

    @staticmethod
    def RawRotersListToLocationPointsList(routers: list[WifiData]):
        lst = []
        for router in routers:
            lst.append(LocationPoint.RawRoterToLocationPoint(router))
        return lst
    # def __str__(self):
    #     point = 'Point(' + str(round(self.originPoint.x, 2)) + ',' + str(round(self.originPoint.y, 2)) + ')'
    #     return 'LocationPoint(' + str(self.originPoint.x) + ',' + str(round(self.distance, 2)) + ')'

    # def __repr__(self):
    #     return 'LocationPoint(' + str(self.originPoint) + ',' + str(round(self.distance, 2)) + ')'