from Location.MathUtil import getDistanceFromSignal
from Location.models.LocationPoint import LocationPoint
from Location.models.Point import Point
from Location.placmentChecker import LocationUtil

loc = LocationUtil()



def findRouterOriginPoints(points: list[LocationPoint]):
    data = dict()
    data['pointDataMap'] = points
    loc.setPointDataMap(points)
    return loc.findLoactionPoints()


def findLocationPoints(routers: list, originPoints : list[Point]) -> list[list[LocationPoint]]:
    routersPoints = []
    for loc in routers[0]:
        bssid = loc['bssid']
        router: list[LocationPoint] = []
        point = LocationPoint(originPoints[0],
                              getDistanceFromSignal(loc))
        router.append(point)
        route = zip(originPoints[1:], routers[1:])
        for point,otherList  in route:
            for values in otherList:
                if values.get('bssid') == bssid:
                    point = LocationPoint(point,
                                          getDistanceFromSignal(values))
                    router.append(point)
        routersPoints.append(router)
    return routersPoints
