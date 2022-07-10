from typing import Any, Dict

DOMAIN = "stormglass"
PLATFORM = "sensor"
DOMAIN_DATA = f"{DOMAIN}_data"

DEFAULT_ICON = "mdi:waves"
UNIT_OF_MEASUREMENT = "%"

ATTRIBUTION = "Data provided by https://stormglass.io"

EXTREMES_URL = "https://api.stormglass.io/v2/tide/extremes/point"

API_META_COST = 'cost'
API_META_DAILYQUOTA = 'dailyQuota'
API_META_REQUESTCOUNT = 'requestCount'
API_META_DATUM = 'datum'
API_META_STATION = 'station'
API_META_DISTANCE = 'distance'
API_META_NAME = 'name'
API_DATA_TIME = 'time'
API_DATA_HEIGHT = 'height'
API_DATA_TYPE = 'type'
API_DATA_HIGHTIDE = 'high'
API_DATA_LOWTIDE = 'low'


ATTR_HIGH_TIDE_TIME = "high_tide_at"
ATTR_LOW_TIDE_TIME = "low_tide_at"
ATTR_HIGH_TIDE_HEIGHT = "high_tide_height"
ATTR_LOW_TIDE_HEIGHT = "low_tide_height"
ATTR_NEXT_TIDE = "next_tide"
ATTR_NEXT_TIDE_AT = "next_tide_at"
ATTR_NEXT_TIDE_IN = "next_tide_in"
ATTR_STORMGLASS_API_COST = 'stormglass_api_cost'
ATTR_CREDITS_LEFT = 'credits_left'
ATTR_DATUM = 'datum'
ATTR_STATION_DISTANCE = 'station_distance'
ATTR_STATION_NAME = 'station_name'

ATTR_HIGHTIDE_ICON = "mdi:waves-arrow-right"
ATTR_LOWTIDE_ICON = "mdi:waves-arrow-left"

CONF_COUNTRY = "country"
CONF_BEACH = "beach"

DEFAULT_COUNTRY = "PT"
