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
    
    query = {'nome': {'$eq': 'Gustavo'}}
    deletar = collection.find_one_and_delete(query)
    print(deletar)
    
    # deletar = collection.delete_one(query) or deletar = collection.delete_many(query)


if __name__ == "__main__":
    testar_conexao()
    colecoes()