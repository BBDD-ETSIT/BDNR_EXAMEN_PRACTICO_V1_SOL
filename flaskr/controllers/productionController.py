from models import Production
from sparql import query
from flask import g, request
from mongoengine import Q


def read_productions():
    print("Reading movies...")
    productions = Production.objects()
    print("aaaa")
    print(productions)
    print("bbb")
    
    return productions

def read_productions_by_filter(min_number_of_awards, max_number_of_awards ):
    #Completar la función para filtar por rango de valores de galardones
    productions = Production.objects(
        Q(number_of_awards__gte=min_number_of_awards) & Q(number_of_awards__lte=max_number_of_awards))

    
    return productions


def read_production(alias):
    print("Reading Production...", alias)
    #Completar la función
    production = Production.objects.get(alias=alias)
    print(production)
    
    return production


def create_review(movie_slug, user_id, username, comment, rating):
    print("Creating review...", movie_slug)
    #Completar la función
    movie = ""
    
    return movie 
