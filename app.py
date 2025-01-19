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

@app.route('/contactus')
def contactus():
    return render_template('01(Contact).html')

@app.route('/products')
def products():
    return render_template('01(products).html')

@app.route('/passwordrecovery')
def passwordrecovery():
    return render_template('02passwordrecovery.html')


@app.route('/passwordreset')
def passwordreset():
    return render_template('03passwordreset.html')

@app.route('/signup')
def signup():
    return render_template('04signup.html')

@app.route('/jobcreate')
def jobcreate():
    return render_template('05jobcreationscreen.html')

@app.route('/jobdraaft')
def jobdraaft():
    return render_template('06jobdraftscreen.html')

@app.route('/jobpub')
def jobpub():
    return render_template('07jobpublishedscreen.html')

@app.route('/jobcat')
def jobcat():
    return render_template('08jobcategoriesmanagement.html')

@app.route('/interviewsche')
def interviewsche():
    return render_template('19InterviewSchedulingDashboard.html')

@app.route('/Dashboard')
def Dashboard():
    return render_template('23DashboradOverviewScreen.html')

@app.route('/custdash')
def custdash():
    return render_template('26CustomereportDashboard.html')

@app.route('/custrepo')
def custrepo():
    return render_template('27customreportscreen.html')

@app.route('/repodetail')
def repodetail():
    return render_template('28Reportdetailscreen.html')

@app.route('/editrepo')
def editrepo():
    return render_template('29Editreportscreen.html')

@app.route('/jobapply')
def jobapply():
    return render_template('30jobapply.html')

@app.route('/clientjob')
def clientjob():
    return render_template('31clientjobpage.html')

@app.route('/resume')
def resume():
    return render_template('32resume.html')

@app.route('/clientdashb')
def clientdashb():
    return render_template('33clientdash.html')










if __name__ == '__main__':
    # Default to port 8080 if PORT is not set in environment variables
    port = int(os.environ.get('PORT', 8080))
    
    # Use Waitress for production-ready serving
    serve(app, host='0.0.0.0', port=port)