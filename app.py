from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash,generate_password_hash
from flask import session
from models.context import Session
from models.usuario import Usuario, create_user
import json
from services.alchemy_encoder import AlchemyEncoder
from models.context import init_db
from models.libros import Libro
from typing import Dict, List

init_db()

app = Flask(__name__)
app.secret_key = 'mysecretkey'



def is_anonymous_authorized_pages(endpoint):
	return (endpoint == 'incio' \
       or endpoint == 'auth_login'\
       or endpoint == 'static')

@app.before_request
def auth():
       if is_anonymous_authorized_pages(request.endpoint) == False:
             if 'username' not in session:
                    return render_template("index.html"), 403
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


@app.route('/addbook', methods=['POST'])
def add_book():
    parameters = request.form
    if('titulo' in parameters and 'autor' in parameters and 'unidades' in parameters and 'ubicacion' in parameters and 'editorial' in parameters and 'año' in parameters):
        with Session() as db_context:
            # Verificar si el título ya existe
            existing_book = db_context.query(Libro).filter_by(titulo=parameters['titulo']).first()
            if existing_book:
                return "El libro ya existe", 400
            # Si el título no existe, agregar el libro a la base de datos
            book = Libro()
            book.titulo = f"{parameters['titulo']} - {parameters['editorial']} - {parameters['año']}"
            book.autor = parameters['autor']
            book.año = parameters['año']
            book.editorial = parameters['editorial']
            book.unidades = parameters['unidades']
            book.ubicacion = parameters['ubicacion']
            db_context.add(book)
            db_context.commit()
            return json.dumps(book, cls=AlchemyEncoder), 200
    return "Solicitud incorrecta", 400


# @app.route('/addbook', methods=['POST'])
# def add_book():
#     parameters = request.form
#     if('titulo' in parameters and 'autor'  in parameters and 'unidades' in parameters and 'ubicacion' in parameters):
#         with Session() as db_context:
#             # Verificar si el título ya existe
#             existing_book = db_context.query(Libro).filter_by(titulo=parameters['titulo']).first()
#             if existing_book:
#                 return "El libro ya existe", 400
#             # Si el título no existe, agregar el libro a la base de datos
#             book = Libro()
#             book.titulo = parameters['titulo']
#             book.autor = parameters['autor']
#             book.año = parameters['año']
#             book.editorial = parameters['editorial']
#             book.unidades = parameters['unidades']
#             book.ubicacion = parameters['ubicacion']
#             db_context.add(book)
#             db_context.commit()
#             return json.dumps(book, cls=AlchemyEncoder), 200
#     return "Bad request : 400", 400


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



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

@app.route('/agregarunidades', methods=['POST'])
def agregar_unidades():
    parameters = request.form
    if('id' in parameters and 'unidades' in parameters):
        with Session() as db_context:
            book = db_context.query(Libro).filter(Libro.id == parameters['id']).one_or_none()
            if book:
                book.unidades = book.unidades + int(parameters['unidades'])
                db_context.commit()
                return json.dumps(book, cls=AlchemyEncoder), 200
            else:
                return "NOK", 400
    return "Bad request : 400", 400

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/libros', methods=['GET'])
def libros():
     with Session() as db_context:
        libros = db_context.query(Libro).all()
        return render_template('libros.html', libros=libros)




if __name__ == '__main__':
    app.run(debug=True)

# modificaciones python
# nuevo archivo