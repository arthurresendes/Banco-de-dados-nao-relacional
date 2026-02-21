from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
cliente = MongoClient(os.getenv("MONGO_URI"))
db = cliente['Farmacia']
collection = db['Vendas']

'''
VALE LEMBRAR QUE ISSO É APENAS CODÍGO EXEMPLO A FIM DE APRENDIZADO

'''

def insercao_um_para_n_exemplo():
    query = {
        '_id': 'f01',
        'nome_prod': 'Dorflex',
        'fornecedores': [
            {'nome': 'Empresa X'},
            {'nome': 'Empresa Y'}
        ]
        }
    collection.insert_one(query)
    res = collection.find({})
    for i in res:
        print(i)

if __name__ == "__main__":
    print("Isto é um exemplo de um para muitos (1 - n), pois um produto pode ter varios fornecedores diferentes, ou seja 1 produto tem n fornecedores, assim adicionamos dentro do produto uma lista de fornecedores de tal item.")
    insercao_um_para_n_exemplo()