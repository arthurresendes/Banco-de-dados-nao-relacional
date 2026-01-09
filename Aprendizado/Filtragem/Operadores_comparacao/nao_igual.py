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

def nao_igual():
    db = client['Escola_Banco']
    collection = db['alunos']
    query = {'nome': {'$ne': 'Arthur'}}
    all_documents = collection.find(query)
    for i in all_documents:
        print(i)    

if __name__ == "__main__":
    testar_conexao()
    nao_igual()