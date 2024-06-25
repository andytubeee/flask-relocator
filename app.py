from flask import Flask
from relocator.relocator import relocator_blueprint 
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.register_blueprint(relocator_blueprint, url_prefix='/') 

if __name__ == '__main__':
    app.run(debug=True, port = os.getenv('PORT', 8001))
