from flask import Flask

app = Flask(__name__)

import routes.index 
from models.index import connection



if __name__ == "__main__":
    connection()
    app.run(debug=True)

