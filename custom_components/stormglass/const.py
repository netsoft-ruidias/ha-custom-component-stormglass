from typing import Any, Dict

DOMAIN = "stormglass"
PLATFORM = "sensor"
DOMAIN_DATA = f"{DOMAIN}_data"

DEFAULT_ICON = "mdi:waves"
UNIT_OF_MEASUREMENT = "%"

ATTRIBUTION = "Data provided by https://stormglass.io"

EXTREMES_URL = "https://api.stormglass.io/v2/tide/extremes/point"

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"

ATTR_HIGHTIDE_ICON = "mdi:waves-arrow-right"
ATTR_LOWTIDE_ICON = "mdi:waves-arrow-left"

CONF_COUNTRY = "country"
CONF_BEACH = "beach"

DEFAULT_COUNTRY = "PT"
COUNTRIES = [
    {"value": DEFAULT_COUNTRY, "label": "Portugal" },
]

## https://www.playocean.net/portugal/todas-as-praias-de-portugal
BEACHES_PT = [
    # Caminha
    {"value": "41.866,-8.863", "label": "CMN: Praia da Foz do Minho" },
    {"value": "41.859,-8.867", "label": "CMN: Praia do Camarido" },
    {"value": "41.849,-8.866", "label": "CMN: Praia de Moledo" },
    {"value": "41.813,-8.865", "label": "CMN: Praia de Vila Praia de Âncora" },
    {"value": "41.808,-8.865", "label": "CMN: Praia da Duna do Caldeirão" },
    {"value": "41.799,-8.871", "label": "CMN: Praia do Forte do Cão" },
    # Viana do Castelo
    {"value": "41.794,-8.872", "label": "VCT: Praia da Gelfa" },
    {"value": "41.784,-8.871", "label": "VCT: Praia da Ínsua" },
    {"value": "41.780,-8.870", "label": "VCT: Praia de Afife" },
    {"value": "11", "label": "VCT: Praia da Arda" },
    {"value": "12", "label": "VCT: Praia de Paçô" },
    {"value": "13", "label": "VCT: Praia de Fornelos e Promontório de Montedor" },
    {"value": "14", "label": "VCT: Praia de Carreço" },
    {"value": "15", "label": "VCT: Praia do Camarido" },
    {"value": "16", "label": "VCT: Praia do Lumiar" },
    {"value": "17", "label": "VCT: Praia do Canto Marinho" },
    {"value": "18", "label": "VCT: Praia do Marco Branco" },
    {"value": "19", "label": "VCT: Praia do Porto de Vinha" },
    {"value": "20", "label": "VCT: Praia do Norte" },
    {"value": "21", "label": "VCT: Praia do Coral" },
    {"value": "22", "label": "VCT: Praia do Cabedelo" },
    {"value": "23", "label": "VCT: Praia de Luzia Mar" },
    {"value": "24", "label": "VCT: Praia do Rodanho" },
    {"value": "25", "label": "VCT: Praia da Amorosa" },
    {"value": "26", "label": "VCT: Praia da Amorosa (Sul)" },
    {"value": "27", "label": "VCT: Praia da Pedra Alta" },
    {"value": "28", "label": "VCT: Praia de Castelo do Neiva" },
    # Esposende
    {"value": "29", "label": "EPS: Praia de Antas" },
    {"value": "30", "label": "EPS: Praia de Belinho" },
    {"value": "31", "label": "EPS: Praia de São Bartolomeu do Mar" },
    {"value": "32", "label": "EPS: Praia de Rio de Moinhos" },
    {"value": "33", "label": "EPS: Praia de Barrelas" },
    {"value": "34", "label": "EPS: Praia de Marinhas" },
    {"value": "35", "label": "EPS: Praia de Cepães" },
    {"value": "36", "label": "EPS: Praia de Suave Mar" },
    {"value": "37", "label": "EPS: Praia de Esposende" },
    {"value": "38", "label": "EPS: Praia de Ofir" },
    {"value": "39", "label": "EPS: Praia de Bonança" },
    {"value": "40", "label": "EPS: Praia de Fão" },
    {"value": "41", "label": "EPS: Praia Nova" },
    {"value": "42", "label": "EPS: Praia de Pedrinhas" },
    {"value": "43", "label": "EPS: Praia de Apúlia (Norte)" },
    {"value": "44", "label": "EPS: Praia de Apúlia" },
    {"value": "45", "label": "EPS: Praia da Ramalha" },
    # Póvoa de Varzim
    {"value": "41.463,-8.776", "label": "PVZ: Praia do Parque de Campismo" },
    {"value": "41.454,-8.777", "label": "PVZ: Praia da Estela" },
    {"value": "41.450,-8.778", "label": "PVZ: Praia do Rio Alto" },
    {"value": "41.444,-8.779", "label": "PVZ: Praia da Barranha" },
    {"value": "41.438,-8.781", "label": "PVZ: Praia da Codixeira" },
    {"value": "41.433,-8.783", "label": "PVZ: Praia da Aguçadoura" },
    {"value": "41.430,-8.783", "label": "PVZ: Praia de Paimó" },
    {"value": "41.422,-8.784", "label": "PVZ: Praia das Pedras Negras" },
    {"value": "41.416,-8.786", "label": "PVZ: Praia de Santo André" },
    {"value": "41.408,-8.782", "label": "PVZ: Praia do Quião" },
    {"value": "41.405,-8.780", "label": "PVZ: Praia de Aver-o-Mar" },
    {"value": "41.403,-8.779", "label": "PVZ: Praia da Boucinha" },
    {"value": "41.402,-8.778", "label": "PVZ: Praia de Coim" },
    {"value": "41.400,-8.778", "label": "PVZ: Praia do Esteiro" },
    {"value": "41.397,-8.778", "label": "PVZ: Praia da Fragosa" },
    {"value": "41.394,-8.777", "label": "PVZ: Praia do Fragosinho" },
    {"value": "41.393,-8.776", "label": "PVZ: Praia de Pontes" },
    {"value": "41.392,-8.775", "label": "PVZ: Praia da Lagoa-I" },
    {"value": "41.391,-8.774", "label": "PVZ: Praia do Hotel" },
    {"value": "41.390,-8.774", "label": "PVZ: Praia da Lagoa-II" },
    {"value": "41.389,-8.774", "label": "PVZ: Praia da Lada-I" },
    {"value": "41.388,-8.774", "label": "PVZ: Praia da Lada-II" },
    {"value": "41.387,-8.774", "label": "PVZ: Praia dos Beijinhos" },
    {"value": "41.385,-8.773", "label": "PVZ: Praia Verde" },
    {"value": "41.384,-8.772", "label": "PVZ: Praia Azul" },
    {"value": "41.383,-8.771", "label": "PVZ: Praia da Salgueira" },
    {"value": "41.381,-8.770", "label": "PVZ: Praia do Carvalhido" },
    {"value": "41.380,-8.769", "label": "PVZ: Praia Redonda" },
    {"value": "41.379,-8.768", "label": "PVZ: Praia do Loulé" },
    {"value": "41.378,-8.768", "label": "PVZ: Praia do Leixão" },
]
