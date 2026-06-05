from pymongo import MongoClient,ASCENDING
from dotenv import load_dotenv
import datetime
import os

load_dotenv()
cliente = MongoClient(os.getenv("MONGO_URI"))

db = cliente["Netflix"]
collection  = db["informations"]

def create_index_release_year():
    collection.create_index([("release_year",1)])



def find_release_year():
    res = collection.find({"release_year": {"$lt": 2010}})
    return list(res)

def simple_find(title: str):
    res = collection.find({"title": title})
    return list(res)

def simple_delete(title: str):
    collection.delete_one({"title": title})
    return "Sucess delete"

def simple_insert():
    collection.insert_one({"type": "TV Show", "title": "The Boys", "date_added": {"$date": "2019-07-26T00:00:00.000Z"}, "release_year": 2019, "rating": "TV-MA", "duration": "4 Seasons", "description": "A fun and irreverent take on what happens when superheroes abuse their superpowers rather than use them for good.", "_id": 81045239, "cast": ["Karl Urban", "Jack Quaid", "Antony Starr", "Erin Moriarty"], "countries": ["United States"], "directors": ["Eric Kripke"], "listed_in": ["Action TV Shows", "TV Sci-Fi & Fantasy", "TV Dramas"]})
    return "Sucess add"

def simple_update(title: str):
    query = {"title": title}
    new_param = {"$set": {"release_year": datetime.datetime.now()}}
    collection.update_one(query,new_param)
    return "Sucess update"

# Operadores de comparação
def seculo_2000():
    res = collection.find({"release_year": {"$gte": 2000}})
    return list(res)

def seculo_passado():
    res = list(collection.find({"release_year": {"$lte": 1999}}))
    return res

def verificar_ator(name: str):
    res = list(collection.find({"cast": {"$in":  [name]}}))
    if len(res) > 0:
        return res
    else:
        return "Nome não encontrado em filmes ou series"

# Operadores logicos
def escolher_ano_ate_ano(anoInicio: int, anoFim: int):
    res = list(collection.find({"$and": [{"release_year": {"$gte": anoInicio, "$lte": anoFim}}]}))
    return res

def busca_por_nomes_semelhantes(name1:str, name2: str):
    res = list(collection.find({"$or": [{"title": {"$eq": name1}},{"title":  {"$eq": name2}}]}))
    return res

def busca_ordenada():
    res = list(collection.find({"listed_in": {"$in": ["Crime TV Shows"]}}).sort('title',-1).limit(5))
    return res