from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))

db = client['Estoque_Comercio']
collection = db['Produtos']

def inserindo():
    query_one = {"nome": "Computador", "preco": 2220.99, "quantidade": 20, "informacoes": {"marca": "XXX", "bateria": "5000mAh", "armazenamento": "128GB"}}
    collection.insert_one(query_one)
    query_many = [
    {"nome": "Celular SS", "preco": 3220.99, "quantidade": 50, "informacoes": {"marca": "SSS", "bateria": "5000mAh", "armazenamento": "64GB"}},
    {"nome": "Computador", "preco": 4501.99, "quantidade": 10, "informacoes": {"marca": "ZZZ", "bateria": "5000mAh", "armazenamento": "256GB"}}
    ]
    collection.insert_many(query_many)

def visualizando():
    res = collection.find({})
    print("Visualizando todos: ")
    for i in res:
        print(i)

    query = {'informacoes.armazenamento': {'$eq': '256GB'}}
    res_one_especifico = collection.find_one(query)
    for i,j in res_one_especifico.items():
        if i == '_id':
            pass
        else:
            print(f"{i}: {j}")

def atualizando():
    query_antiga = {'nome': 'Celular SS'}
    query_atual = {'$set': {'nome': 'Celular SSX'}}
    res = collection.find_one_and_update(query_antiga,query_atual)
    print(res)

def deletando():
    query = {'informacoes.marca': 'XXX'}
    collection.delete_one(query)

def contagem():
    res = collection.count_documents({})
    print(f"Quantidade de produtos: {res}")

def ordenacao():
    res_crescente = collection.find().sort('preco',1)
    res_decrescente = collection.find().sort('preco',-1)
    print("Ordenação em ordem crescente: ")
    for i in res_crescente:
        print(i)
    print("Ordenação em ordem decrescente: ")
    for i in res_decrescente:
        print(i)

def limite():
    res_limite = collection.find().limit(2)
    print("Limitando apenas para duas consultas: ")
    for i in res_limite:
        print(i)

def filtragem_dinamica():
    query1 = {'$and': [{'quantidade': {'$gte': 15}}, {'quantidade': {'$lte': 40}}]}
    res_logico1 = collection.find(query1)
    print("Filtragem dinamica com and para apenas produtos com quantidade maior igual que 15 e menor igual que 15")
    for i in res_logico1:
        print(i)
    
    query2 = {'$or': [{'nome': {'$eq': 'Computador'}},{'preco': {'$gt': 4000.00}}]}
    res_logico2 = collection.find(query2)
    print("Filtragem dinamica com operador OR")
    for i in res_logico2:
        print(i)

if __name__ == "__main__":
    inserindo()
    visualizando()
    atualizando()
    deletando()
    contagem()
    ordenacao()
    limite()
    filtragem_dinamica()