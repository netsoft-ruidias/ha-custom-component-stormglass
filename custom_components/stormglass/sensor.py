"""Platform for sensor integration."""
from __future__ import annotations
from typing import Any
import aiohttp
import logging

from datetime import timedelta, datetime
from typing import Any, Callable

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.util import dt
from homeassistant.const import (
    CONF_API_KEY,
    CONF_LATITUDE,
    CONF_LONGITUDE,
    CONF_NAME
)

from .api import StormglassAPI
from .const import (
    DOMAIN, DEFAULT_ICON, UNIT_OF_MEASUREMENT,
    ATTRIBUTION,
    ATTR_HIGH_TIDE_TIME, ATTR_LOW_TIDE_TIME,
    ATTR_HIGH_TIDE_HEIGHT, ATTR_LOW_TIDE_HEIGHT,
    ATTR_NEXT_TIDE, ATTR_NEXT_TIDE_AT, ATTR_NEXT_TIDE_IN,
    ATTR_STORMGLASS_API_COST, ATTR_CREDITS_LEFT, ATTR_DATUM,
    ATTR_STATION_DISTANCE, ATTR_STATION_NAME,

    API_META_COST, API_META_DAILYQUOTA, API_META_REQUESTCOUNT,
    API_META_DATUM, API_META_STATION, API_META_DISTANCE, API_META_NAME,
    API_DATA_TIME, API_DATA_HEIGHT, API_DATA_TYPE,

    API_DATA_HIGHTIDE, API_DATA_LOWTIDE
)

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

# Time between updating data from API
SCAN_INTERVAL = timedelta(minutes=15)

async def async_setup_entry(hass: HomeAssistant, 
                            config_entry: ConfigEntry, 
                            async_add_entities: Callable):
    """Setup sensor platform."""
    session = async_get_clientsession(hass, True)
    api = StormglassAPI(session)
    config = config_entry.data

    sensors = [ StormglassSensor(api, config) ]
    async_add_entities(sensors, update_before_add=True)


