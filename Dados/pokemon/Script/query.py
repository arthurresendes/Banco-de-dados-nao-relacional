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

# i = Sem case sensitive, m = modo multilinhas
def name_wih_regex(name):
    query = {"name": {"$regex": name, "$options": "i"}}
    res = collection.find(query)
    
    for i in res:
        print(i)

def pokemon_with_max_power():
    res = collection.find({}).sort("attack",-1).limit(5)
    for i in res:
        print(i) 

pokemon_with_max_power()