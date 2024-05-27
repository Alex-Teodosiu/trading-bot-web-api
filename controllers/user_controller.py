from flask_restx import Namespace, Resource
from flask import request, jsonify
from models.user_model import User  
from services.user_service import UserService  

users = Namespace('users')
user_service = UserService()  

@users.route('/signin')
class SignIn(Resource):
    @users.expect(User)
    def post(self):
        try:
            data = request.json
            result = user_service.signin(data['email'], data['password'])
            if isinstance(result, tuple):  # If a message and status code were returned
                return result
            return {'message': 'Invalid email or password.'}, 401
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}, 500


@users.route('/signup')
class SignUp(Resource):
    @users.expect(User)
    def post(self):
        try:
            data = request.json
            if 'email' not in data or not data['email']:
                return {'message': 'Email is required.'}, 400
            print(data['email'])
            print(data['password'])
            result = user_service.signup(data['email'], data['password'])
            if isinstance(result, tuple):  # If an error message and status code were returned
                return result
            return {'message': 'Signed up successfully.', 'token': result}, 200
        except Exception as e:
            return jsonify({'error': 'An error occurred: ' + str(e)}), 500

    
@users.route('/getuser/<email>')
class GetUser(Resource):
    def get(self, email):
        try:
            user = user_service.get_user_by_email(email)
            if user is not None:
                return user, 200
            return {'message': 'User not found.'}, 404
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}, 500
    

@users.route('/deleteuser')
class DeleteUser(Resource):
    @users.expect(User)
    def delete(self):
        try:
            data = request.json
            user = User(data['email'], data['password'])
            response = user_service.delete_user(user)
            return response if response else {'message': 'User deleted successfully.'}, 200
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}, 500
        

@users.route('/updateuser')
class UpdateUser(Resource):
    @users.expect(User)
    def put(self):
        try:
            data = request.json
            user = User(data['email'], data['password'], data['id'])
            response = user_service.update_user(user)
            return response if response else {'message': 'User updated successfully.'}, 200
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}, 500
        
@users.route('/get-email-by-id/<id>')
class GetEmailById(Resource):
    def get(self, id):
        try:
            email = user_service.get_user_by_id(id)
            if email is not None:
                return email, 200
            return {'message': 'Email not found.'}, 404
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}, 500