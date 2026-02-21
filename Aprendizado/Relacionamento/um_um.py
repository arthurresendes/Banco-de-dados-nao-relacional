from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
cliente = MongoClient(os.getenv("MONGO_URI"))
db = cliente['Scholl']
collection = db['Alunos']

def insercao_um_para_um_exemplo():
    query = {
        '_id': 'a01',
        'nome': 'Josias',
        'idade': 16,
        'carteirinha': {
            'num_matricula': 123456789,
            'instituicao': 'Josias Academy'
        }
    }
    collection.insert_one(query)
    res = collection.find({})
    for i in res:
        print(i)

if __name__ == "__main__":
    print("Isto é um exemplo de um para um (1 - 1), pois um aluno tem uma carteirinha e a carteirinha depende da existência do aluno, então criamos a carteirinha com suas devidos informações dentro da collection aluno juntamento com as devidas informações de tal.")
    insercao_um_para_um_exemplo()