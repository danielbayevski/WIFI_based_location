import math

from Location.models.dataModels import WifiData
from Location.models.LocationPoint import LocationPoint
from Location.models.Point import Point


def getCiceleIntersections(point0: Point, r0: float, point1: Point, r1: float, insideCircle=False) -> list[Point]:
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1
    d = math.sqrt((point1.x - point0.x) ** 2 + (point1.y - point0.y) ** 2)

    # One circle within other
    if d < abs(r0 - r1) and abs(r0 - r1) < 5:
        if insideCircle == False:
            return []
        r0 = r1 + d - 0.5 if r0 - r1 > 0 else r1 - d + 0.5

    # non intersecting
    if d > r0 + r1:
        return []

    # One circle within other
    if d < abs(r0 - r1):
        return []
    # coincident circles
    if d == 0 and r0 == r1:
        return []
    else:
        targetPoint: list[Point] = []
        a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(r0 ** 2 - a ** 2)
        x2 = point0.x + a * (point1.x - point0.x) / d
        y2 = point0.y + a * (point1.y - point0.y) / d
        targetPoint1 = Point()
        targetPoint1.x = x2 + h * (point1.y - point0.y) / d
        targetPoint1.y = y2 - h * (point1.x - point0.x) / d
        targetPoint2 = Point()
        targetPoint2.x = x2 - h * (point1.y - point0.y) / d
        targetPoint2.y = y2 + h * (point1.x - point0.x) / d
        targetPoint.append(targetPoint1)
        targetPoint.append(targetPoint2)
        return targetPoint


def getDistanceBetweenPoints(point1: Point, point2: Point) -> float:
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

def getDistanceFromSignal(wifiData: dict):
    return 100 - wifiData.get('signal')


def isPointInsideCircle(circle: LocationPoint, point: Point) -> bool:
    return getDistanceBetweenPoints(circle.OriginPoint, point) <= circle.distance

# def isPointInsideCircle(circle: LocationPoint, point: Point):
#     # return (((point.x - circle.OriginPoint.x) ** 2) +
#     #                  ((point.x - circle.OriginPoint.x) ** 2)) <= (circle.distance ** 2)
#     return getDistanceBetweenPoints(circle.OriginPoint, point) <= circle.distance

def pointDistanceFromCircle(circle: LocationPoint, point: Point):
    # return (((point.x - circle.OriginPoint.x) ** 2) +
    #                  ((point.x - circle.OriginPoint.x) ** 2)) <= (circle.distance ** 2)
    return math.fabs(getDistanceBetweenPoints(circle.OriginPoint, point) - circle.distance)

def pointDistanceFromCircleCircumference(circle: LocationPoint, point: Point):
    return math.fabs(getDistanceBetweenPoints(circle.OriginPoint, point) - circle.distance)

def calcBestFitDistancesValue(distances: list[float]) -> float:
    return sum(distances) / len(distances)


# https://www.researchgate.net/publication/239919656_Indoor_Location_Using_Trilateration_Characteristics
def signalToDistance(data:WifiData) -> float:
    signal = -32
    power = data.signal / 2 - 100
    Lamda = 0.125
    wave = 20 * math.log10(Lamda / 4 * math.pi)
    P = power - signal
    n = 2
    interfernce = 10 * n
    distance = 1 / math.pow(10, (P - wave) / interfernce)
    return distance