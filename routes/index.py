from __main__ import app
from models.index import connection
from blueprint.email import email

@app.route('/')
def index():
    db = connection()
    item_1 = {
        "_id" : "U1IT00001",
        "item_name" : "Blender",
        "max_discount" : "10%",
        "batch_number" : "RR450020FRG",
        "price" : 340,
        "category" : "kitchen appliance"
    }

    item_2 = {
        "_id" : "U1IT00002",
        "item_name" : "Egg",
        "category" : "food",
        "quantity" : 12,
        "price" : 36,
        "item_description" : "brown country eggs"
    }
    db.auth2fa.insert_many([item_1,item_2])
    return "oi"

@app.route('/contribua', methods=["GET", "POST"])
def contribua():
    resultado = None
    
   

    e = email()
    if e == True:
        resultado = 'Email enviado!'
        return resultado
    if e == False:
        resultado = 'Verfique se os campos foram colocados com informações corretas!'
    else:
        resultado = 'Verfique se os campos foram colocados com informações corretas!'
    return resultado

