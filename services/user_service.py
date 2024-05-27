import re
from models.user_model import User
from data_access.user_repository import UserRepository
from werkzeug.security import check_password_hash
from flask import jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token, decode_token


class UserService:
    def __init__(self):
        self._user_repository = UserRepository()

    def get_user_by_email(self, email):
        user = self._user_repository.get_user_by_email(email)
        if user is None:
            return None
        return user.to_dict()


    def signup(self, email, password):
        try:
            if not email:
                return {'message': 'Email is required.'}, 400
            self.validate_email(email)
            self.validate_password(password)

            existing_user = self._user_repository.get_user_by_email(email)
            if existing_user is not None:
                return {'message': 'A user with this email already exists.'}, 400

            hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            user = User(email=email, password=hashed_password)
            self._user_repository.save_user(user)
            return self.generate_token(identity=email), 200
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}, 500
    

    def signin(self, email, password):
        try:
            if not email:
                return {'message': 'Email is required.'}, 400
            self.validate_email(email)
            self.validate_password(password)

            existing_user = self._user_repository.get_user_by_email(email)
            if existing_user is None:
                return {'message': 'A user with this email does not exist.'}, 400

            if not check_password_hash(existing_user.get_password(), password):
                return {'message': 'Invalid password.'}, 400

            return {'message': 'Signed in successfully.','user_id': existing_user.get_id(), 'token': self.generate_token(identity=email)}, 200
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}, 500
    

    def delete_user(self, user):
        try:
            db_user = self._user_repository.get_user_by_email(user.get_email())
            if not db_user:
                return {'message': 'User not found'}, 404
            print("user found")
            print(db_user.id)
            if check_password_hash(db_user.get_password(), user.get_password()):
                try:
                    print("Deleting user")
                    self._user_repository.delete_user(db_user)
                    return {'message': 'User deleted successfully'}, 200
                except Exception as e:
                    return {'error': 'An error occurred: ' + str(e)}, 500
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}, 500
        
    def update_user(self, user):
        try:
            db_user = self._user_repository.get_user_by_email(user.get_email())
            if not db_user:
                return {'message': 'User not found'}, 404
            if check_password_hash(db_user.get_password(), user.get_password()):
                try:
                    self._user_repository.update_user(user)
                    return {'message': 'User updated successfully'}, 200
                except Exception as e:
                    return {'error': 'An error occurred: ' + str(e)}, 500
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}, 500
        

    def get_user_by_id(self, id):
        user = self._user_repository.get_user_by_id(id)
        if user is None:
            return None
        return user.get_email()


    def validate_email(self, email):
        if not email:
            raise ValueError("Email cannot be empty")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")

    def validate_password(self, password):
        if not password:
            raise ValueError("Password cannot be empty")
        if len(password) < 5:
            raise ValueError("Password must be at least 5 characters long")
        if not re.search(r"\d", password):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"[!@#$%^&*()\-_=+{};:,<.>]", password):
            raise ValueError("Password must contain at least one special character")

    
    def generate_token(self, identity):
        token = create_access_token(identity=identity)
        return token


    def decode_token(self, token):
        try:
            decoded_token = decode_token(token)
            return decoded_token
        except Exception as e:
            # Handle invalid token error
            return None