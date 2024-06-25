from flask import Blueprint, render_template, current_app
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Define the blueprint
relocator_blueprint = Blueprint('relocator', __name__, template_folder='templates')

# Read environment variables
new_location = os.getenv('NEW_LOCATION')

@relocator_blueprint.route('/', defaults={'path': ''})
@relocator_blueprint.route('/<path:path>')
def index(path):
    if new_location:
        message = f"Server is migrated to <a href='{new_location}'>{new_location}</a>"
    else:
        message = "The server is migrated somewhere else and is no longer here..."
    return render_template('index.html', message=message)
