from Location.models.dataModels import WifiData
from Location.tests.branchData.yohananofData import location00, location0003, location0100, loaction0115


def sortWifi(a : WifiData)-> bool:
    return a['bssid']

loaction: list[WifiData] = location00
#loactions.sort(key=sortWifi , reverse=True)
location03 : list[WifiData] = location0003
tLocation0100 = location0100
tLoaction0115 = loaction0115
# loactions = sorted(location03, key=sortWifi, reverse=True)
# for loaction in loactions:
#     print(loaction)
diff = dict()
location2 = location03
for i in range(len(loaction)):
    for loc in location2:
        if loc['bssid'] == loaction[i]['bssid']:
            diff[loc['bssid']] = loaction[i]['signal'] - loc['signal']
            break

for d in  diff.items():
    print(d)
#cars.sort()


