"""Config flow for stormglass.io integration."""
from __future__ import annotations

import logging
import voluptuous as vol
import async_timeout

from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers import selector
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (
    CONF_API_KEY,
    CONF_LATITUDE,
    CONF_LONGITUDE,
    CONF_NAME
)

from .api import StormglassAPI
from .const import (
    DOMAIN, 
    CONF_BEACH,
    DEFAULT_COUNTRY
)
from .countries import BEACHES

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Stormglass config flow."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user interface."""
        _LOGGER.debug("Starting async_step_user...")
        errors = {}

        if user_input is not None:
            coord = user_input[CONF_BEACH].split(',')
            record = [f for f in BEACHES[DEFAULT_COUNTRY] if f["value"] == user_input[CONF_BEACH]][0]
            label = record['label']
            
            await self.async_set_unique_id(
                f"{DOMAIN}.{label}"
                .lower())
            self._abort_if_unique_id_configured()

            valid = await self._test_credentials(
                user_input[CONF_API_KEY],
                float(coord[0]),
                float(coord[1]))
            if valid:
                _LOGGER.debug("Config is valid!")               
                return self.async_create_entry(
                    title= label,
                    data = {
                        CONF_API_KEY: user_input[CONF_API_KEY],
                        CONF_LATITUDE: coord[0],
                        CONF_LONGITUDE: coord[1],
                        CONF_NAME: label
                    }
                ) 
            else:
                errors = {"base": "auth"}

        return self.async_show_form(
            step_id="user", 
            data_schema=vol.Schema({
                vol.Required(CONF_API_KEY): str,
                vol.Required(
                    CONF_BEACH, default=''
                ): selector.selector({ 
                    "select": { 
                        "options": BEACHES[DEFAULT_COUNTRY], 
                        "mode": "dropdown" 
                    } 
                }),
            }),
            errors=errors,
        )

    async def _test_credentials(self, api_key: str, lat: float, long: float) -> bool:
        """Return true if credentials is valid."""
        session = async_get_clientsession(self.hass, True)
        async with async_timeout.timeout(10):
            api = StormglassAPI(session)
            try:
                details = await api.fetchExtremes(api_key, lat, long)
                if details:
                    return True
                return False
            except Exception as exception:
                _LOGGER.error(exception)
                return False