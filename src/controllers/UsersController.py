from flask import render_template, request
from src.models.UsersModel import User, db

def create():
    # VERIFICA SE VISITANTE VEIO DE UM FORMULARIO "POST"
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname =  request.form['lastname']
        email = request.form['email']
        account = request.form['account']
        password = request.form['password']
        user = User(user_firstname = firstname,
            user_lastname = lastname,
            user_email = email,
            user_account = account,
            user_password = password,
            user_is_active = 1,
            user_is_delete = 0
        )
        db.session.add(user)
        # commit é o comando q confirma a persistencia
        db.session.commit()
        # rollback é o comando q cancela 
        return "Usuário criado com sucesso"
    
    return render_template('users/create.html')

def read():
    return "metodo de leitura e exibicao dos dados"

def update():
    return "metodo de atualizacao dos dados"

def delete():
    return "metodo de delete dos dados"