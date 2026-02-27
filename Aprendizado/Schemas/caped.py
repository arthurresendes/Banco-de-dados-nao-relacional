from pymongo import MongoClient

# 1. Conectar ao MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['capedLogs']

# 2. Definir nome da coleção
collection_name = 'logs_aplicacao'

# 3. Remover se já existir para rodar o exemplo novamente
if collection_name in db.list_collection_names():
    db.drop_collection(collection_name)

# 4. Criar a Capped Collection explicitamente
# capped=True: Ativa a funcionalidade
# size: Tamanho máximo em bytes (Obrigatório)
# max: Número máximo de documentos (Opcional)
db.create_collection(
    collection_name, 
    capped=True, 
    size=5242880, # 5MB
    max=10000     # 10 mil documentos
)

capped_collection = db[collection_name]

# 5. Inserir dados para testar
for i in range(10005):
    capped_collection.insert_one({
        "log": f"Log de evento número {i}",
        "status": "info",
        "timestamp": i
    })

# 6. Verificar
count = capped_collection.count_documents({})
print(f"Número de documentos na collection: {count}") # Saída será 10000

# Mostrar o último documento inserido
print(capped_collection.find_one(sort=[('$natural', -1)]))
