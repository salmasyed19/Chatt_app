from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import nlp_model

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://user:password@localhost/genz_chat_db'
app.config['JWT_SECRET_KEY'] = 'supersecretkey'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

jwt = JWTManager(app)
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
# Chat Model
class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String(500), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    new_user = User(username=username, password=password, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify(message="Invalid credentials"), 401

@app.route('/chat', methods=['POST'])
@jwt_required()
def send_message():
    sender = request.json.get('sender')
    receiver = request.json.get('receiver')
    message = request.json.get('message')
    # Use NLP for Gen Z language transformation
    message = nlp_model.process_message(message)
    new_chat = Chat(sender_id=sender, receiver_id=receiver, message=message)
    db.session.add(new_chat)
    db.session.commit()
    return jsonify(message="Message sent successfully")

if __name__ == '__main__':
    app.run(debug=True)
