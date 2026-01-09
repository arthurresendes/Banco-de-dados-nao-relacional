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

def criando_inserindo_banco():
    db = client['Escola_Banco']
    colecao = db['alunos']
    
    um_aluno = {"nome": "Arthur", "idade": 19, "matricula": "111222"}
    colecao.insert_one(um_aluno)
    varios_alunos = [
        {"nome": "Leticia", "idade": 19, "matricula": "222333"},
        {"nome": "Josias", "idade": 13, "matricula": "333444"},
        {"nome": "Gustavo", "idade": 11, "matricula": "444555"}
    ]
    colecao.insert_many(varios_alunos)
    print("Informações inseridas")

if __name__ == "__main__":
    testar_conexao()
    criando_inserindo_banco()