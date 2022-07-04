import asyncio
import aiohttp
from datetime import datetime

from custom_components.stormglass.api import StormglassAPI

async def main():
    async with aiohttp.ClientSession() as session:
        api = StormglassAPI(session)

        details = await api.fetchExtremes(
            "1044e504-c6df-11ec-ab59-0242ac130002-1044e586-c6df-11ec-ab59-0242ac130002", 
            41.444525, 
            -8.780134
        )
        print(details)
        attr = { }
        print (details['data'][0]["type"])
        if "high" in str(details['data'][0]["type"]):
            print("high")
            attr["high_tide_time_utc"] = details['data'][0]["time"]
            attr["high_tide_height"] = details['data'][0]["height"]
            attr["low_tide_time_utc"] = details['data'][1]["time"]
            attr["low_tide_height"] = details['data'][1]["height"]
        elif "low" in str(details['data'][0]["type"]):
            print ("low")
            attr["high_tide_time_utc"] = details['data'][1]["time"]
            attr["high_tide_height"] = details['data'][1]["height"]
            attr["low_tide_time_utc"] = details['data'][0]["time"]
            attr["low_tide_height"] = details['data'][0]["height"]
        print (attr)
        
        high = datetime.timestamp(
            datetime.strptime(attr["high_tide_time_utc"], '%Y-%m-%dT%H:%M:%S:00'))
        low = datetime.timestamp(
            datetime.strptime(attr["low_tide_time_utc"], '%Y-%m-%dT%H:%M:%S:00'))

        print (high)
        print (low)


asyncio.get_event_loop().run_until_complete(main())
