Primeiro, instale o Gunicorn usando o pip:

pip install gunicorn


Agora, você pode iniciar o servidor Gunicorn apontando-o para o seu aplicativo Flask. Abra um terminal e navegue até o diretório onde seu arquivo app.py está localizado. Em seguida, execute o seguinte comando:


gunicorn -w 4 -b 0.0.0.0:8000 app:app
