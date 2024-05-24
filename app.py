from flask import Flask, redirect
from flask_restx import Api
from routes import initialize_routes

app = Flask(__name__)
api = Api(app, doc='/')  # Set the documentation to be served at the root URL

initialize_routes(api)

# Redirect the root URL to /documentation for Swagger UI
@app.route('/')
def index():
    return redirect('/documentation')

if __name__ == '__main__':
    app.run(port=8000)
