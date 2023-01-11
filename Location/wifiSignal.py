from Location.models.dataModels import WifiData

def __getAllNetworks(comm: list[str]) -> list[list[str]]:
    #['', 'Interface name : Wi-Fi', 'There are 1 networks currently visible.', 'SSID 1 : RIL', 'Network type            : Infrastructure', 'Authentication          : WPA2-Personal', 'Encryption              : CCMP', 'BSSID 1                 : 70:4c:a5:9e:fb:f1', 'Signal             : 96%', 'Radio type         : 802.11ac', 'Channel            : 11', 'Basic rates (Mbps) : 6 12 24', 'Other rates (Mbps) : 9 18 36 48 54']
    wifis = []
    index = -1
    for net in comm:
        if net.startswith('SSID'):
            index += 1
            new_wifi = []
            wifis.append(new_wifi)
            wifis[index].append(net)
        else:
            if index > -1:
                wifis[index].append(net)
    #[['SSID 1 : RIL', 'Network type            : Infrastructure', 'Authentication          : WPA2-Personal', 'Encryption              : CCMP', 'BSSID 1                 : 70:4c:a5:9e:fb:f1', 'Signal             : 96%', 'Radio type         : 802.11ac', 'Channel            : 11', 'Basic rates (Mbps) : 6 12 24', 'Other rates (Mbps) : 9 18 36 48 54']]
    return wifis

def get_str_from_list(list: [], name) -> str:
    return [s for s in list if name in s][0]

def __get_list(my_list : list[str], seperator : str, name)-> list:
    routers = []
    for router_comp in my_list:
        if router_comp.startswith('BSSID'):
            router_list = []
            routers.append(router_list)
            router_list.append("NetworkName : "+ name);
            routers[-1].append( router_comp )
        else:
            if(len(routers)):
                routers[-1].append(router_comp)
    return routers

def __processNetowrks(networks :  list[list[str]]):
    newNetworks = []
    routers = []
    counter = 1
    for p in networks:
        name = p[0].split(':')[1].strip()
        if name == '':
            name = str(counter)
            counter += 1
        newNetworks.append(__get_list(p, 'BSSID', name))
    return newNetworks

def __getRouters(networks : list[list[str]]) -> list[WifiData]:
    states = []
    for p in networks:
        # print(p)
        for router in p:
            bssid = get_str_from_list(router, "BSSID").split(':', 1)[1].strip()
            signal = float(get_str_from_list(router, "Signal").split(':', 1)[1][:-1].strip())
            networkName = get_str_from_list(router, "NetworkName").split(':')[1].strip()
            networkType = get_str_from_list(router, "Radio type").split(':')[1].strip()
            states.append(WifiData(bssid=bssid, signal=signal, networkName=networkName, networkType=networkType))
    return states


def getWifiSignalList(rawNetworks : str) -> list[WifiData]:

    comm = rawNetworks.split('\r\n')
    comm = list(filter(None, comm))
    comm = [i.strip() for i in comm]

    networks = __getAllNetworks(comm)
    networks = __processNetowrks(networks)
    routers = __getRouters(networks)
    return routers

