from .const import DEFAULT_COUNTRY

COUNTRIES = [
    { "value": DEFAULT_COUNTRY, "label": "Portugal" },
    { "value": "ES", "label": "Spain" },
    { "value": "FR", "label": "France" }
]

BEACHES = {
    "PT": [],
    "ES": [],
    "FR": []
}

## https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Portugal
## https://www.playocean.net/portugal/todas-as-praias-de-portugal
BEACHES["PT"] = [
    ## MINHO
    # Caminha
    { "value": "41.866,-8.863", "label": "CMN: Praia da Foz do Minho" },
    { "value": "41.859,-8.867", "label": "CMN: Praia do Camarido" },
    { "value": "41.849,-8.866", "label": "CMN: Praia de Moledo" },
    { "value": "41.813,-8.865", "label": "CMN: Praia de Vila Praia de Âncora" },
    { "value": "41.808,-8.865,", "label": "CMN: Praia da Duna do Caldeirão" },
    { "value": "41.799,-8.871", "label": "CMN: Praia do Forte do Cão" },
    # Viana do Castelo
    { "value": "41.794,-8.872", "label": "VCT: Praia da Gelfa" },
    { "value": "41.784,-8.871", "label": "VCT: Praia da Ínsua" },
    { "value": "41.780,-8.870", "label": "VCT: Praia de Afife" },
    { "value": "41.769,-8.873", "label": "VCT: Praia da Arda" },
    { "value": "41.758,-8.877", "label": "VCT: Praia de Paçô" },
    { "value": "41.746,-8.877", "label": "VCT: Praia de Fornelos e Promontório de Montedor" },
    { "value": "41.742,-8.876", "label": "VCT: Praia de Carreço" },
    { "value": "41.739,-8.875", "label": "VCT: Praia do Camarido" },
    { "value": "41.735,-8.873", "label": "VCT: Praia do Lumiar" },
    { "value": "41.732,-8.872", "label": "VCT: Praia do Canto Marinho" },
    { "value": "41.725,-8.868", "label": "VCT: Praia do Marco Branco" },
    { "value": "41.711,-8.861", "label": "VCT: Praia do Porto de Vinha" },
    { "value": "41.697,-8.850", "label": "VCT: Praia do Norte" },
    { "value": "41.683,-8.845", "label": "VCT: Praia do Coral" },
    { "value": "41.678,-8.832", "label": "VCT: Praia do Cabedelo" },
    { "value": "41.676,-8.829", "label": "VCT: Praia de Luzia Mar" },
    { "value": "41.667,-8.824", "label": "VCT: Praia do Rodanho" },
    { "value": "41.646,-8.825", "label": "VCT: Praia da Amorosa" },
    { "value": "41.641,-8.822", "label": "VCT: Praia da Amorosa (Sul)" },
    { "value": "41.628,-8.819", "label": "VCT: Praia da Pedra Alta" },
    { "value": "41.624,-8.816", "label": "VCT: Praia de Castelo do Neiva" },
    # Esposende
    { "value": "41.608,-8.808", "label": "EPS: Praia de Antas" },
    { "value": "41.582,-8.804", "label": "EPS: Praia de Belinho" },
    { "value": "41.572,-8.798", "label": "EPS: Praia de São Bartolomeu do Mar" },
    { "value": "41.565,-8.796", "label": "EPS: Praia de Rio de Moinhos" },
    { "value": "41.562,-8.796", "label": "EPS: Praia de Barrelas" },
    { "value": "41.559,-8.795", "label": "EPS: Praia de Marinhas" },
    { "value": "41.554,-8.793", "label": "EPS: Praia de Cepães" },
    { "value": "41.547,-8.792", "label": "EPS: Praia de Suave Mar" },
    { "value": "41.543,-8.792", "label": "EPS: Praia de Esposende" },
    { "value": "41.517,-8.787", "label": "EPS: Praia de Ofir" },
    { "value": "41.513,-8.786", "label": "EPS: Praia de Bonança" },
    { "value": "41.506,-8.787", "label": "EPS: Praia de Fão" },
    { "value": "41.500,-8.788", "label": "EPS: Praia Nova" },
    { "value": "41.495,-8.785", "label": "EPS: Praia de Pedrinhas" },
    { "value": "41.486,-8.781", "label": "EPS: Praia de Apúlia (Norte)" },
    { "value": "41.482,-8.777", "label": "EPS: Praia de Apúlia" },
    { "value": "41.473,-8.775", "label": "EPS: Praia da Ramalha" },
    
    ## DOURO LITORAL
    # Póvoa de Varzim
    { "value": "41.463,-8.776", "label": "PVZ: Praia do Parque de Campismo" },
    { "value": "41.454,-8.777", "label": "PVZ: Praia da Estela" },
    { "value": "41.450,-8.778", "label": "PVZ: Praia do Rio Alto" },
    { "value": "41.444,-8.779", "label": "PVZ: Praia da Barranha" },
    { "value": "41.438,-8.781", "label": "PVZ: Praia da Codixeira" },
    { "value": "41.433,-8.783", "label": "PVZ: Praia da Aguçadoura" },
    { "value": "41.430,-8.783", "label": "PVZ: Praia de Paimó" },
    { "value": "41.422,-8.784", "label": "PVZ: Praia das Pedras Negras" },
    { "value": "41.416,-8.786", "label": "PVZ: Praia de Santo André" },
    { "value": "41.408,-8.782", "label": "PVZ: Praia do Quião" },
    { "value": "41.405,-8.780", "label": "PVZ: Praia de Aver-o-Mar" },
    { "value": "41.403,-8.779", "label": "PVZ: Praia da Boucinha" },
    { "value": "41.402,-8.778", "label": "PVZ: Praia de Coim" },
    { "value": "41.400,-8.778", "label": "PVZ: Praia do Esteiro" },
    { "value": "41.397,-8.778", "label": "PVZ: Praia da Fragosa" },
    { "value": "41.394,-8.777", "label": "PVZ: Praia do Fragosinho" },
    { "value": "41.393,-8.776", "label": "PVZ: Praia de Pontes" },
    { "value": "41.392,-8.775", "label": "PVZ: Praia da Lagoa-I" },
    { "value": "41.391,-8.774", "label": "PVZ: Praia do Hotel" },
    { "value": "41.390,-8.774", "label": "PVZ: Praia da Lagoa-II" },
    { "value": "41.389,-8.774", "label": "PVZ: Praia da Lada-I" },
    { "value": "41.388,-8.774", "label": "PVZ: Praia da Lada-II" },
    { "value": "41.387,-8.774", "label": "PVZ: Praia dos Beijinhos" },
    { "value": "41.385,-8.773", "label": "PVZ: Praia Verde" },
    { "value": "41.384,-8.772", "label": "PVZ: Praia Azul" },
    { "value": "41.383,-8.771", "label": "PVZ: Praia da Salgueira" },
    { "value": "41.381,-8.770", "label": "PVZ: Praia do Carvalhido" },
    { "value": "41.380,-8.769", "label": "PVZ: Praia Redonda" },
    { "value": "41.379,-8.768", "label": "PVZ: Praia do Loulé" },
    { "value": "41.378,-8.768", "label": "PVZ: Praia do Leixão" },
    # Vila do Conde
    { "value": "41.378,-8.768", "label": "VCD: Prainha" },
    # Matosinhos MTS:
    # Porto PRT:
    # Vila Nova de Gaia VNG:
    # Espinho ESP:
    
    ## BEIRA LITORAL
    # Ovar OVR:
    # Murtosa MRS:
    # Aveiro AVR:
    # Ílhavo ILH:
    # Vagos VGS:
    # Mira MIR:
    # Cantanhede CNT:
    # Figueira da Foz FIG:
    # Pombal PBL:
    # Leiria LRA:

    ## ESTREMADURA
    # Marinha Grande MGR:
    # Alcobaça ACB:
    # Nazaré NZR:
    # Caldas da Rainha CLD:
    # Óbidos OBD:
    # Peniche PNI:
    # Lourinhã LNH:
    # Torres Vedras TVD:
    # Mafra MFR:
    # Sintra  SNT:
    # Cascais CSC:
    # Oeiras OER:
    # Almada ALM:
    # Sesimbra SSB:
    # Setúbal STB:

    ## BAIXO ALENTEJO
    # GDL: Grândola
    # STC: Santiago do Cacém
    # SNS: Sines
    # ODM: Odemira

    ## ALGARVE
    # AJZ: Aljezur
    # VBP: Vila do Bispo
    # LGS: Lagos
    # PTM: Portimão
    # LGA: Lagoa
    # SLV: Silves
    # ABF: Albufeira
    # LLE: Loulé
    # FAR: Faro
    # OLH: Olhão
    # TVR: Tavira
    # VRS: Vila Real de Santo António
    # CTM: Castro Marim
]
