from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
import os, random
import boto3
from src.models.PostsModel import Post, db
from src.models.UsersModel import User

def upload_file(filename, bucket):
    
    objectname = filename
    s3client = boto3.client('s3')
    response = s3client.upload_file(filename, bucket, objectname)
    os.remove(filename)

    return response


@login_required
def create():
    # CONFIGURAÇÕES DE UPLOAD
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg','gif'}
    BUCKET = 'professorphotoblog'
    # VERIFICA SE VISITANTE VEIO DE UM FORMULARIO "POST"
    if request.method == 'POST':
        description = request.form['description']
        file =  request.files['file']
        # variavel filename recebe apenas o nome do arquivo e a extensao fica com fileext...
        filename, fileextension = os.path.splitext(file.filename)
        fileextension = fileextension.replace(".","")

        if fileextension.lower() in ALLOWED_EXTENSIONS:
            filename = current_user.user_account+str(random.randrange(1,999999999))+'.'+fileextension
            file.save(file.filename)
            os.rename(file.filename,filename)
            upload_file(f"{filename}", BUCKET)
            post = Post(user_id = current_user.id,
                        post_description=description,
                        post_mediatype=fileextension,
                        post_mediapath="https://professorphotoblog.s3.us-east-2.amazonaws.com/",
                        post_filename=filename
                        )
            db.session.add(post)
            db.session.commit()
            return "Post criado"
    
    return render_template('posts/create.html')

def read(useraccount, postid):
    if User.query.filter_by(user_account=useraccount).count() == 0 or Post.query.filter_by(id=postid).count() == 0:
        # TO DO
        # Retornar mensagem que a conta(pagina) ou postagem não foi encontrada e redirecionar
        return "Conta ou post não existe."
    else:
        user = db.one_or_404(db.select(User).filter_by(user_account=useraccount))
        post = db.one_or_404(db.select(Post).filter_by(id=postid))
        return render_template('posts/read.html',
                               user = user,
                               post = post,
                               currentuser = current_user)

@login_required
def update(useraccount, postid):
    if User.query.filter_by(user_account=useraccount).count() == 0 or Post.query.filter_by(id=postid).count() == 0:
        # TO DO
        # Retornar mensagem que a conta(pagina) ou postagem não foi encontrada e redirecionar
        return "Conta ou post não existe."
    else:
        if request.method == 'POST':
            if current_user.user_account == useraccount:
                post = db.one_or_404(db.select(Post).filter_by(id=postid))
                post.post_description = request.form['postdescription']
                db.session.commit()
                return redirect(url_for('app_routes.profile',useraccount= useraccount))
            else:
                # TO DO
                # Retornar mensagem que a conta(pagina) ou postagem não foi encontrada e redirecionar
                return "Você não pode apagar um post de outro usuário."
        else:
            user = db.one_or_404(db.select(User).filter_by(user_account=useraccount))
            post = db.one_or_404(db.select(Post).filter_by(id=postid))
            return render_template('posts/update.html',
                                user = user,
                                post = post,
                                currentuser = current_user)
@login_required
def delete(useraccount, postid):
    if User.query.filter_by(user_account=useraccount).count() == 0 or Post.query.filter_by(id=postid).count() == 0:
        # TO DO
        # Retornar mensagem que a conta(pagina) ou postagem não foi encontrada e redirecionar
        return "Conta ou post não existe."
    else:
        if current_user.user_account == useraccount:
            post = db.one_or_404(db.select(Post).filter_by(id=postid))
            db.session.delete(post)
            db.session.commit()
            return redirect(url_for('app_routes.profile',useraccount= useraccount))
        else:
            # TO DO
            # Retornar mensagem que a conta(pagina) ou postagem não foi encontrada e redirecionar
            return "Você não pode apagar um post de outro usuário."
