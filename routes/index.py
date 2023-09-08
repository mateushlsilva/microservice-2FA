from __main__ import app

from flask import jsonify
from models import connection
from blueprint.email import email
from models import getAuth

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

@app.route('/auth2fa_email/<emailUser>', methods=["GET", "POST"])
def enviarEmail(emailUser):
    resultado = None
    

    e = email(emailUser)
    if e == True:
        return 'Email enviado!', 200
    if e == False:
        resultado = 'Verfique se os campos foram colocados com informações corretas!'
    else:
        resultado = 'Verfique se os campos foram colocados com informações corretas!'
    return resultado

@app.route('/auth2fa/getEmail/<email>/<cod>')
def getCod2FA(email, cod):
    return jsonify(getAuth(email, 'email', cod)) # Vai retornar null se não encontrar 