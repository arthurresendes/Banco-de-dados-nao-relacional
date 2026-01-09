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

def maior():
    db = client['Escola_Banco']
    collection = db['alunos']
    query = {'idade': {'$gt': 13}}
    all_documents = collection.find(query)
    for i in all_documents:
        print(i)  

def maior_igual():
    db = client['Escola_Banco']
    collection = db['alunos']
    query = {'idade': {'$gte': 13}}
    all_documents = collection.find(query)
    for i in all_documents:
        print(i)    

if __name__ == "__main__":
    testar_conexao()
    print("Maior $gt")
    maior()
    print("Maior igual $gte")
    maior_igual()