from pymongo import MongoClient

def connection():
    try:
        URI = 'mongodb://172.17.0.1:27017'
        client = MongoClient(URI)
        db = client['auth2fa']  
        print("Conexão bem-sucedida ao MongoDB")
        return db
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {str(e)}")
        return None

