import asyncio
import aiohttp
import time
from datetime import timedelta, datetime

from custom_components.stormglass.api import StormglassAPI
from custom_components.stormglass.const import DATETIME_FORMAT
from homeassistant.util import dt

from custom_components.stormglass.countries import COUNTRIES, BEACHES

async def main():
    async with aiohttp.ClientSession() as session:
        # api = StormglassAPI(session)

        # details = await api.fetchExtremes(
        #     "1044e504-c6df-11ec-ab59-0242ac130002-1044e586-c6df-11ec-ab59-0242ac130002", 
        #     41.444525, 
        #     -8.780134
        # )
        # print(details)
        attr = { }
        attr["high_tide_time_utc"] = '2022-07-05T14:03:00+00:00'
        attr["low_tide_time_utc"] = '2022-07-05T19:03:00+00:00'

        # print (details['data'][0]["type"])
        # if "high" in str(details['data'][0]["type"]):
        #     print("high")
        #     attr["high_tide_time_utc"] = details['data'][0]["time"]
        #     attr["high_tide_height"] = details['data'][0]["height"]
        #     attr["low_tide_time_utc"] = details['data'][1]["time"]
        #     attr["low_tide_height"] = details['data'][1]["height"]
        # elif "low" in str(details['data'][0]["type"]):
        #     print ("low")
        #     attr["high_tide_time_utc"] = details['data'][1]["time"]
        #     attr["high_tide_height"] = details['data'][1]["height"]
        #     attr["low_tide_time_utc"] = details['data'][0]["time"]
        #     attr["low_tide_height"] = details['data'][0]["height"]
        # print (attr)
        
        high = datetime.timestamp(
            dt.parse_datetime(attr["high_tide_time_utc"]))
        low = datetime.timestamp(
            dt.parse_datetime(attr["low_tide_time_utc"]))

        #high = datetime.timestamp(
        #     datetime.strptime(attr["high_tide_time_utc"], DATETIME_FORMAT))
        #low = datetime.timestamp(
        #     datetime.strptime(attr["low_tide_time_utc"], DATETIME_FORMAT))

        print ("high..:", high)
        print ("low...:", low)

        if (high - low) > 0:
            print (int(50-(((low - datetime.timestamp(datetime.utcnow()))/(high-low)) * 50)), "%")
        else:
            print (int(100-(((high - datetime.timestamp(datetime.utcnow()))/(low-high)) * 50)), "%")

        # start = int(time.time())
        # end = datetime.utcnow().shift(days=1).to('UTC').timestamp()
        # end = int(time.time()) + (3600 * 24)

        start = datetime.utcnow()
        end = start + timedelta(hours=24)
        print ("from/to:", time.time(), start, end)

        st1 = datetime.timestamp(start)
        en1 = datetime.timestamp(end)
        print ("from/to:", st1, en1)

        attr["next_tide_at"] = "2022-07-05T19:03:00+00:00"


        print (" ")
        print (" ")
        now = datetime.utcnow()
        next = datetime.strptime(attr["next_tide_at"], DATETIME_FORMAT)

        diference = next - now
        print ("diference", diference)
        minutes = diference.total_seconds() / 60
        print ("minutes..:", minutes)
        hours = int(minutes / 60)
        print ("hours....:", hours)
        minutes = int(minutes - (hours*60))
        print ("falta....:", f"{hours}h{minutes}")
        print (" ")

        #if (datetime.timestamp(next) > datetime.timestamp(now)):
        if (hours <= 0):
            print ("Agora sim, update")
            #print (now - timedelta(minutes=next.minute))
        else:
            print ("ainda não...")
            
        print (BEACHES['PT'][8])
        print (BEACHES['PT'][8]['value'])
        split = BEACHES['PT'][8]['value'].split(',')
        print (split)
        lat = split[0]
        long = split[1]
        print (lat, long)


asyncio.get_event_loop().run_until_complete(main())
