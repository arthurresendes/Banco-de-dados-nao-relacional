from pymongo import MongoClient,ASCENDING
from dotenv import load_dotenv
import os

load_dotenv()
cliente = MongoClient(os.getenv("MONGO_URI"))


db = cliente["pokemon_center"]
collection  = db["pokemon"]
collection_fight = db["fight"]

def lendarios_count():
    queryLendario = {"legendary": {"$eq": True}}
    res = collection.find(queryLendario)
    contagem = collection.count_documents(queryLendario)
    for i in res:
        print(i)
    return f"Total: {contagem}"

def distinct_generations():
    return collection.distinct("generation")

# i = Sem case sensitive(ignore case), m = modo multilinhas
def name_wih_regex(name):
    query = {"name": {"$regex": name, "$options": "i"}}
    res = collection.find(query, {"_id": False,"name": True, "types": 1,"legendary": True})
    
    for i in res:
        print(i)

def pokemon_with_max_power():
    res = collection.find({}).sort("attack",-1).limit(5)
    for i in res:
        print(i) 


def search_type_in_arrays(tipo):
    query = {"types": tipo}
    res = collection.find(query)
    for i in res:
        print(i)

def search_two_type_in_arrays(tipo1,tipo2):
    query = {"types": {"$in": [tipo1,tipo2]}}
    res = collection.find(query)
    for i in res:
        print(i)

def searche_fire_or_aqua():
    query = {"$or": [
        {"types": {"$regex": "fire", "$options": "i"}},
        {"types": {"$regex": "water", "$options": "i"}}
    ]}
    res = collection.find(query)
    for i in res:
        print(i)

def sort_pokemons():
    res = collection.find({}).sort("name",1)
    for i in res:
        print(i)

def search_pokemon_with_two_types():
    query = {"types": {"$size": 2}}
    res = collection.find(query)
    for i in res:
        print(i)

def search_pokemon_exectaly_with_two_types():
    query = {"types": {"$all": ["Fire", "Water"]}}
    res = collection.find(query)
    for i in res:
        print(i)


def limit_five_max_powerfull_pokemons():
    res = collection.find({}).sort("attack", -1).limit(5)
    for i in res:
        print(i)


def skip():
    page = 3
    itens = 10
    res = collection.find({}).sort("name", 1).skip(page).limit(itens)
    for i in res:
        print(i)

def update_one_legendary():
    antigo = {'legendary': False}
    novo = {'$set': {'legendary': True}}
    collection.update_one(antigo,novo)
    return "Atualizado"

def update_inc():
    antigo = {'hp': 39}
    novo = {'$inc': {'hp': 50, 'speed': -20}}
    collection.update_one(antigo,novo)
    return "Atualizado"

def update_mul():
    antigo = {'defense': 30}
    novo = {'$mul': {'defense': 1.15}}
    collection.update_one(antigo,novo)
    return "Atualizado defesa"

# Caso não exista cria um novo
def update_upsert():
    antigo = {"name": "Pikachu"}
    novo = {"$set": {"attack": 60}}
    collection.update_one(antigo,novo,upsert=True)
    return "Atualizado ataque do pikachu"

def update_in_current_time():
    antigo = {"name": "Pikachu"}
    novo = {"$set": {"speed": 80},"$currentDate": {"data_envio": True,  "logs.timestamp": {"$type": "timestamp"}}}
    collection.update_one(antigo,novo)
    return "Atualizado velocidade do pikachu"

def update_array():
    antigo = {"name": "Pikachu"}
    novo = {"$push": {"sound": ["Pika-Pi"]}}
    collection.update_one(antigo,novo)
    return "Adicionando som ao pikachu"

def update_array_multiple_sounds():
    antigo = {"name": "Charmander"}
    novo = {"$push": {"sound": {"$each": ["Charmander", "Char-Char"]}}}
    collection.update_one(antigo,novo)
    return "Adicionando varios sons ao Charmander"

def update_array_multiple_sounds_with_position():
    antigo = {"name": "Charmander"}
    novo = {"$push": {"sound": {"$each": ["Char-Char"], "$position": 0}}}
    collection.update_one(antigo,novo)
    return "Adicionando Char-Char ao primeiro som da lista no Charmander"

def update_array_not_duplicates():
    antigo = {"name": "Charmander"}
    novo = {"$addToSet": {"sound": {"$each": ["Char-Char", "CHARMANDERR"]}}} # Only CHARMANDERR is add in mongodb
    collection.update_one(antigo,novo)
    return "Adicionando apenas um som evitando duplicatas"

def update_and_sort_arrays():
    antigo = {"name": "Pikachu"}
    novo = {"$push": {"sound": {"$each": ["Pikachuu"], "$sort": 1}}}
    collection.update_one(antigo,novo)
    return "Adicionando e ordenando o array"

