# El código de Act_1_ruta calcula la ruta de menos costo de una matriz
# Docker Proxy
Crea y corre un nuevo contenedor
``` Batchfile
PS C:\Users\kiovahn> docker run --name dockerproxy -d -p 8080:80 nginx
```
Comprobar que nginx está corriendo en [127.0.0.1:8080](http://127.0.0.1:8080)
![Screenshot 2024-09-11 235122](https://github.com/user-attachments/assets/c27f9e4e-1751-41ce-aca4-c582c283e1cb)

Consulta de las imagenes de docker
``` Batchfile
PS C:\Users\kiovahn> docker ps -a
CONTAINER ID   IMAGE                                    COMMAND                  CREATED          STATUS                    PORTS                  NAMES
04da54428248   nginx                                    "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes             0.0.0.0:8080->80/tcp   dockerproxy
```
Se copia el ID de la imagen
``` Batchfile
PS C:\Users\kiovahn> docker exec -it 04da54428248 bash
```
Agregar usuario. Después de teclear el password, podemos darle enter a lo demás, sin rellenar la información.
``` Batchfile
root@04da54428248:/# adduser fire
```
Correr apt update. Instalar python, python-venv, python-pip, vim
``` Batchfile
root@04da54428248:/# apt update
root@04da54428248:/# apt install -y python3.11
root@04da54428248:/# apt install -y python3.11-venv
root@04da54428248:/# apt install -y python3-pip
root@04da54428248:/# apt install -y vim
```
Entrar al usuario, navegar a home/username, crear venv y activarlo
``` Batchfile
root@04da54428248:/# su fire
fire@04da54428248:/$ cd home
fire@04da54428248:/home$ ls
fire
fire@04da54428248:/home$ cd fire/
fire@04da54428248:~$ python3 -m venv firesenv
fire@04da54428248:~$ source firesenv/bin/activate
```
Crear test.py
``` Batchfile
(firesenv) fire@04da54428248:~$ vim test.py
```
Agregar el sig. codigo de python
``` python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola soy fire</p>"
```
> [!NOTE]
> ESC (salir de modo INSERT), :wq (write, quit)

Instalar flask, desactivar venv, salir de usuario
``` Batchfile
(firesenv) fire@04da54428248:~$ pip install flask
(firesenv) fire@04da54428248:~$ deactivate
fire@04da54428248:~$ exit
```
Navegar al directorio mostrado y editar default.conf con vim
``` Batchfile
root@04da54428248:/# cd /
root@04da54428248:/# cd etc/nginx/conf.d/
root@04da54428248:/etc/nginx/conf.d# ls
default.conf
root@04da54428248:/etc/nginx/conf.d# vim default.conf
```
> [!NOTE]
> I (modo INSERT)

Agregamos un nuevo location (cuadro morado)

![Screenshot 2024-09-12 012020](https://github.com/user-attachments/assets/dbbf5b67-f00a-4d3e-900a-6ca15dca6564)

> [!NOTE]
> ESC (salir de modo INSERT), :wq (write, quit)

Entrar al usuario, navegar al directorio mostrado, activar venv y editar el archivo creado anteriormente
``` Batchfile
root@04da54428248:/etc/nginx/conf.d# su fire
fire@04da54428248:/etc/nginx/conf.d$ cd /
fire@04da54428248:/$ cd home
fire@04da54428248:/home$ cd fire
fire@04da54428248:~$ source firesenv/bin/activate
(firesenv) fire@04da54428248:~$ vim test.py
```
> [!NOTE]
> I (modo INSERT)

Agregar _webpage_ dentro de los ()
``` python
from flask import Flask

app = Flask(__name__)

@app.route("/webpage")
def hello_world():
    return "<p>Hola soy fire</p>"
```
> [!NOTE]
> ESC (salir de modo insert), :wq (write, quit)

Desactivar venv y salir de usuario. Recargar nginx. Entrar a usuario, activar venv
``` Batchfile
(firesenv) fire@04da54428248:~$ deactivate
fire@04da54428248:~$ exit
root@04da54428248:/# nginx -s reload
root@04da54428248:/# su fire
fire@04da54428248:/$ cd home/fire/
fire@04da54428248:~$ source firesenv/bin/activate
```
Correr el archivo test con flask
``` Batchfile
(firesenv) fire@04da54428248:~$ flask --app test run
```
![Screenshot 2024-09-12 013256](https://github.com/user-attachments/assets/f99e21a8-5bc3-4eeb-8068-8ca7ff0dde73)

# Sesiones
En seguimiento a la práctica de docker proxy, ahora probaremos el funcionamiento de sesiones en flask, basado en https://flask.palletsprojects.com/en/3.0.x/quickstart/#sessions

kiovahn@Kiovahns--MacBook-Air ~ % docker exec -it dockerproxy bash
```Batchfile
root@d832bc1a087a:/# cd home/fire
root@d832bc1a087a:/home/fire# source firesenv/bin/activate
(firesenv) root@d832bc1a087a:/home/fire# vim test.py
```
Reemplazar el codigo python anterior con este:
```python
from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)

@app.route("/webpage")
def hello_world():
    return "<p>Hola soy fire</p>"

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
```

Abrir otra terminal y entrar al contenedor con

```Batchfile
kiovahn@Kiovahns--MacBook-Air ~ % docker exec -it dockerproxy bash
```
```Batchfile
root@d832bc1a087a:/# cd etc/nginx/conf.d
root@d832bc1a087a:/etc/nginx/conf.d# vim default.conf
```

Agregar las sig. líneas:

<img width="830" alt="Screenshot 2024-10-16 at 4 24 53 PM" src="https://github.com/user-attachments/assets/1487bdeb-bdb7-4baf-b2da-7b964b50263a">

Salir del contenedor de docker con el comando exit

kiovahn@Kiovahns--MacBook-Air ~ % docker restart dockerproxy

Regresar a la primer terminal y correr 

```Batchfile
(firesenv) root@d832bc1a087a:/home/fire# flask --app test run
```

<img width="751" alt="Screenshot 2024-10-16 at 4 30 29 PM" src="https://github.com/user-attachments/assets/888b358f-2a4d-496c-923d-b61dd5bfd67d">













