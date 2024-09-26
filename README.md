# fastapi_app - простое приложение для работы с БД с помощью API
 Учебный проект в рамках которого выполняются следующие операции:  
 - Созданы несколько таблиц с помощью  асинхронного движка sqlalchemy  
 - Написаны асинхронные обработчики запросов  
 - Контейнеризация приложения в docker
 - Развертывание на удаленном сервере на базе Ubuntu 22.04
 - для отработки создания простейшего приложения на fastapi выполняющего асинхронные запросы к БД с контейнеризацией в Docker и развертыванием на сервер на базе Ubuntu 22.04.
 
## Локальный запуск на своей машине 
Если не планируете арендовать сервер и хотите просто протестировать локально, то перейдите к шагу [How to test the app](#How-to-test-the-app).  
Для запуска приложения на сервере на Ubuntu выполните шаги, подготовительные шаги описанные в [Подготовка сервера](#Prepare-the-Ubuntu-server)

## Prepare the Ubuntu server  
**Install git:**
```
sudo apt update
sudo apt install git
git --version
```

**Install Docker:**
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce -y sudo systemctl start docker
sudo systemctl enable docker
```

To verify that docker is installed correctly, run `sudo docker run hello-world`.  
This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation message and exits.

## How to test the app
1. Fork the repo from github:

    `git clone https://github.com/alekseykonotop/fastapi_first_app.git`
2. Move to cloned directory: 

    `cd fastapi_first_app`
3. Build and run a docker image:

    `sudo docker build . --tag fastapi_app && docker run -p 80:80 fastapi_app`
4. The app is running, check `127.0.0.0`  with the paths described below in [API specs](#API-specs).
## API specs
Roots  
- Users:  
  - POST '/users' - Add user
  - GET '/users' - find all users
  - GET '/user/{user_id}' - get user data by id
- Tasks:
  - POST '/tasks' - add new task
  - GET '/tasks' - find all tasks

