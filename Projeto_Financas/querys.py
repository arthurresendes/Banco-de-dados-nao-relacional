from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))

db = client['Financa_Pessoas']
collection = db['Pessoas']

def insercao(nome:str,salario:float):
    query = {"Nome": nome,"Salario": salario,"Investimento": salario*0.10}
    collection.insert_one(query)

def deletar(nome:str):
    query = {'Nome': {'$eq': nome}}
    res = collection.delete_one(query)
    if res.deleted_count > 0:
        return "Deletado com sucesso"
    else:
        return "Usuario não encontrado"

def atualizar(nome_filter: str,salario: float):
    filtro = {"Nome": nome_filter}
    valores_novos = {"$set": {"Salario": salario, "Investimento": salario*0.10}}
    resultado = collection.update_one(filtro, valores_novos)
    if resultado.matched_count > 0:
        return f"Sucesso: {resultado.modified_count} documento(s) alterado(s)."
    else:
        return "Usuário não encontrado."


def valores_salario(salario_de: float, salario_ate:float):
    query = {'$and': [{'Salario': {'$gte': salario_de}},{'Salario': {'$lte': salario_ate}}]}
    res = collection.find(query)
    lista_users = [i for i in res]
    if lista_users == []:
        return "Sem salarios entre esses valores!"
    else:
        return lista_users

def ver_info_or(nome1: str, nome2: str):
    query = {'$or': [{'Nome': {'$eq': nome1}},{'Nome': {'$eq': nome2}}]}
    res = collection.find(query)
    lista_users = [i for i in res]
    if lista_users == []:
        return "Sem usuarios com esses nomes!"
    else:
        return lista_users

def maior():
    res = collection.find().sort('Investimento', -1).limit(1)
    maior_investimento = []
    for i in res:
        maior_investimento.append(f'Nome: {i['Nome']}, Salario: {i['Salario']}, Porte para investimento: {i['Investimento']}')
    return maior_investimento

def menor():
    res = collection.find().sort('Investimento', 1).limit(1)
    menor_investimento = []
    for i in res:
        menor_investimento.append(f'Nome: {i['Nome']}, Salario: {i['Salario']}, Porte para investimento: {i['Investimento']}')
    return menor_investimento
