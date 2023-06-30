from flask import render_template, request, redirect, url_for
from src.models.UsersModel import User, db
from werkzeug.security import check_password_hash

def index():
    return render_template('index.html')

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(user_email=email).count() > 0:
            user = db.one_or_404(db.select(User).filter_by(user_email = email))
            if check_password_hash(user.user_password, password):
                return "senha correta"
            else:
                return "senha incorreta"
            # redirect(url_for('app_routes.login'))
        # TO DO SEGURANCA DE LOGIN
        return "Ainda não é possível fazer login"
    return render_template('login.html')