# El código de Act_1_ruta calcula la ruta de menos costo de una matriz
# Docker Proxy
Crea y corre un nuevo contenedor
``` Batchfile
PS C:\Users\kiovahn> docker run --name dockerproxy -d -p 8080:80 nginx
```
Comprobar que nginx está corriendo en [127.0.0.1:8080](127.0.0.1:8080)
```
image
```
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
ESC
:wq (write, quit)
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
 I para modo INSERT
Agregamos un nuevo location (cuadro morado)
image
ESC
:wq (write, quit)
Entrar al usuario, navegar al directorio mostrado, activar venv y editar el archivo creado anteriormente
``` Batchfile
root@04da54428248:/etc/nginx/conf.d# su fire
fire@04da54428248:/etc/nginx/conf.d$ cd /
fire@04da54428248:/$ cd home
fire@04da54428248:/home$ cd fire
fire@04da54428248:~$ source firesenv/bin/activate
(firesenv) fire@04da54428248:~$ vim test.py
```
 I para modo INSERT
Agregar _webpage_ dentro de los ()
``` python
from flask import Flask

app = Flask(__name__)

@app.route("/webpage")
def hello_world():
    return "<p>Hola soy fire</p>"
```
ESC
:wq (write, quit)
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













