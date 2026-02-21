from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
cliente = MongoClient(os.getenv("MONGO_URI"))
db = cliente['Farmacia']
collection = db['Vendas']

def insercao_n_para_n_exemplo():
    query = [{
    "_id": "f04",
    "cnpj": "165486984",
    "nome": "Fornecedor X",
    "cep": "1098465",
    "produto_ids": ["p16", "p21"] # O fornecedor x fabrica os produtos com ids p16 e p21,
    }, 
    {
    "_id": "f07",
    "cnpj": "98498151",
    "nome": "Fornecedor Y",
    "cep": "198498",
    "produto_ids": ["p21", "p47"] # O fornecedor Y fabrica os produtos com ids p47 e p21,
    },

    {
    "_id": "p16",
    "descricao": "Dorflex",
    "preco": 45.50,
    "fornecedor_ids": ["f04"] # Ele so entrga para o fornecedor x
    },
    {
    "_id": "p21",
    "descricao": "Nimesulida",
    "preco": 14,
    "fornecedor_ids": ["f04", "f07"] # Ele entrga para o fornecedor x e y
    }, 
    {
    "_id": "p47",
    "descricao": "Trembolona",
    "preco": 127.46,
    "fornecedor_ids": ["f07"] # Ele so entrga para o fornecedor y
}]

    collection.insert_many(query)
    res = collection.find({})
    for i in res:
        print(i)

if __name__ == "__main__":
    print("Isto é um exemplo de um para muitos (n - n). Tanto produtos quanto fornecedores tem sua informação propria e usam uma lista dentro de si para identificar quem é o fornecedor e de onde vem o produto com os codigos ids, sem precisar especificar quais as descrições, preco, etc. Assim, não gerando duplicidade e apenas indicando de onde vem.")
    insercao_n_para_n_exemplo()