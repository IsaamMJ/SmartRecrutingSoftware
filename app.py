import os
from flask import Flask, render_template
from dotenv import load_dotenv
from flask_cors import CORS
from waitress import serve  # Production-ready WSGI server

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)
CORS(app)

# Configure FLASK_DEBUG from the environment variable (default: False)
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', '0') == '1'

# Define a route for the homepage
@app.route('/')
def home():
    return render_template('01loginpage.html')  # Render the HTML template

@app.route('/aboutus')
def aboutus():
    return render_template('01(Aboutus).html')

if __name__ == '__main__':
    # Default to port 8080 if PORT is not set in environment variables
    port = int(os.environ.get('PORT', 8080))
    
    # Use Waitress for production-ready serving
    serve(app, host='0.0.0.0', port=port)