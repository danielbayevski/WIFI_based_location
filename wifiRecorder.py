
import subprocess
import time


from pynput import keyboard
import pandas
import os
from Location.models.dataModels import WifiData
from Location.wifiSignal import getWifiSignalList
from Location.activeApp.RssiRouters import getRouters
# import numpy as np
import pandas as pd
import tkinter
from tkinter import Toplevel,Message,messagebox

#
# def onKey(key):
#     global wifiSignals
#     global index
#     if key == keyboard.Key.esc:
#         wifiSignals = pd.DataFrame.drop(wifiSignals,columns = 0)
#         num = len(os.listdir('.'))
#         with pd.ExcelWriter("wifiSignals"+str(num)+'.xls') as writer:
#             wifiSignals.to_excel(writer)
#         exit(0)
#     elif key == keyboard.Key.space:
#         routers: list[WifiData] = getWifiSignalList(True)
#
#         for router in routers:
#             if not router.bssid in wifiSignals.columns:
#                 wifiSignals[router.bssid] = 0
#             wifiSignals[router.bssid].iloc[index]=router.signal
#         wifiSignals = wifiSignals.append([0], ignore_index = True)
#         index+=1
#
#         print("index")


import matplotlib.pyplot as plt
from tkinter import *
root=Tk()
class wifiRecorder:

    def __init__(self,root,x=0,y=0):
        self.root = root
        self.current_coordiantes = [int(x), int(y)]
        self.index = 0
        self.wifiSignals = pandas.DataFrame([0])



    def record_entry(self,network_name,direction,canvas,ax):

        routers: list[WifiData] = getRouters(removeUnkownRouters = True)
        if self.wifiSignals.shape[0]==0:
            self.wifiSignals = self.wifiSignals.concat([0])
        for router in routers:
            if (not (router.networkName == network_name)) and network_name:
                continue
            if not router.bssid in self.wifiSignals.columns:
                self.wifiSignals.loc[router.bssid] = 0
            self.wifiSignals[router.bssid][self.index] = router.signal
        self.wifiSignals.loc[0][self.index] = str(self.current_coordiantes)
        self.wifiSignals = pd.concat([self.wifiSignals, pd.DataFrame([0])], ignore_index = True, axis = 0)
        self.index += 1
        ax.add_patch(
            plt.Circle((self.current_coordiantes[0], self.current_coordiantes[1]),
                       0.5, fill = True))
        self.current_coordiantes = [self.current_coordiantes[0] + direction[0],
                                    self.current_coordiantes[1] + direction[1]]
        canvas.configure(text=self.current_coordiantes)
        plt.pause(0.001)



    def stop_record(self,canvas,canv,direction,x,y):

        # wifiSignals = pd.DataFrame.drop(wifiSignals, columns = 0)
        self.wifiSignals = self.wifiSignals.drop(self.wifiSignals.shape[0]-1)
        with pd.ExcelWriter("wifiSignals [" + str(x) +","+ str(y)+ ']'+
                            str(direction) +'.xls') as writer:
            self.wifiSignals.to_excel(writer)
        canvas.destroy()
        canv.pack()

def record(x,y,direction,canv,network_name,storeSizeX=100,storeSizeY=100):
    recorder = wifiRecorder(root,x,y)
    canv.pack_forget()
    if direction == 'north':
        direct = [0, 2]
    elif direction ==  "south":
        direct = [0, -2]
    elif direction ==  "east":
        direct = [-2, 0]
    elif direction == "west":
        direct = [2, 0]
    else:
        direct = [0, 0]
    fig, ax = plt.subplots()
    store_limits = [int(storeSizeY),int(storeSizeX)]  #<-store limits in [y,x]
    ax.imshow(plt.imread("yoh-ye-pick up 1-101.png"),extent = [0, store_limits[0], 0, store_limits[1]])
    plt.xlim([0, store_limits[0]])
    plt.ylim([0, store_limits[1]])
    plt.ion()
    plt.show()
    canvas = Canvas(root, width=400, height=300)
    canvas.pack()

    current_coordiantes = [int(x),int(y)]


    label2 = Label(canvas, text = "next_coordiantes:")
    label2.place(x = 150, y = 20)
    label = Label(canvas,text = current_coordiantes)
    label.place(x =200,y=40)
    # canvas.create_text(100, 50, label)
    button1 = Button(text = 'record entry',
                    command = lambda: recorder.record_entry(network_name,
                                                            direct,
                                                            label,
                                                            ax))
    button2 = Button(text = 'done',
                     command = lambda: recorder.stop_record(canvas,
                                                   canv,
                                                   direction,
                                                   x,
                                                   y))
    canvas.create_window(200, 100, window = button1)
    canvas.create_window(200, 200, window = button2)




def record_box():
    global root
    canvas = Canvas(root,width=200,height=300)
    canvas.pack()
    y,x,direction = Entry(canvas),Entry(canvas),Entry(canvas)
    network_name = Entry(canvas)
    storeSizeX,storeSizeY = Entry(canvas),Entry(canvas)
    canvas.create_text(100, 10, text = 'enter network name: ')
    canvas.create_window(100, 50, window = network_name, width = 100)
    canvas.create_text(100, 80, text = 'enter start coordinates: ')
    canvas.create_window(75, 100, window = x, width = 40)
    canvas.create_window(125, 100, window = y, width = 40)
    canvas.create_text(100, 150, text = 'enter direction: north,south,east,west')
    canvas.create_window(100, 170, window = direction)
    canvas.create_text(100, 200,
                       text = 'store size x,y in meters')
    canvas.create_window(75, 225, window = storeSizeX, width = 40)
    canvas.create_window(125, 225, window = storeSizeY, width = 40)
    button = Button(text='ok',
                    command=lambda: record(int(x.get()),
                                           int(y.get()),
                                           direction.get(),
                                           canvas,
                                           network_name.get(),
                                           int(storeSizeX.get()),
                                           int(storeSizeY.get())))
    canvas.create_window(100, 250, window = button)

    root.mainloop()


if __name__ == "__main__":

    record_box()
    # listener = keyboard.Listener(on_press=onKey)
    # listener.start()  # start to listen on a separate thread
    # listener.join()


