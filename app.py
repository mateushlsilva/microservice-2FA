from flask import Flask
from models.index import connection
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

import routes.index 



if __name__ == "__main__":
    connection()
    app.run(debug=True)

