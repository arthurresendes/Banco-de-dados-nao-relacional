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

def operador_exists():
    db = client['Escola_Banco']
    colecao = db['alunos']
    query = {'nome': {'$type': 'string'}}
    filter = colecao.find(query)
    for i in filter:
        print(i)

if __name__ == "__main__":
    testar_conexao()
    operador_exists()