# El código de Act_1_ruta calcula la ruta de menos costo de una matriz
# Docker Proxy
``` Batchfile
PS C:\Users\kiovahn> docker run --name dockerproxy -d -p 8080:80 nginx
```
image
``` Batchfile
PS C:\Users\kiovahn> docker ps -a
CONTAINER ID   IMAGE                                    COMMAND                  CREATED          STATUS                    PORTS                  NAMES
04da54428248   nginx                                    "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes             0.0.0.0:8080->80/tcp   dockerproxy
```
``` Batchfile
PS C:\Users\kiovahn> docker exec -it 04da54428248 bash
root@04da54428248:/# adduser fire
```
Después de teclear el password, podemos darle enter a lo demás, sin rellenar la información.
``` Batchfile
root@04da54428248:/# apt update
root@04da54428248:/# apt install -y python3.11
root@04da54428248:/# apt install -y python3.11-venv
root@04da54428248:/# apt install -y python3-pip
root@04da54428248:/# apt install -y vim
root@04da54428248:/# su fire
fire@04da54428248:/$ cd home
fire@04da54428248:/home$ ls
fire
fire@04da54428248:/home$ cd fire/
fire@04da54428248:~$ python3 -m venv firesenv
fire@04da54428248:~$ source firesenv/bin/activate
(firesenv) fire@04da54428248:~$ vim test.py
```
``` python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola soy fire</p>"
```
ESC
:wq (write, quit)
``` Batchfile
(firesenv) fire@04da54428248:~$ pip install flask
(firesenv) fire@04da54428248:~$ deactivate
fire@04da54428248:~$ exit
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
``` Batchfile
root@04da54428248:/etc/nginx/conf.d# su fire
fire@04da54428248:/etc/nginx/conf.d$ cd /
fire@04da54428248:/$ cd home
fire@04da54428248:/home$ cd fire
fire@04da54428248:~$ source firesenv/bin/activate
(firesenv) fire@04da54428248:~$ vim test.py
```
 I para modo INSERT
image
``` python
from flask import Flask

app = Flask(__name__)

@app.route("/webpage")
def hello_world():
    return "<p>Hola soy fire</p>"
```
ESC
:wq (write, quit)

``` Batchfile
(firesenv) fire@04da54428248:~$ deactivate
fire@04da54428248:~$ exit
root@04da54428248:/# nginx -s reload
root@04da54428248:/# su fire
fire@04da54428248:/$ cd home/fire/
fire@04da54428248:~$ source firesenv/bin/activate
```
image
``` Batchfile
(firesenv) fire@04da54428248:~$ flask --app test run
```
image













