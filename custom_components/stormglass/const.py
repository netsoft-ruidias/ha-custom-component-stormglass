from typing import Any, Dict

DOMAIN = "stormglass"
PLATFORM = "sensor"
DOMAIN_DATA = f"{DOMAIN}_data"

DEFAULT_ICON = "mdi:waves"
UNIT_OF_MEASUREMENT = "%"

ATTRIBUTION = "Data provided by https://stormglass.io"

EXTREMES_URL = "https://api.stormglass.io/v2/tide/extremes/point"

ATTR_HIGHTIDE_ICON = "mdi:waves-arrow-right"
ATTR_LOWTIDE_ICON = "mdi:waves-arrow-left"

CONF_COUNTRY = "country"
CONF_BEACH = "beach"

DEFAULT_BEACH = "Praia da Foz do Minho"

BEACHES_PT = [
    {"value": { 'lat': 41.68, 'lng': -8.83 }, "label": DEFAULT_BEACH },
    {"value": { 'lat': 41.68, 'lng': -8.83 }, "label": "Praia do Camarido" },
    {"value": { 'lat': 41.68, 'lng': -8.83 }, "label": "Praia de Moledo" },
    {"value": { 'lat': 41.68, 'lng': -8.83 }, "label": "Praia de Vila Praia de Âncora" },
    {"value": { 'lat': 41.68, 'lng': -8.83 }, "label": "Praia da Duna do Caldeirão" },
    {"value": { 'lat': 41.68, 'lng': -8.83 }, "label": "Praia do Forte do Cão" }
]
