
import time
import serial
import re

class AccData:
    speed = 0
    distance = 0
    lastSpeed = 0
    lastDistance = 0
    lastAcc = 0

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='Com3',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
list = []
acc_data = AccData()
ser.isOpen()
while(ser.isOpen()):
    list_temp = ser.readline().decode("utf8").split()
#print(list_temp)
    acc = (float(list_temp[0]) - acc_data.lastAcc)
    #print(list_temp[0] + " " + str(acc_data.lastAcc) + " " + str(float(list_temp[0]) - acc_data.lastAcc))
    time = int(list_temp[1]) / 1000
    # print(time)
    acc_data.lastSpeed = acc_data.speed
    acc_data.speed = acc_data.lastSpeed + acc if abs(acc) > 0.05 else 0;
    # if(abs(acc_data.speed)  > 1 ):
    #     print(acc_data.speed)
    #print(acc_data.speed)
    # print(str(acc_data.speed) + " " + str(acc))
    acc_data.distance = acc_data.lastDistance + acc_data.lastSpeed * time * 10
    # if(acc_data.distance - acc_data.lastDistance > 0.5):
    if(acc_data.distance != acc_data.lastDistance):
        print(acc_data.distance)
    acc_data.lastAcc = float(list_temp[0])
    acc_data.lastDistance = acc_data.distance
    # print(list)
ser.close()



