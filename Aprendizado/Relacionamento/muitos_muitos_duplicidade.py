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

def insercao_n_para_n_exemplo():
    query = [{
    "_id": "f04",
    "cnpj": "165486984",
    "nome": "Fornecedor X",
    "cep": "1098465",
    "produto_ids": [{
        "_id": "p16",
        "descricao": "Dorflex",
        "preco": 45.50}, 
        {"_id": "p21",
        "descricao": "Nimesulida",
        "preco": 14}]
    }, 
    {
    "_id": "f07",
    "cnpj": "98498151",
    "nome": "Fornecedor Y",
    "cep": "198498",
    "produto_ids": [{
        "_id": "p21",
        "descricao": "Nimesulida",
        "preco": 14}, 
        {"_id": "p47",
        "descricao": "Trembolona",
        "preco": 127.46}]
    },

    {
    "_id": "p16",
    "descricao": "Dorflex",
    "preco": 45.50,
    "fornecedor_ids": [{
        "_id": "f04",
        "cnpj": "165486984",
        "nome": "Fornecedor X",
        "cep": "1098465"}]
    },
    {
    "_id": "p21",
    "descricao": "Nimesulida",
    "preco": 14,
    "fornecedor_ids": [{
        "_id": "f04",
        "cnpj": "165486984",
        "nome": "Fornecedor X",
        "cep": "1098465"}, {
        "_id": "f07",
        "cnpj": "98498151",
        "nome": "Fornecedor Y",
        "cep": "198498"}]
    }, 
    {
    "_id": "p47",
    "descricao": "Trembolona",
    "preco": 127.46,
    "fornecedor_ids": [{
        "_id": "f07",
        "cnpj": "98498151",
        "nome": "Fornecedor Y",
        "cep": "198498"}]
}
]

    collection.delete_many({})
    collection.insert_many(query)
    res = collection.find({})
    for i in res:
        print(i)

if __name__ == "__main__":
    print("Isto é um exemplo de um para muitos (n - n). Tanto produtos quanto fornecedores tem sua informação propria e usam uma lista dentro de si com ** duplicidade **, ou seja aparece os dados tanto dentro da lista quanto fora na sua especificação. Exemplo: Fornecedor fabrica produto Z, dentro da lista de produtos terá todas as informações de tal e não apenas o id.")
    insercao_n_para_n_exemplo()