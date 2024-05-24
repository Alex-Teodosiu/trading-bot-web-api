from flask import Flask, redirect
from flask_jwt_extended import JWTManager
from flask_restx import Api
from routes import initialize_routes

app = Flask(__name__)
api = Api(app, doc='/')  # Set the documentation to be served at the root URL

app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  

# Initialize JWTManager
jwt = JWTManager(app)

initialize_routes(api)

# Redirect the root URL to /documentation for Swagger UI
@app.route('/')
def index():
    return redirect('/documentation')

if __name__ == '__main__':
    app.run(port=8000)
