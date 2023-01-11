from Location.models.Point import Point
from math import pow

class WifiData:
    def __init__(self, bssid: str, signal: str, networkName: str,
                 networkType : str = "", originPoint: Point = Point(0, 0)):
        self.networkName = networkName
        self.bssid = bssid

        self.signal = signal
        self.networkType = networkType
        self.originPoint: Point = originPoint
        self.distance = self.signal_to_distance()

    def __eq__(self, other):
        return self.bssid == other.bssid

    def __le__(self, other):
        return self.signal >= other.signal

    def __lt__(self, other):
        return self.signal > other.signal

    def signal_to_distance(self):
        Pr = (self.signal / 2) - 100
        # 802.11a/n is 14dbm
        Pi = 27.55
        Lamda = 74.48 if (self.networkType=='802.11ac' or
                          self.networkType=='802.11a' or self.bssid[:-1]=="c") else 67.64
        n = 2
        distance = 1 / pow(10, (Pr - Pi + Lamda) / (10 * n))
        # return math.sqrt(math.pow(distance,2)-9)
        return distance
