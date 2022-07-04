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
from homeassistant.const import (
    CONF_API_KEY,
    CONF_LATITUDE,
    CONF_LONGITUDE,
    CONF_NAME
)

from .api import StormglassAPI
from .const import (
    DOMAIN, DEFAULT_ICON, UNIT_OF_MEASUREMENT,
    ATTRIBUTION
)

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

# Time between updating data from API
SCAN_INTERVAL = timedelta(hours=6)

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

    def process_data(self, data, meta) -> None:
        attr = { }

        if data:
            if "high" in str(data[0]["type"]):
                attr["high_tide_time_utc"] = data[0]["time"]
                attr["high_tide_height"] = data[0]["height"]
                attr["low_tide_time_utc"] = data[1]["time"]
                attr["low_tide_height"] = data[1]["height"]
                attr["next_tide"] = "high"
                attr["next_tide_at"] = attr["high_tide_time_utc"]
            elif "low" in str(data[0]["type"]):
                attr["low_tide_time_utc"] = data[0]["time"]
                attr["low_tide_height"] = data[0]["height"]
                attr["high_tide_time_utc"] = data[1]["time"]
                attr["high_tide_height"] = data[1]["height"]
                attr["next_tide"] = "low"
                attr["next_tide_at"] = attr["low_tide_time_utc"]
        
        if meta:
            attr['stormglass_api_cost'] = meta['cost']
            attr['daily_quota'] = meta['dailyQuota']
            attr['request_count'] = meta['requestCount']
            attr['datum'] = meta['datum']
            attr['station_distance'] = meta['station']['distance']
            attr['station_name'] = meta['station']['name']
        
        self._attr = attr

        if attr["high_tide_time_utc"] and attr["low_tide_time_utc"]:
            high = datetime.timestamp(
                datetime.strptime(attr["high_tide_time_utc"], '%Y-%m-%dT%H:%M:%S:00'))
            low = datetime.timestamp(
                datetime.strptime(attr["low_tide_time_utc"], '%Y-%m-%dT%H:%M:%S:00'))
            if (high - low) > 0:
                self._state = 50-(((low - datetime.timestamp(datetime.now))/(high-low)) * 50)
            else:
                self._state = 100-(((high - datetime.timestamp(datetime.now))/(low-high)) * 50)
            self._available = True

        return

    async def async_update(self) -> None:
        """Fetch new state data for the sensor."""
        api = self._api
        config = self._config

        try:        
            details = await api.fetchExtremes(
                config[CONF_API_KEY], 
                float(config[CONF_LATITUDE]),
                float(config[CONF_LONGITUDE]))
            if (details):
                self.process_data(
                    details['data'],
                    details['meta'])
                
        except aiohttp.ClientError as err:
            self._available = False
            _LOGGER.exception("Error fetching data from Stormglass.io API.", err)
