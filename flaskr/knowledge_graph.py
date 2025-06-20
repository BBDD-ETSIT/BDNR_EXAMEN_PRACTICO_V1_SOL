import json
import time
from sparql import query

def get_uri(company) -> str:
    """Apartado A: Mostrar la URI de la productura dada"""
    txt = f'''
    SELECT ?uri
    WHERE {{
        ?uri wdt:P31 wd:Q1762059 ;
             rdfs:label "{ company["name"] }"@en .

    }}
    LIMIT 1
    '''
    q = query(txt)
    return q[0]['uri'] if q else None

def movies(uri) -> dict[str, str]:
    """Apartado A: Devolver películas producidas por esta productora como un diccionario URI -> título de la película en castellano"""
    movies = query(f'''
    SELECT ?uri ?name
    WHERE {{
       ?uri wdt:P272 <{uri}>;
            rdfs:label ?name .
        FILTER(LANG(?name) = "en")
    }}
    LIMIT 5
   ''')
    return { m["uri"]: m["name"] for m in movies}

def other_examples() -> dict[str, str]:
    """Apartado D: Devolver otros ejemplos de productoras, en forma de diccionario URI -> nombre de la productura en inglés"""
    res = query('''SELECT ?uri ?name
    WHERE {
        ?uri wdt:P31 wd:Q1762059 ;
             rdfs:label ?name .
        FILTER(LANG(?name) = "en")

    }
    LIMIT 20
    ''')
    return {r['uri']: r['name'] for r in res}

with open('seeders/production.json') as f:
    productions = json.load(f)
    for p in productions:
        print("Productura", p["name"])
        uri = get_uri(p)
        if not uri:
            print("\tNo se pudo encontrar la URI")
            continue
        print("\tURI:", uri)
        print("\tPelículas de esta productora:")
        for (uri, name) in movies(uri).items():
            print(f"\t\t{name} - {uri}")
        time.sleep(1)


print('Otros ejemplos de productoras')
for (uri, name) in other_examples().items():
    print(f"\t{uri} - {name}")
