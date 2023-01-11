from Location.models.Point import Point


class RouterData:
    bssid: str
    originPoint: Point
    signalStrength: float
    wifiType: str


class RouterPoint:
    bssid: str
    originPoint: Point
    distance: float


routers = {
    #yohananof rehovot
    "a8:46:9d:26:90:52": Point(x=1, y=6), "a8:46:9d:26:91:95": Point(1, 15),
           "a8:46:9d:26:90:96": Point(25, 15), "a8:46:9d:26:98:00":Point(-15, 20),

    #yohananof Tel-aviv
        # "d8:38:fc:2c:6f:e8":Point(44.09,7.1),
        # "0c:f4:d5:24:d6:38":Point(43.89,29.15),
        # "d8:38:fc:2c:6f:ec":Point(45.0,13.3),
        # "0c:f4:d5:24:d6:3c":Point(44.12,28.78),

        "0c:f4:d5:31:28:d8":Point(20.5,34.5),
        "0c:f4:d5:31:28:dc":Point(20.5,34.5),
        "0c:f4:d5:24:d6:38":Point(43.5,30),
        "0c:f4:d5:24:d6:3c":Point(43.5,30),
        "d8:38:fc:2c:6f:ec":Point(48,11),
        "d8:38:fc:2c:6f:e8":Point(48,11),
        # "0c:f4:d5:31:28:d8":Point(18,16),
        # "0c:f4:d5:31:28:dc":Point(18,16),


    #office

            '70:4c:a5:9e:fb:f1' : Point(1, 1) , 'e8:1c:ba:28:a3:18' : Point(5, 7.5), 'e8:1c:ba:28:a3:19':Point(5,8),
            'e8:1c:ba:28:a3:c0' : Point(4, 10.5), '70:4c:a5:9e:fb:f0':Point(1.5,1),
    # 'e8:1c:ba:28:a3:c1' : Point(0, 0),

           'a2:dc:a7:60:78:b5' : Point(0, 0), "ca:a4:99:2b:97:a8" : Point(0, 0),'5a:be:85:73:15:cc' : Point(0, 0),
#Home
'b4:0f:3b:31:38:c9': Point(1,1),'b4:0f:3b:31:38:c1':Point(4.6, 11.2), 'c0:ac:54:f7:f7:69':Point(0,0)
    # , '04:95:e6:db:0b:41':Point(14,0)
           }