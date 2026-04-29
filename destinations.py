"""Aberdeen Airport (ABZ) destinations — April 2026."""

DESTINATIONS = {
    "ABZ": {
        "name": "Aberdeen",
        "routes": {
            "AGP": "Malaga",
            "ALC": "Alicante",
            "AMS": "Amsterdam",
            "BGO": "Bergen",
            "BHD": "Belfast City",
            "BHX": "Birmingham",
            "BOJ": "Bourgas",
            "BRS": "Bristol",
            "CDG": "Paris CDG",
            "CFU": "Corfu",
            "CPH": "Copenhagen",
            "DLM": "Dalaman",
            "DUB": "Dublin",
            "EBJ": "Esbjerg",
            "FAO": "Faro",
            "GDN": "Gdansk",
            "GVA": "Geneva",
            "HUY": "Humberside",
            "KOI": "Kirkwall",
            "KRK": "Krakow",
            "LGW": "London Gatwick",
            "LHR": "London Heathrow",
            "LSI": "Sumburgh",
            "LTN": "London Luton",
            "MAN": "Manchester",
            "MME": "Durham Teesside",
            "NCL": "Newcastle",
            "NQY": "Newquay",
            "NWI": "Norwich",
            "PMI": "Palma",
            "REU": "Reus",
            "RIX": "Riga",
            "RVN": "Rovaniemi",
            "SVG": "Stavanger",
            "TFS": "Tenerife South",
            "WIC": "Wick",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
