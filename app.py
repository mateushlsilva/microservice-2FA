from flask import Flask
from models import connection
from dotenv import load_dotenv
from blueprint.generate2FA import generate
load_dotenv()

app = Flask(__name__)

import routes.index 



if __name__ == "__main__":
    connection()
    app.run(debug=True)

