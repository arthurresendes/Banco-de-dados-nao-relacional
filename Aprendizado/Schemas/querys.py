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

db.create_collection("cars", validator=validator_cars)

