import math
import pandas
import os
from Location.models.dataModels import Point

class special_point:
    bssid_signal_strength = {}
    point: Point

    def __init__(self, bssid_signal:{str:int}, point:Point):
        self.bssid_signal_strength = bssid_signal
        self.point = point

    def __getitem__(self, item):
        return self.bssid_signal_strength[item]


def loadPoints(directory:str):
    #TODO: later turn into numpy and enumerate points and routers,
    # for quicker calculation
    excel_List = os.listdir(directory)
    routers_mapping = [pandas.read_excel(directory + "/" + excl)
                       for excl in excel_List]
    special_points=[]
    for excel in routers_mapping:
        router_names = excel.columns.delete((0,1))
        excel.fillna(0)
        for line in excel.iloc():
            comma = line[0].find(',')
            point = Point(int(line[0][1:comma]),
                          int(line[0][comma + 1:-1]))
            sp = special_point({x:line[x] for x in router_names}, point)
            special_points.append(sp)
    return special_points


special_points=loadPoints('wifi mapping')

def getClosestPoint(bssid_signal:{str:int}):

    closest = []
    min=1000
    global special_points
    for point in special_points:
        sum=0
        count = 0
        for bssid in bssid_signal:
            if bssid in point.bssid_signal_strength:
                if point[bssid] ==0:
                    continue
                sum += abs(point[bssid]-bssid_signal[bssid])
                count+=1
                if count ==4:
                   break
        if min>sum and count>1:
            min=sum
            closest = point.point
    if min < 20:
        return closest
    return None





