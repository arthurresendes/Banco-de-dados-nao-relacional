from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))

db = client['Simple_Crud']
collection = db['Colaboradores']

def ver_tudo() -> list[dict]:
    res = collection.find() # db.Colaboradores.find()
    lista_res = [i for i in res]
    return lista_res

def adicionar() -> dict:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    query = {'nome': nome, 'idade': idade}
    collection.insert_one(query) # db.Colaboradores.insert({'nome': nome, 'idade': idade})
    return query

def remover() -> dict:
    nome = input("Digite o nome: ")
    query = {'nome': {'$eq': nome}}
    collection.delete_one(query) # db.Colaboradores.deleteOne({'nome': {$eq: nome}})
    return query

def atualizar() -> dict:
    nome = input("Digite o nome da pessoa atualizar: ")
    idade = int(input("Digite a idade: "))
    antigo = {'nome': nome}
    novo = {'$set': {'idade': idade}}
    collection.update_one(antigo,novo) # db.Colaboradores.update({'nome': nome}, {$set: {'idade': idade}})
    return 'Atualizado'

def menu() -> None:
    print("="*50)
    print("1 - Adicionar")
    print("2 - Selecionar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("5 - Sair")
    print("="*50)

if __name__ == "__main__":
    while True:
        menu()
        opcao = int(input(": "))
        if opcao == 1:
            print(adicionar())
        elif opcao == 2:
            print(ver_tudo())
        elif opcao == 3:
            print(atualizar())
        elif opcao == 4:
            print(remover())
        elif opcao == 5:
            print("Saindo")
            break