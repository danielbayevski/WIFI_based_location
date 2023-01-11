import subprocess

from models.dataModels import WifiData

results = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=Bssid"]).decode("utf-8")
# print(results)
#results.split('\n\r',str)

def get_list(my_list : list[str], seperator : str, name)-> list:
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

comm = results.split('\r\n')
comm = list(filter(None, comm))
comm = [i.strip()  for i in comm]
wifis = []
index = -1
#print(comm)
for net in comm:
    if net.startswith('SSID'):
        index += 1
        new_wifi = []
        wifis.append(new_wifi)
        wifis[index].append(net)
    else:
        if index > -1:
            wifis[index].append(net)
#print(wifis)
wifis2 = []
routers = []
counter = 1
for p in wifis:
    name = p[0].split(':')[1].strip()
    if name == '':
        name = str(counter)
        counter += 1
    wifis2.append(get_list(p, 'BSSID', name))
#print(wifis2)
states = []

def get_str_from_list(list : [], name) -> str:
    return [s for s in list if name in s][0]

for p in wifis2:
    #print(p)
    for router in p:
        bssid = get_str_from_list(router, "BSSID").split(':', 1)[1].strip()
        #bssid = router[0].split(':', 1)[1].strip()
        signal = float(get_str_from_list(router, "Signal").split(':', 1)[1][:-1].strip())
        networkName = get_str_from_list(router, "NetworkName").split(':')[1].strip()
        networkType = get_str_from_list(router,"Radio type").split(':')[1].strip()
        #state.append({ 'bssid' : bssid, 'signal': signal})
        states.append(WifiData(bssid=bssid, networkType=networkType, signal=signal, networkName=networkName))
#print(state)
#states.sort()
# for state in states:
#     print(state.__dict__)

#wifiDis = list(x for x in states if x.bssid == '7c:03:4c:ba:c5:a4')[0]
for state in states:
    print(str(state.__dict__) + ',')
#print(wifiDis.__dict__)

#print(getDistanceFromRouter(DistCalData(wifiDis[0].signal)))

# print(wifis[2])
# print(get_list(wifis[0], 'BSSID'))




# BSSID 1                 : 70:4c:a5:20:ae:30
#          Signal             : 80%
#          Radio type         : 802.11ac
#          Channel            : 40
#          Basic rates (Mbps) : 6 12 24
#          Other rates (Mbps) : 9 18 36 48 54
