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

## https://www.playocean.net/portugal/todas-as-praias-de-portugal
BEACHES["PT"] = [
    ## MINHO
    # Caminha
    { "value": "41.866,-8.863", "label": "CMN: Praia da Foz do Minho" },
    { "value": "41.859,-8.867", "label": "CMN: Praia do Camarido" },
    { "value": "41.849,-8.866", "label": "CMN: Praia de Moledo" },
    { "value": "41.813,-8.865", "label": "CMN: Praia de Vila Praia de Âncora" },
    { "value": "41.808,-8.865", "label": "CMN: Praia da Duna do Caldeirão" },
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
    { "value": "41.363,-8.760", "label": "VCD: Praia do Senhor dos Navegantes" },
    { "value": "41.362,-8.760", "label": "VCD: Praia dos Barcos" },
    { "value": "41.361,-8.758", "label": "VCD: Praia de Mar e Sol" },
    { "value": "41.360,-8.758", "label": "VCD: Praia de Luzimar" },
    { "value": "41.359,-8.757", "label": "VCD: Praia do Pôr do Sol" },
    { "value": "41.358,-8.756", "label": "VCD: Praia Atlântica" },
    { "value": "41.355,-8.754", "label": "VCD: Praia das Caxinas" },
    { "value": "41.353,-8.754", "label": "VCD: Praia da Olinda" },
    { "value": "41.350,-8.754", "label": "VCD: Praia do Turismo" },
    { "value": "41.347,-8.753", "label": "VCD: Praia Azul" },
    { "value": "41.344,-8.753", "label": "VCD: Praia da Ladeira" },
    { "value": "41.342,-8.753", "label": "VCD: Praia do Forno" },
    { "value": "41.342,-8.752", "label": "VCD: Praia do Seca" },
    { "value": "41.340,-8.750", "label": "VCD: Praia da Senhora da Guia" },
    { "value": "41.339,-8.744", "label": "VCD: Praia da Azurara" },
    { "value": "41.330,-8.739", "label": "VCD: Praia de Árvore" },
    { "value": "41.312,-8.739", "label": "VCD: Praia da Areia" },
    { "value": "41.309,-8.740", "label": "VCD: Praia de Mindelo" },
    { "value": "41.303,-8.737", "label": "VCD: Praia do Pinhal dos Eléctricos" },
    { "value": "41.301,-8.737", "label": "VCD: Praia de Laderça" },
    { "value": "41.298,-8.737", "label": "VCD: Praia da Terra Nova" },
    { "value": "41.295,-8.736", "label": "VCD: Praia da Congreira" },
    { "value": "41.290,-8.733", "label": "VCD: Praia de Vila Chã" },
    { "value": "41.288,-8.732", "label": "VCD: Praia do Pucinho" },
    { "value": "41.285,-8.731", "label": "VCD: Praia de Moreiró" },
    { "value": "41.283,-8.731", "label": "VCD: Praia de São Paio" },
    { "value": "41.274,-8.728", "label": "VCD: Praia de Labruge" },
    # Matosinhos:
    { "value": "41.267,-8.726", "label": "MTS: Praia de Angeiras" },
    { "value": "41.262,-8.725", "label": "MTS: Praia do Barreiro" },
    { "value": "41.260,-8.724", "label": "MTS: Praia Central" },
    { "value": "41.257,-8.723", "label": "MTS: Praia do Funtão" },
    { "value": "41.252,-8.723", "label": "MTS: Praia das Pedras Brancas" },
    { "value": "41.249,-8.725", "label": "MTS: Praia das Pedras do Corgo" },
    { "value": "41.242,-8.727", "label": "MTS: Praia das Pedras da Agudela" },
    { "value": "41.239,-8.725", "label": "MTS: Praia da Agudela" },
    { "value": "41.237,-8.723", "label": "MTS: Praia da Quebrada" },
    { "value": "41.235,-8.723", "label": "MTS: Praia do Marreco" },
    { "value": "41.230,-8.721", "label": "MTS: Praia da Memória" },
    { "value": "41.227,-8.720", "label": "MTS: Praia do Facho" },
    { "value": "41.224,-8.716", "label": "MTS: Praia do Paraíso" },
    { "value": "41.220,-8.714", "label": "MTS: Praia do Cabo do Mundo" },
    { "value": "41.217,-8.714", "label": "MTS: Praia das Salinas" },
    { "value": "41.208,-8.715", "label": "MTS: Praia do Aterro" },
    { "value": "41.204,-8.714", "label": "MTS: Praia Azul" },
    { "value": "41.202,-8.713", "label": "MTS: Praia da Boa Nova" },
    { "value": "41.196,-8.709", "label": "MTS: Praia do Fuzelhas" },
    { "value": "41.189,-8.705", "label": "MTS: Praia de Leça da Palmeira" },
    { "value": "41.176,-8.691", "label": "MTS: Praia de Matosinhos" },
    # Porto
    { "value": "41.170,-8.688", "label": "PRT: Praia Internacional" },
    { "value": "41.167,-8.689", "label": "PRT: Praia do Castelo do Queijo" },
    { "value": "41.160,-8.685", "label": "PRT: Praia do Homem do Leme" },
    { "value": "41.158,-8.683", "label": "PRT: Praia do Molhe" },
    { "value": "41.156,-8.681", "label": "PRT: Praia de Gondarém" },
    { "value": "41.153,-8.679", "label": "PRT: Praia da Luz" },
    { "value": "41.152,-8.678", "label": "PRT: Praia dos Ingleses" },
    { "value": "41.149,-8.676", "label": "PRT: Praia do Ourigo" },
    { "value": "41.147,-8.675", "label": "PRT: Praia do Carneiro" },
    { "value": "41.147,-8.674", "label": "PRT: Praia das Pastoras" },
    # Vila Nova de Gaia
    { "value": "41.139,-8.666", "label": "VNG: Praia do Cabedelo do Douro" },
    { "value": "41.129,-8.668", "label": "VNG: Praia de Lavadores" },
    { "value": "41.126,-8.667", "label": "VNG: Praia das Pedras Amarelas" },
    { "value": "41.122,-8.667", "label": "VNG: Praia da Estrela do Mar" },
    { "value": "41.120,-8.665", "label": "VNG: Praia de Salgueiros" },
    { "value": "41.117,-8.663", "label": "VNG: Praia da Sereia da Costa Verde" },
    { "value": "41.115,-8.663", "label": "VNG: Praia de Canide" },
    { "value": "41.105,-8.662", "label": "VNG: Praia de Marbelo" },
    { "value": "41.103,-8.661", "label": "VNG: Praia da Madalena" },
    { "value": "41.092,-8.657", "label": "VNG: Praia de Valadares" },
    { "value": "41.089,-8.656", "label": "VNG: Praia do Sindicato" },
    { "value": "41.084,-8.656", "label": "VNG: Praia do Atlântico" },
    { "value": "41.082,-8.656", "label": "VNG: Praia de Dunas Mar" },
    { "value": "41.079,-8.656", "label": "VNG: Praia de Francelos" },
    { "value": "41.076,-8.657", "label": "VNG: Praia de Francemar" },
    { "value": "41.072,-8.658", "label": "VNG: Praia da Sãozinha" },
    { "value": "41.069,-8.657", "label": "VNG: Praia do Senhor da Pedra" },
    { "value": "41.067,-8.657", "label": "VNG: Praia de Miramar" },
    { "value": "41.058,-8.656", "label": "VNG: Praia de Mar e Sol" },
    { "value": "41.053,-8.655", "label": "VNG: Praia da Areia Branca" },
    { "value": "41.051,-8.655", "label": "VNG: Praia da Aguda" },
    { "value": "41.044,-8.652", "label": "VNG: Praia da Sétima Arte" },
    { "value": "41.040,-8.650", "label": "VNG: Praia da Granja" },
    { "value": "41.033,-8.646", "label": "VNG: Praia de Bocamar" },
    { "value": "41.028,-8.645", "label": "VNG: Praia do Hotel Solverde" },
    { "value": "41.025,-8.645", "label": "VNG: Praia do Brito" },
    { "value": "41.023,-8.644", "label": "VNG: Praia das Pedras da Maré" },
    { "value": "41.021,-8.644", "label": "VNG: Praia do Areal da Marinha" },
    # Espinho
    { "value": "41.014,-8.644", "label": "ESP: Praia da Frente Azul" },
    { "value": "41.009,-8.646", "label": "ESP: Praia da Baía" },
    { "value": "41.002,-8.646", "label": "ESP: Praia da Rua 37" },
    { "value": "40.997,-8.646", "label": "ESP: Praia do Bairro Piscatório" },
    { "value": "40.988,-8.646", "label": "ESP: Praia de Silvalde" },
    { "value": "40.977,-8.649", "label": "ESP: Praia de Paramos" },

    
    ## BEIRA LITORAL
    # Ovar
    { "value": "40.958,-8.654", "label": "OVR: Praia de Esmoriz" },
    { "value": "40.940,-8.658", "label": "OVR: Praia de Cortegaça" },
    { "value": "40.920,-8.661", "label": "OVR: Praia de São Pedro de Maceda" },
    { "value": "40.893,-8.669", "label": "OVR: Praia das Dunas de Ovar" },
    { "value": "40.875,-8.676", "label": "OVR: Praia do Furadouro" },
    { "value": "40.861,-8.679", "label": "OVR: Praia da Marreta" },
    { "value": "40.828,-8.690", "label": "OVR: Praia de Torrão do Lameiro" },
    # Murtosa
    { "value": "40.761,-8.713", "label": "MRS: Praia da Torreira" },
    { "value": "40.754,-8.715", "label": "MRS: Praia da Colónia de Férias" },
    { "value": "40.747,-8.718", "label": "MRS: Praia da Gaivina" },
    { "value": "40.720,-8.728", "label": "MRS: Praia de Muranzel" },
    # Aveiro
    { "value": "40.686,-8.740", "label": "AVR: Praia das Dunas de São Jacinto" },
    { "value": "40.669,-8.746", "label": "AVR: Praia de São Jacinto" },
    # Ílhavo
    { "value": "40.641,-8.748", "label": "ILH: Praia Velha" },
    { "value": "40.639,-8.749", "label": "ILH: Praia Nova" },
    { "value": "40.632,-8.749", "label": "ILH: Praia da Barra" },
    { "value": "40.617,-8.753", "label": "ILH: Praia da Costa Nova" },
    { "value": "40.600,-8.756", "label": "ILH: Praia do Parque de Campismo" },
    { "value": "40.594,-8.757", "label": "ILH: Praia da Costinha" },
    # Vagos
    { "value": "40.579,-8.762", "label": "VGS: Praia da Vagueira" },
    { "value": "40.549,-8.773", "label": "VGS: Praia do Labrego" },
    { "value": "40.544,-8.773", "label": "VGS: Praia da Duna Alta" },
    { "value": "40.537,-8.775", "label": "VGS: Praia da Gafanha da Boa Hora" },
    { "value": "40.527,-8.777", "label": "VGS: Praia da Ponte da Vagueira" },
    { "value": "40.521,-8.781", "label": "VGS: Praia do Areão" },
    # Mira
    { "value": "40.490,-8.791", "label": "MIR: Praia do Poço da Cruz" },
    { "value": "40.452,-8.804", "label": "MIR: Praia de Mira" },
    # Cantanhede 
    { "value": "40.387,-8.824", "label": "CNT: Praia do Palheirão" },
    { "value": "40.360,-8.834", "label": "CNT: Praia dos Almadoiros" },
    { "value": "40.329,-8.844", "label": "CNT: Praia da Tocha" },
    # Figueira da Foz
    { "value": ",", "label": "FIG: " },
    # Pombal
    { "value": "40.003,-8.913", "label": "PBL: Praia do Osso da Baleia" },
    # Leiria
    { "value": "39.938,-8.943", "label": "LRA: Praia do Fausto" },
    { "value": "39.922,-8.951", "label": "LRA: Praia do Pedrogão" },
    { "value": "39.891,-8.965", "label": "LRA: Praia do Vigão" },

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