class StormglassSensor(SensorEntity):
    """Representation of a Stormglass Tides (Sensor)."""

    def __init__(self, api: StormglassAPI, config: Any):
        super().__init__()
        self._api = api
        self._attr = None
        self._config = config

        self._icon = DEFAULT_ICON
        self._unit_of_measurement = UNIT_OF_MEASUREMENT
        self._device_class = SensorDeviceClass.CURRENT
        self._state_class = SensorStateClass.TOTAL
        self._state = None
        self._available = False
        
    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return self._config[CONF_NAME]
        
    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return f"{DOMAIN}-{self._config[CONF_NAME]}".lower()

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._available

    @property
    def state(self) -> float:
        return self._state

    @property
    def device_class(self):
        return self._device_class

    @property
    def state_class(self):
        return self._state_class

    @property
    def unit_of_measurement(self):
        """Return the unit the value is expressed in."""
        return self._unit_of_measurement

    @property
    def icon(self):
        return self._icon

    @property
    def attribution(self):
        return ATTRIBUTION

    @property
    def extra_state_attributes(self):
        """Return the state attributes of this device."""
        return self._attr

    def _update_state(self, attr) -> None:
        """Update state with new value."""
        if attr[ATTR_HIGH_TIDE_TIME] and attr[ATTR_LOW_TIDE_TIME]:
            high = datetime.timestamp(
                dt.parse_datetime(attr[ATTR_HIGH_TIDE_TIME]))
            low = datetime.timestamp(
                dt.parse_datetime(attr[ATTR_LOW_TIDE_TIME]))

            if (high - low) > 0:
                self._state = int(50-(((low - datetime.timestamp(datetime.utcnow()))/(high-low)) * 50))
            else:
                self._state = int(100-(((high - datetime.timestamp(datetime.utcnow()))/(low-high)) * 50))
            self._available = True

    def _next_tide_index(self, data) -> int:
        """Get next tide index."""
        index = 0
        now = datetime.utcnow()
        for row in data:
            time = dt.parse_datetime(row["time"])
            if (time > now):
                return index
            index = index + 1
        return 0

    def _process_data(self, data, meta) -> None:
        """Check if we need to fetch data from the API."""
        attr = { }

        if data:
            index = self._next_tide_index(data)
            if API_DATA_HIGHTIDE in str(data[index][API_DATA_TYPE]):
                attr[ATTR_HIGH_TIDE_TIME] = data[index][API_DATA_TIME]
                attr[ATTR_HIGH_TIDE_HEIGHT] = data[index][API_DATA_HEIGHT]
                attr[ATTR_LOW_TIDE_TIME] = data[index+1][API_DATA_TIME]
                attr[ATTR_LOW_TIDE_HEIGHT] = data[index+1][API_DATA_HEIGHT]
                attr[ATTR_NEXT_TIDE] = API_DATA_HIGHTIDE
                attr[ATTR_NEXT_TIDE_AT] = attr[ATTR_HIGH_TIDE_TIME]
            elif API_DATA_LOWTIDE in str(data[index][API_DATA_TYPE]):
                attr[ATTR_LOW_TIDE_TIME] = data[index][API_DATA_TIME]
                attr[ATTR_LOW_TIDE_HEIGHT] = data[index][API_DATA_HEIGHT]
                attr[ATTR_HIGH_TIDE_TIME] = data[index+1][API_DATA_TIME]
                attr[ATTR_HIGH_TIDE_HEIGHT] = data[index+1][API_DATA_HEIGHT]
                attr[ATTR_NEXT_TIDE] = API_DATA_LOWTIDE
                attr[ATTR_NEXT_TIDE_AT] = attr[ATTR_LOW_TIDE_TIME]
            attr[ATTR_NEXT_TIDE_IN] = ""
        if meta:
            attr[ATTR_STORMGLASS_API_COST] = meta[API_META_COST]
            attr[ATTR_CREDITS_LEFT] = int(meta[API_META_DAILYQUOTA]) - int(meta[API_META_REQUESTCOUNT])
            attr[ATTR_DATUM] = meta[API_META_DATUM]
            attr[ATTR_STATION_DISTANCE] = meta[API_META_STATION][API_META_DISTANCE]
            attr[ATTR_STATION_NAME] = meta[API_META_STATION][API_META_NAME]
        
        self._attr = attr

        if attr[ATTR_HIGH_TIDE_TIME] and attr[ATTR_LOW_TIDE_TIME]:
            self._update_state(attr)

        return

    def _is_update_needed(self, attr) -> bool:
        """Check if we need to fetch data from the API."""
        if hasattr(attr, ATTR_NEXT_TIDE_AT):
            if attr[ATTR_NEXT_TIDE_AT]:
                now = datetime.utcnow()
                next = dt.parse_datetime(attr[ATTR_NEXT_TIDE_AT])
                diference = next - now
                total_minutes = diference.total_seconds() / 60
                hours = int(total_minutes / 60)
                minutes = int(total_minutes - (hours*60))
                self._attr[ATTR_NEXT_TIDE_IN] = f"{hours}h{minutes}"
                return (hours <= 0 and minutes < 15)
        return True

    async def async_update(self) -> None:
        """Fetch new state data for the sensor."""
        api = self._api
        config = self._config

        attr = self._attr
        if (self._is_update_needed(attr)):
            try:        
                details = await api.fetchExtremes(
                    config[CONF_API_KEY], 
                    config[CONF_NAME], 
                    float(config[CONF_LATITUDE]),
                    float(config[CONF_LONGITUDE]))
                if (details):
                    self._process_data(
                        details['data'],
                        details['meta'])
                    
            except aiohttp.ClientError as err:
                self._available = False
                _LOGGER.exception("Error fetching data from Stormglass.io API.", err)
        else:
            self._update_state(attr)