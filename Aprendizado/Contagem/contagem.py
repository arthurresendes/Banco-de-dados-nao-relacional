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

def colecoes():
    db = client['Escola_Banco']
    collection = db['alunos']
    print("Quantidade coleções: ")
    first_document = collection.count_documents({})
    print(first_document)
    query = {'nome': {'$eq': 'Arthur'}}
    filter_and_count = collection.count_documents(query)
    print("Coleções com nome Arthur: ")
    print(filter_and_count)

if __name__ == "__main__":
    testar_conexao()
    colecoes()