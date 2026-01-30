from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))

db = client['Financa_Pessoas']
collection = db['Pessoas']

def insercao(nome:str,salario:float):
    query = {"Nome": nome,"Salario": salario,"Investimento": salario*0.10}
    collection.insert_one(query)


def deletar(nome:str):
    query = {'nome': {'$eq': nome}}
    collection.delete_one(query)