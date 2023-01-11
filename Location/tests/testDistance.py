import math

from Location.DistanceFromRouter import getDistanceFromRouter

class powerData:
    siganlStrenght: int
    NetworkType : str


data = { "siganlStrenght": "" }

# getDistanceFromRouter()
a = 99
power = a / 2 - 100
#2.4
#signal = 32-25 with 32 as default
#Lamda = 0.125
#5
signal = -25
Lamda = 0.125 # 0.06
n =2
# exp=pow(10,((27.55-(20*math.log10(float(0.05)))+float(power)))/20)
wave = 20 * math.log10(Lamda / 4 * math.pi)
P = power - signal
interfernce = 10 * n
distance = 1 / math.pow(10, (P - wave) / interfernce)

print('power',100 -a)
# distance = math.pow(math.log10(power + 14 - 20 * math.log10(Lamda/(4 * math.pi))) / (10 * n), -10)
print(distance)
