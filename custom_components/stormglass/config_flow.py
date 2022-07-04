"""Config flow for stormglass.io integration."""
from __future__ import annotations

import logging
import voluptuous as vol
import async_timeout


from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (
    CONF_API_KEY,
    CONF_LATITUDE,
    CONF_LONGITUDE,
    CONF_NAME
)

from .api import StormglassAPI
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_API_KEY): cv.string,
    vol.Required(CONF_LATITUDE): cv.latitude,
    vol.Required(CONF_LONGITUDE): cv.longitude,
    vol.Required(CONF_NAME): cv.string,
})


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Stormglass config flow."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user interface."""
        _LOGGER.debug("Starting async_step_user...")
        errors = {}

        if user_input is not None:
            await self.async_set_unique_id(
                f"{user_input[CONF_LATITUDE]},{user_input[CONF_LONGITUDE]}"
                .lower())
            self._abort_if_unique_id_configured()

            name = await self._test_credentials(user_input)
            if name:
                _LOGGER.debug("Config is valid!")
                return self.async_create_entry(
                    title= name,
                    data = user_input
                ) 
            else:
                errors = {"base": "auth"}

        return self.async_show_form(
            step_id="user", 
            data_schema=DATA_SCHEMA, 
            errors=errors,
        )

    async def _test_credentials(self, user_input) -> str:
        """Return true if credentials is valid."""
        session = async_get_clientsession(self.hass, True)
        async with async_timeout.timeout(10):
            api = StormglassAPI(session)
            try:
                details = await api.fetchExtremes(
                    user_input[CONF_API_KEY], 
                    float(user_input[CONF_LATITUDE]),
                    float(user_input[CONF_LONGITUDE])
                )                
                if details:
                    return details['meta']['station']['name']
                else:
                    return None
            except Exception as exception:
                _LOGGER.error(exception)
                return None