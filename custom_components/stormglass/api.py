"""API to stormglass.io."""
import aiohttp
import logging
import json
from datetime import timedelta, datetime

from .const import EXTREMES_URL

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)


class StormglassAPI:
    """Interfaces to https://api.stormglass.io/v2/tide/extremes/"""
    
    def __init__(self, websession):
        self.websession = websession
        self.json = None

    async def fetchExtremes(self, apiKey: str, name: str, lat: float, lng: float):
        try:
            start = datetime.utcnow()
            end = start + timedelta(hours=25)
            
            _LOGGER.debug(
                "Fetch Extremes... from %s to %s", 
                start, 
                end)

            async with self.websession.get(
                EXTREMES_URL, 
                params = { 
                    'lat': lat, 
                    'lng': lng,
                    'start': str(start),
                    'end': str(end)
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
                        f"'{name}': {obj['errors']['key']}, request count {obj['meta']['requestCount']} of {obj['meta']['dailyQuota']}.")
                
                raise Exception("Could not fetch extremes, API failed")
        except aiohttp.ClientError as err:
            _LOGGER.exception(err)
        