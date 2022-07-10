"""Platform for sensor integration."""
from __future__ import annotations
from typing import Any, Dict
import aiohttp
import logging

from datetime import timedelta, datetime, timezone
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
SCAN_INTERVAL = timedelta(minutes=2)

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
        self._config = config

        self._attr_low_tide_at: datetime = None
        self._attr_low_tide_height: float = None
        self._attr_high_tide_at: datetime = None
        self._attr_high_tide_height: float = None
        self._attr_next_tide: str = None
        self._attr_next_tide_at: datetime = None
        self._attr_next_tide_in: str = None
        self._attr_datum: str = None
        self._attr_station_name: str = None
        self._attr_station_distance: str = None
        self._attr_stormglass_api_cost: int = None
        self._attr_credits_left: str = None

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
        """Return the unit of measurement the value is expressed in."""
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
        return {
            ATTR_LOW_TIDE_TIME: self._attr_low_tide_at,
            ATTR_LOW_TIDE_HEIGHT: self._attr_low_tide_height,
            ATTR_HIGH_TIDE_TIME: self._attr_high_tide_at,
            ATTR_HIGH_TIDE_HEIGHT: self._attr_high_tide_height,
            ATTR_NEXT_TIDE: self._attr_next_tide,
            ATTR_NEXT_TIDE_AT: self._attr_next_tide_at,
            ATTR_NEXT_TIDE_IN: self._attr_next_tide_in,
            ATTR_DATUM: self._attr_datum,
            ATTR_STATION_NAME: self._attr_station_name,
            ATTR_STATION_DISTANCE: self._attr_station_distance,
            ATTR_STORMGLASS_API_COST: self._attr_stormglass_api_cost,
            ATTR_CREDITS_LEFT: self._attr_credits_left
        }

    def _next_tide_in(self) -> Dict:
        if self._attr_next_tide_at:
            now = datetime.now(timezone.utc)
            next = self._attr_next_tide_at
            diference = next - now
            total_minutes = diference.total_seconds() / 60
            hours = int(total_minutes / 60)
            minutes = int(total_minutes - (hours*60))
            return { 'hours': hours, 'minutes': minutes }
        return { 'hours': 0, 'minutes': 0 }

    def _update_state(self) -> None:
        """Update state with new value."""
        _LOGGER.debug("Update state with new value")
        if self._attr_high_tide_at and self._attr_low_tide_at:
            high = datetime.timestamp(self._attr_high_tide_at)
            low = datetime.timestamp(self._attr_low_tide_at)
            now = datetime.timestamp(datetime.utcnow())

            if (high - low) > 0:
                self._state = int(50-(((low - now)/(high-low)) * 50))
            else:
                self._state = int(100-(((high - now)/(low-high)) * 50))
            _LOGGER.debug("State updated with new value %s", self._state)

            next_tide_in = self._next_tide_in()
            _LOGGER.debug("Update next tide in with new value %s", f"{next_tide_in['hours']}h{next_tide_in['minutes']}")
            self._attr_next_tide_in = f"{next_tide_in['hours']}h{next_tide_in['minutes']}"

            self._available = True

    def _next_tide_index(self, data) -> int:
        """Get next tide index."""
        _LOGGER.debug("Get next tide index")

        index = 0
        now = datetime.utcnow()
        for row in data:
            time = dt.parse_datetime(row["time"]).astimezone(timezone.utc)
            if (datetime.timestamp(time) > datetime.timestamp(now)):
                _LOGGER.debug("Next tide index: %s > %s [%s]", time, now, index)
                return index
            index = index + 1

        _LOGGER.debug("Next tide index: [0]")
        return 0
    
    def _update_attr(self, data, meta) -> None:
        """update sensor attributes from API."""
        _LOGGER.debug("Process data fetched from API and update sensor attributes")

        if data:
            index = self._next_tide_index(data)
            if API_DATA_HIGHTIDE in str(data[index][API_DATA_TYPE]):
                self._attr_high_tide_at = dt.parse_datetime(data[index][API_DATA_TIME]).astimezone(timezone.utc)
                self._attr_high_tide_height = float(data[index][API_DATA_HEIGHT])
                self._attr_low_tide_at = dt.parse_datetime(data[index+1][API_DATA_TIME]).astimezone(timezone.utc)
                self._attr_low_tide_height = float(data[index+1][API_DATA_HEIGHT])
                self._attr_next_tide = API_DATA_HIGHTIDE
                self._attr_next_tide_at = self._attr_high_tide_at
            elif API_DATA_LOWTIDE in str(data[index][API_DATA_TYPE]):
                self._attr_low_tide_at = dt.parse_datetime(data[index][API_DATA_TIME]).astimezone(timezone.utc)
                self._attr_low_tide_height = float(data[index][API_DATA_HEIGHT])
                self._attr_high_tide_at = dt.parse_datetime(data[index+1][API_DATA_TIME]).astimezone(timezone.utc)
                self._attr_high_tide_height = float(data[index+1][API_DATA_HEIGHT])
                self._attr_next_tide = API_DATA_LOWTIDE
                self._attr_next_tide_at = self._attr_low_tide_at
        if meta:
            self._attr_datum = meta[API_META_DATUM]
            self._attr_station_name = meta[API_META_STATION][API_META_NAME]
            self._attr_station_distance = f"{meta[API_META_STATION][API_META_DISTANCE]} Km"
            self._attr_stormglass_api_cost = meta[API_META_COST]
            self._attr_credits_left = int(meta[API_META_DAILYQUOTA]) - int(meta[API_META_REQUESTCOUNT])
        
        if self._attr_high_tide_at and self._attr_low_tide_at:
            _LOGGER.debug("Process data fetched from API: update_state()")
            self._update_state()

        return

    def _is_fetch_needed(self) -> bool:
        """Check if we need to fetch data from the API."""
        _LOGGER.debug("Check if we need to fetch data from the API")

        _next_tide_in = self._next_tide_in()

        _LOGGER.debug(
            "Check if we need to fetch data from the API %s", 
            (_next_tide_in['hours'] <= 0 and _next_tide_in['minutes'] < 15))

        return (_next_tide_in['hours'] <= 0 and _next_tide_in['minutes'] < 15)

    async def async_update(self) -> None:
        """Fetch new state data for the sensor."""
        _LOGGER.debug("Fetch new state data for the sensor.")

        api = self._api
        config = self._config

        if (self._is_fetch_needed()):
            try:        
                details = await api.fetchExtremes(
                    config[CONF_API_KEY], 
                    config[CONF_NAME], 
                    float(config[CONF_LATITUDE]),
                    float(config[CONF_LONGITUDE]))
                if (details):
                    self._update_attr(
                        details['data'],
                        details['meta'])
                    
            except aiohttp.ClientError as err:
                self._available = False
                _LOGGER.exception("Error fetching data from Stormglass.io API.", err)
        else:
            _LOGGER.debug("No Fetch needed, only update state data for the sensor.")
            self._update_state()