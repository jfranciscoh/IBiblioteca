from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash,generate_password_hash
from flask import session
from models.context import Session
from models.usuario import Usuario, create_user
import json
from services.alchemy_encoder import AlchemyEncoder
from models.context import init_db
from typing import Dict, List

init_db()

app = Flask(__name__)
app.secret_key = 'mysecretkey'

    
@app.route('/')
def incio():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')
        
@app.route('/register', methods=['POST'])
def auth_register():
    parameters = request.form
    if('username' in parameters and 'password' in parameters):
        with Session() as db_context:
            user = db_context.query(Usuario).filter(Usuario.username == parameters['username']).limit(1).one_or_none()
            if not user:
                user = create_user(username=parameters['username'], clear_password=parameters['password'])
                db_context.add(user)
                db_context.commit()
            else:
                return "NOK", 400
            return json.dumps(user, cls=AlchemyEncoder), 200
    return "Bad request : 400", 400


@app.route('/login', methods=['POST'])
def auth_login():
    parameters = request.form
    if('username' in parameters and 'password' in parameters):
        with Session() as db_context:
            user = db_context.query(Usuario).filter(Usuario.username == parameters['username']).one_or_none()
            if user:
                if check_password_hash(user.password, parameters['password']):
                    session['username'] = parameters['username']
                    session['id'] = user.id
                else:
                    return "NOK", 400
                return json.dumps(user, cls=AlchemyEncoder), 200
            else:
                return request.environ.get('HTTP_ORIGIN', 'default value'), 400
    return "Bad request : 400", 400

@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)

# modificaciones python
# nuevo archivo