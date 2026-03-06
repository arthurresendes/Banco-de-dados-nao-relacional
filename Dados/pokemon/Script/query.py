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

