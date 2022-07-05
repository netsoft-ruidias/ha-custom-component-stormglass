"""API to stormglass.io."""
import aiohttp
import logging
import json
import time

from .const import EXTREMES_URL

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)


class StormglassAPI:
    """Interfaces to https://api.stormglass.io/v2/tide/extremes/"""
    
    def __init__(self, websession):
        self.websession = websession
        self.json = None

    async def fetchExtremes(self, apiKey: str, lat: float, lng: float):
        try:
            _LOGGER.debug("Fetch Extremes...")
            start = int(time.time())
            end = int(time.time()) + (3600 * 24)
            
            async with self.websession.get(
                EXTREMES_URL, 
                params = { 
                    'lat': lat, 
                    'lng': lng,
                    'start': start,
                    'end': end
                },
                headers = { 
                    "Authorization": apiKey 
                }
            ) as res:
                if res.status == 200 and res.content_type == "application/json":
                    text = await res.text()
                    obj = json.loads(text)
                    if obj['data'] and obj['meta']:
                        _LOGGER.debug(
                            "Fetched Extremes, request nº %s", 
                            obj['meta']['requestCount'])
                        return obj
                    raise Exception("Fetch extremes failed with invalid response.")
                elif res.status == 402 and res.content_type == "application/json":
                    text = await res.text()
                    obj = json.loads(text)
                    raise Exception(
                        f"{obj['errors']['key']}, daily quota {obj['meta']['dailyQuota']}, request count {obj['meta']['requestCount']}.")
                
                raise Exception("Could not fetch extremes, API failed")
        except aiohttp.ClientError as err:
            _LOGGER.exception(err)
        