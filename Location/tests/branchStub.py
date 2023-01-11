
#0026
from Location.models.dataModels import WifiData
brachRouters0026 = [
WifiData(networkName = 'yochananof-wifi', bssid = 'a8:46:9d:26:91:7b', signal = 31.0, networkType = '802.11ax'),
WifiData(networkName = 'yochananof-wifi', bssid = 'a8:46:9d:26:91:95', signal = 67.0, networkType = '802.11ax'),
WifiData(networkName = 'yochananof-wifi', bssid = 'a8:46:9d:26:9a:0d', signal = 50.0, networkType = '802.11ax'),
WifiData(networkName = 'yochananof-wifi', bssid = 'a8:46:9d:26:97:54', signal = 80.0, networkType = '802.11ax'),
WifiData(networkName = 'yochananof-wifi', bssid = 'a8:46:9d:26:90:52', signal = 82.0, networkType = '802.11ax'),
]


def jsonsToWifiDatas(routers) -> list[WifiData]:
    routersList = []
    for router in  routers:
        routersList.append(WifiData(
            networkName=router["networkName"],
            bssid=router["bssid"],
            signal=router["signal"],
            networkType=router["networkType"],
        ))
    return routersList

brachRouters2615 = jsonsToWifiDatas([
{'networkName': 'yochananof-wifi', 'bssid': 'a8:46:9d:26:97:c8', 'signal': 57.0, 'networkType': '802.11ax', 'originPoint': None},
{'networkName': 'yochananof-wifi', 'bssid': 'a8:46:9d:26:90:96', 'signal': 50.0, 'networkType': '802.11ax', 'originPoint': None},
{'networkName': 'yochananof-wifi', 'bssid': 'a8:46:9d:26:98:00', 'signal': 35.0, 'networkType': '802.11ax', 'originPoint': None},
{'networkName': 'yochananof-wifi', 'bssid': 'a8:46:9d:26:91:95', 'signal': 46.0, 'networkType': '802.11ax', 'originPoint': None},
{'networkName': 'yochananof-wifi', 'bssid': 'a8:46:9d:26:90:52', 'signal': 33.0, 'networkType': '802.11ax', 'originPoint': None},
{'networkName': 'yochananof-wifi', 'bssid': 'a8:46:9d:26:97:54', 'signal': 33.0, 'networkType': '802.11ax', 'originPoint': None},
{'networkName': '1', 'bssid': '96:46:9d:26:97:54', 'signal': 72.0, 'networkType': '802.11ax', 'originPoint': None},
{'networkName': '1', 'bssid': '96:46:9d:26:91:95', 'signal': 67.0, 'networkType': '802.11ax', 'originPoint': None},
{'networkName': '1', 'bssid': '96:46:9d:26:98:00', 'signal': 35.0, 'networkType': '802.11ax', 'originPoint': None},
{'networkName': '1', 'bssid': '96:46:9d:26:90:52', 'signal': 38.0, 'networkType': '802.11ax', 'originPoint': None},
])