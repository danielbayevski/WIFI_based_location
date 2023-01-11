from Location.models.dataModels import WifiData
map = {}


def insertRouter(data: WifiData) -> None:
    map[data.bssid] = data


def insertRouters(routers: list[WifiData]) -> None:
    for router in routers:
        insertRouter(router)


def getLocationList() -> list[WifiData]:
    return map.items()
