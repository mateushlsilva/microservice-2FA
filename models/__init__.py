from pymongo import MongoClient

def connection():
    try:
        URI = 'mongodb://localhost:27017'
        client = MongoClient(URI)
        db = client['auth']  
        print("Conexão bem-sucedida ao MongoDB")
        return db
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {str(e)}")
        return None

def insert2FAEmail(email, cod2FA):
    try:
        db = connection()

        newInsert = {
            "email" : f"{email}",
            "cod2FA" : f"{cod2FA}",
        }

        db.auth.insert_one(newInsert)
    except Exception as e:
        return False
    return True