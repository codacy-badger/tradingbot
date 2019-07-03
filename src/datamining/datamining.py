import requests
import datetime,time
import simplejson
currencies_file = open("currencies", "r")
currencies = []
for line in currencies_file:
    currencies.append(line)
actual_time = time.mktime(datetime.datetime.now().timetuple()) * 1000

for i in range(len(currencies)):
    split_currency = currencies[i].split(":")
    pair,timeframe = split_currency[0],split_currency[1]
    timeframe = timeframe.split("\n")[0]
    url = "https://api-pub.bitfinex.com/v2/candles/trade:" + timeframe + ":t" + pair + "/hist?limit=5000&sort=1"
    js = requests.get(url)
    data = js.json()
    f = open( pair + timeframe + ".json", "w")
    f.write(str(data))
    time.sleep(1)