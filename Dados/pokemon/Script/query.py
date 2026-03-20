from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
cliente = MongoClient(os.getenv("MONGO_URI"))


db = cliente["pokemon_center"]
collection  = db["pokemon"]

def lendarios_count():
    queryLendario = {"legendary": {"$eq": True}}
    res = collection.find(queryLendario)
    contagem = collection.count_documents(queryLendario)
    for i in res:
        print(i)
    return f"Total: {contagem}"

def distinct_generations():
    return collection.distinct("generation")

# i = Sem case sensitive(ignore case), m = modo multilinhas
def name_wih_regex(name):
    query = {"name": {"$regex": name, "$options": "i"}}
    res = collection.find(query, {"_id": False,"name": True, "types": 1,"legendary": True})
    
    for i in res:
        print(i)

def pokemon_with_max_power():
    res = collection.find({}).sort("attack",-1).limit(5)
    for i in res:
        print(i) 


def search_type_in_arrays(tipo):
    query = {"types": tipo}
    res = collection.find(query)
    for i in res:
        print(i)

def search_two_type_in_arrays(tipo1,tipo2):
    query = {"types": {"$in": [tipo1,tipo2]}}
    res = collection.find(query)
    for i in res:
        print(i)

def searche_fire_or_aqua():
    query = {"$or": [
        {"types": {"$regex": "fire", "$options": "i"}},
        {"types": {"$regex": "water", "$options": "i"}}
    ]}
    res = collection.find(query)
    for i in res:
        print(i)

def sort_pokemons():
    res = collection.find({}).sort("name",1)
    for i in res:
        print(i)

def search_pokemon_with_two_types():
    query = {"types": {"$size": 2}}
    res = collection.find(query)
    for i in res:
        print(i)

def search_pokemon_exectaly_with_two_types():
    query = {"types": {"$all": ["Fire", "Water"]}}
    res = collection.find(query)
    for i in res:
        print(i)


def limit_five_max_powerfull_pokemons():
    res = collection.find({}).sort("attack", -1).limit(5)
    for i in res:
        print(i)


def skip():
    page = 3
    itens = 10
    res = collection.find({}).sort("name", 1).skip(page).limit(itens)
    for i in res:
        print(i)

def update_one_legendary():
    antigo = {'legendary': False}
    novo = {'$set': {'legendary': True}}
    collection.update_one(antigo,novo)
    return "Atualizado"

def update_inc():
    antigo = {'hp': 39}
    novo = {'$inc': {'hp': 50, 'speed': -20}}
    collection.update_one(antigo,novo)
    return "Atualizado"

def update_mul():
    antigo = {'defense': 30}
    novo = {'$mul': {'defense': 1.15}}
    collection.update_one(antigo,novo)
    return "Atualizado defesa"

# Caso não exista cria um novo
def update_upsert():
    antigo = {"name": "Pikachu"}
    novo = {"$set": {"attack": 60}}
    collection.update_one(antigo,novo,upsert=True)
    return "Atualizado ataque do pikachu"

def update_in_current_time():
    antigo = {"name": "Pikachu"}
    novo = {"$set": {"speed": 80},"$currentDate": {"data_envio": True,  "logs.timestamp": {"$type": "timestamp"}}}
    collection.update_one(antigo,novo)
    return "Atualizado velocidade do pikachu"