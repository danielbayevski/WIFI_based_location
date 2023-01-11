import math



def getDistanceFromRouter(data) -> float:
    Pr = (data.siganlStrenght / 2) - 100
    #802.11a/n is 14dbm
    Pi = getPiDbm(data.NetworkType)
    Lamda = getLamda(data.SignalHZ)
    #2
    n = data.dataLost = 2
    #https://www.researchgate.net/publication/239919656_Indoor_Location_Using_Trilateration_Characteristics
    distance = 1 / math.pow(10,(Pr - Pi - 20 * math.log10(Lamda/(4 * math.pi))) / (10 * n))
    return distance


def getPiDbm(type: str) -> float:
    if(type == "802.11ac"):
        return -30 #14
    raise Exception("NetworkType is unknown")

def getLamda(type: str):
    if (type == "2.4"):
        return 0.125
    if (type == "5.0"):
        return 0.06
    return 0