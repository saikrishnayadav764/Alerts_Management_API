from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Post request to register User
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Checking if username already exists
    if User.find_by_username(data['username']):
        return jsonify({"message": "Username already exists"}), 400

    hashed_password = generate_password_hash(data['password'], method='pbkdf2', salt_length=16)
    new_user = User(username=data['username'], password=hashed_password, email=data['email'])
    new_user.save()

    return jsonify({"message": "User registered successfully"}), 201

# Post request to login User
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.find_by_username(data['username'])

    if user and check_password_hash(user['password'], data['password']):
        access_token = create_access_token(identity=user['username'])
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Get request to get User existence
@auth_bp.route('/user', methods=['GET'])
@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    user = User.find_by_username(current_user)
    
    if user:
        return jsonify({"username": user['username']}), 200
    else:
        return jsonify({"message": "User not found"}), 404
