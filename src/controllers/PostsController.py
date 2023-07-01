from flask import render_template, request
from flask_login import login_required, current_user
import os, random
import boto3
from src.models.PostsModel import Post, db

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
        print(fileextension)
        if fileextension in ALLOWED_EXTENSIONS:
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

def read():
    return "metodo de leitura e exibicao dos dados"

def update():
    return "metodo de atualizacao dos dados"

def delete():
    return "metodo de delete dos dados"