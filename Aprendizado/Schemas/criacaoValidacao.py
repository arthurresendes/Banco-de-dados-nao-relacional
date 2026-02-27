from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
cliente = MongoClient(os.getenv("MONGO_URI"))


db = cliente["automoveis"]

validator_cars = {
    '$jsonSchema': {
        'bsonType': "object",  # documento é um objeto
        'required': ['model','madeBy' ,'year'], # requiridos obrigatorios
        'properties': {
            'model': {
                'bsonType': "string",
                'description': 'O modelo deve ser uma string'
            },
            'madeBy': {
                'bsonType': "string",
                'minLength': 3,
                'description': 'Feito por quem deve ser uma string'
            },
            'year': {
                'bsonType': "int",
                'minimum': 1900,
                'maximum': 2026,
                'description': 'O ano deve ser um inteiro'
            },
        }
    }
}

try:
    db.create_collection('cars', validator=validator_cars)
    print("Coleção 'cars' criada com validação!")
    query = {'model': 'Fiesta', 'madeBy': 'Ford', 'year': '2015'}
    try:
        cars = db['cars']
        cars.insert_one(query)
        res = cars.find()
        for i in res:
            print(i)
    except:
        print("Erro na digitação, verifique os campos")
except Exception as e:
    print(f"{e}")
    db.command({
        "collMod": "cars",
        "validator": validator_cars,
        "validationLevel": "strict",    
        "validationAction": "error"
    })

    print("Validação aplicada com sucesso!")

