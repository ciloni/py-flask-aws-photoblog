from flask import render_template, request, redirect, url_for
from src.models.UsersModel import User, db
from src.models.PostsModel import Post
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

def index():
    return render_template('index.html',
                           current_user = current_user,
                           )

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(user_email=email).count() > 0:
            user = db.one_or_404(db.select(User).filter_by(user_email = email))
            if check_password_hash(user.user_password, password):
                login_user(user)
                return redirect(url_for('app_routes.index'))
            else:
                # to do "flash" retornar para  pagagina de login com o erro senha incorreta
                return redirect(url_for('app_routes.login'))
        # email não localizado
        # to do "flash" retornar para  pagagina de login com o erro de email não localizado
        return redirect(url_for('app_routes.login'))

    return render_template('login.html')

@login_required
def logout():
    logout_user()
    return redirect(url_for('app_routes.index'))

def profile(account):
    if User.query.filter_by(user_account=account).count() == 0:
        # TO DO
        # Retornar mensagem que a conta(pagina) não foi encontrada e redirecionar
        return "Conta não existe."
    else:
        user = db.one_or_404(db.select(User).filter_by(user_account=account))
        posts = Post.query.filter_by(user_id=user.id)
        return render_template('profile.html',
                               user = user,
                               posts = posts)