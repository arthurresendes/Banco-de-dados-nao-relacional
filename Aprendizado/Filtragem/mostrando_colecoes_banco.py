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
    print("Coleções: ")
    for i in db.list_collection_names():
        print(i)
    

if __name__ == "__main__":
    testar_conexao()
    colecoes()