from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))

def testar_conexao():
    try:
        client.admin.command('ping')
        print("Conexão estabelecida com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        exit()

def menor():
    db = client['Escola_Banco']
    collection = db['alunos']
    query = {'idade': {'$lt': 13}}
    all_documents = collection.find(query)
    for i in all_documents:
        print(i)  

def menor_igual():
    db = client['Escola_Banco']
    collection = db['alunos']
    query = {'idade': {'$lte': 13}}
    all_documents = collection.find(query)
    for i in all_documents:
        print(i)    

if __name__ == "__main__":
    testar_conexao()
    print("Maior $lt")
    menor()
    print("Menor igual $lte")
    menor_igual()