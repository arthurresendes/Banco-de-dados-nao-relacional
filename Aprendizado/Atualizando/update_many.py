
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

def atualizar():
    db = client['Escola_Banco']
    colecao = db['alunos']
    antigo = {'idade': 19}
    novo = {'$set': {'idade': 20}}
    colecao.update_many(antigo,novo)
    res = colecao.find()
    for i in res:
        print(i)

if __name__ == "__main__":
    testar_conexao()
    atualizar()