def update_delete_one_sound():
    antigo = {"name": "Charmander"}
    novo = {"$push": {"sound": {"$each": [], "$slice": 2}}} # Mantem os 2 primeiros apos o push
    collection.update_one(antigo,novo)
    return "Mantendo apenas os 2 primeiros sons do Charmander"

def update_pop():
    antigo = {"name": "Charmander"}
    novo = {"$pop": {"sound": 1}}
    collection.update_one(antigo,novo)
    return "Removendo o ultimo som do charmander"

def update_pull():
    antigo = {"name": "Pikachu"}
    novo = {"$pull": {"sound": "Pika-Pi"}}
    collection.update_one(antigo,novo)
    return "Removendo um som especifico do pikachu"

def create_index_in_name():
    name_index = collection.create_index([("name", ASCENDING)])
    return name_index

def create_index_array():
    collection.create_index([("types", 1)]) # 1 ASCENDING, -1 DESCENDING
    return "Criando index para tipos"

def find_in_array_index():
    res = collection.find({"types": "Poison"})
    for i in res:
        print(i)

# Com index as pesquisas ficam mais rapidas
def sort_with_index():
    res = collection.find().sort("name", ASCENDING)
    for i in res:
        print(i)

def analise_explain():
    res = collection.find({"name": "Pikachu"}).sort("type", -1).explain()['executionStats']
    print(f"Tempo de execução (ms): {res['executionTimeMillis']}")
    print(f"Documentos examinados: {res['totalDocsExamined']}")
    print(f"Documentos retornados: {res['nReturned']}")

def drop_index():
    collection.drop_index([("name", ASCENDING)])
    return 'Index excluido'

def see_stats():
    return db.command("dbStats")

def explain_name():
    res = collection.find({"name": "Pikachu"}).explain()
    return res

def explain_speed():
    res = collection.find({"speed":{"$eq": 80}}).explain()
    return res

def only_legendary():
    pipeline = [{"$match": {"legendary": True}}]
    res = collection.aggregate(pipeline)
    for i in res:
        print(i)

def group_pokemon():
    pipeline = [{ "$group": { "_id": None,"total_poderes": { "$sum": {"$add": ["$defense", "$attack", "$speed"]}},"media_poderes": { "$avg": {"$add": ["$defense", "$attack", "$speed"]}}}}]
    res = collection.aggregate(pipeline)
    for i in res:
        print(i)

def join_first_pokemon():
    pipeline = [
        {
            "$lookup": {
                "from": "pokemon", # Tabela que puxa da onde vem os dados
                "localField": "First_pokemon", # Campo da coleção do fight
                "foreignField": "_id", # Campo de comparação
                "as": "pokemon1" # Se chama pokemon1
            }
        }
    ]
    return collection_fight.aggregate(pipeline)

def join_second_pokemon():
    pipeline = [
        {
            "$lookup":{
                "from": "pokemon",
                "localField": "Second_pokemon",
                "foreignField": "_id",
                "as": "pokemon2"
            }
        }
    ]
    
    return collection_fight.aggregate(pipeline)

def join_first_and_two():
    pipeline = [
        {
            "$lookup":{
                "from": "pokemon",
                "localField": "First_pokemon",
                "foreignField": "_id",
                "as": "pokemon1"
            }   
        },
        {
            "$lookup":{
                "from": "pokemon",
                "localField": "Second_pokemon",
                "foreignField": "_id",
                "as": "pokemon2"
            }
        }
    ]
    
    return collection_fight.aggregate(pipeline)

def winner():
    pipeline = [
        {
            "$lookup": { # Join
                "from": "pokemon", # De
                "localField": "First_pokemon", # Nome do campo
                "foreignField": "_id", # Campo que liga
                "as": "pokemon1" # Nome que sera abreviado
            }   
        },
        {
            "$lookup": {
                "from": "pokemon",
                "localField": "Second_pokemon",
                "foreignField": "_id",
                "as": "pokemon2"
            }
        },
        {
            "$project": { # Utilizado para selecionar/remover/transformar campos que passam para proxima etapa, no caso pokemon1 e pokemon2
                "_id": 0, # Remove id
                "Winner": 1, # Mantem o campo Winner
                "pokemon1": { "$arrayElemAt": ["$pokemon1", 0] }, # Pega o array de informações
                "pokemon2": { "$arrayElemAt": ["$pokemon2", 0] }
            }
        },
        {
            "$project": {
                "WinnerName": { # Novo campo
                    "$cond": {
                        "if": { "$eq": ["$Winner", "$pokemon1._id"] }, # Se Winner == pokemon1_id retorna pokemon1.name
                        "then": "$pokemon1.name",
                        "else": "$pokemon2.name" # Se nao traz o nome do pokemon2
                    }
                }
            }
        }
    ]
    
    return collection_fight.aggregate(pipeline)
