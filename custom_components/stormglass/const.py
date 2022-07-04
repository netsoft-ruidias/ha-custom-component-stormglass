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

BEACHES_PT: Dict[str, Any] = { 
    'Praia da Foz do Minho': { 'lat': 41.68, 'lng': -8.83 }, 
    'Praia do Camarido': { 'lat': 41.68, 'lng': -8.83 }, 
    'Praia de Moledo': { 'lat': 41.68, 'lng': -8.83 }, 
    'Praia de Vila Praia de Âncora': { 'lat': 41.68, 'lng': -8.83 }, 
    'Praia da Duna do Caldeirão': { 'lat': 41.68, 'lng': -8.83 }, 
    'Praia do Forte do Cão': { 'lat': 41.68, 'lng': -8.83 }, 
}
