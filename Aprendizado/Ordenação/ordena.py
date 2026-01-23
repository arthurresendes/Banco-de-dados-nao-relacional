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
    ordenacao_crescente = collection.find().sort('idade', 1)
    ordenacao_decrescente = collection.find().sort('idade', -1)
    print("Crescente: ")
    for res in ordenacao_crescente:
        print(res)
        
    print("Decrescente: ")
    for res in ordenacao_decrescente:
        print(res)

if __name__ == "__main__":
    testar_conexao()
    colecoes()