from pymongo import MongoClient,ASCENDING
from dotenv import load_dotenv
import os

load_dotenv()
cliente = MongoClient(os.getenv("MONGO_URI"))


db = cliente["Netflix"]
collection  = db["attractive"]

def create_index_release_year():
    collection.create_index([("release_year",1)])

def find_release_year():
    res = collection.find({"release_year": {"$lt": 2010}})
    for i in res:
        print(i)

def simple_find(title: str):
    res = collection.find({"title": title})
    for i in res:
        print(i)

def simple_delete(title: str):
    collection.delete_one({"title": title})
    return "Sucess delete"