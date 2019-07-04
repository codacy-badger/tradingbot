import time
import datetime
import requests

with open("currencies") as currencies_file:
    currencies = currencies_file.readlines()

actual_time = time.mktime(datetime.datetime.now().timetuple()) * 1000

for currency in currencies:
    pair, time_frame = currency.split(":")
    time_frame = time_frame.rsplit("\n", 1)[0]

    url = f"https://api-pub.bitfinex.com/v2/candles/trade:{time_frame}:t{pair}/hist?limit=5000&sort=1"

    js = requests.get(url)
    data = js.json()

    with open(f"{pair}_{time_frame}.json", "w") as f:
        f.write(str(data))
    time.sleep(1)
