import json

def get_uri(company) -> str:
    """Apartado A: Mostrar la URI de la productura dada"""
    return "DESCONOCIDA"

def movies(company) -> dict[str, str]:
    """Apartado A: Devolver películas producidas por esta productora como un diccionario URI -> título de la película en castellano"""
    return { "http://example.com/inception": "Origen"}

def other_examples() -> dict[str, str]:
    """Apartado D: Devolver otros ejemplos de productoras, en forma de diccionario URI -> nombre de la productura en inglés"""
    return { "http://example.com/ETSITFilms": "ETSIT Films"}

with open('seeders/production.json') as f:
    productions = json.load(f)
    for p in productions:
        print("La URI de la productura es:", get_uri(p))
        print("\tPelículas de esta productora:")
        for (uri, name) in movies(p).items():
            print(f"\t\t{name} - {uri}")


print('Otros ejemplos de productoras')
for (uri, name) in other_examples().items():
    print(f"\t{uri} - {name}")
