# Проект api  на opendata.mkrf.ru 

### API на справочник кинотеатров с возможностью поиска Кинотеатров по адресу или по названию

[Тестовое задание](https://disk.yandex.ru/d/9oQRbCKkon2h4A)

<br>

## Оглавление:
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Описание работы](#описание-работы)
- [Удаление](#удаление)
- [Автор](#автор)

<br>

## Технологии:

<details><summary>Подробнее</summary>

**Языки программирования, библиотеки и модули:**

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)

**Фреймворк, расширения и библиотеки:**

[![Django](https://img.shields.io/badge/Django-v5.1.0-blue?logo=Django)](https://www.djangoproject.com/)


**Базы данных и инструменты работы с БД:**

[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?logo=SQLite)](https://www.sqlite.com/version3.html)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)



**CI/CD:**

[![docker_hub](https://img.shields.io/badge/-Docker_Hub-464646?logo=docker)](https://hub.docker.com/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?logo=gunicorn)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?logo=NGINX)](https://nginx.org/ru/)

[⬆️Оглавление](#оглавление)
</details>

<br>

## Установка и запуск:

<details><summary>Предварительные условия</summary>

Предполагается, что пользователь:
 - установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине или на удаленном сервере, где проект будет запускаться в контейнерах. Проверить наличие можно выполнив команды:
    ```bash
    docker --version && docker-compose --version
    ```
<h1></h1>
</details>

<details><summary>Локальный запуск</summary> 


1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны в evn_example для примера, но их можно оставить):
```bash
git clone https://github.com/sapov/minCultTest.git && \
cd minCultTest && \
cp env_example .env && \
nano .env
```
<details><summary>Локальный запуск: Django/SQLite3</summary>

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```

4. Выполните миграции, загрузку данных, создание суперюзера и запустите приложение:
```bash
python tree_menu/manage.py makemigrations && \
python tree_menu/manage.py migrate && \
python tree_menu/manage.py load_data && \
python tree_menu/manage.py createsuperuser && \
python tree_menu/manage.py runserver
```
Сервер запустится локально по адресу `http://127.0.0.1:8000/`

5. Остановить приложение можно комбинацией клавиш Ctl-C.
<h1></h1>
 </details>

<details><summary>Локальный запуск: Docker Compose/PostgreSQL</summary>

2. Из корневой директории проекта выполните команду:
```bash
docker compose up
```
Проект будет развернут в трех docker-контейнерах (postgres_db, django_project, nginx) по адресу `http://localhost`.

3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
docker compose down
```
Если также необходимо удалить тома базы данных, статики и медиа:
```bash
docker compose down -v
```

</details><h1></h1></details>

<details><summary>Запуск на удаленном сервере</summary>

1. Сделайте [форк](https://docs.github.com/en/get-started/quickstart/fork-a-repo) в свой репозиторий.

2. Создайте `Actions.Secrets` согласно списку ниже (значения указаны для примера) + переменные окружения из env_example файла:
```py
PROJECT_NAME
SECRET_KEY

POSTGRES_PASSWORD
DATABASE_URL

CODECOV_TOKEN

DOCKERHUB_USERNAME
DOCKERHUB_PASSWORD

# Данные удаленного сервера и ssh-подключения:
HOST  # публичный IP-адрес вашего удаленного сервера
USERNAME
SSH_KEY  
PASSPHRASE



```

3. Запустите вручную `workflow`, чтобы автоматически развернуть проект в трех docker-контейнерах (db, web, nginx) на удаленном сервере.
</details><h1></h1>

При первом запуске будут автоматически произведены следующие действия:
  - выполнены миграции БД
  - БД заполнена начальными данными
  - собрана статика
  - для создания суперюзера (пользователь с правами админа) нужно зайти в работающий докер:
```bash
docker exec -it <имя докера> /bin/bash/
``` 
и выполнить команду
```bash
python manage.py createsuperuser
```
выйти из контейнера
```bash
exit
```

 


Вход в админ-зону осуществляется по адресу (в зависимости от способа запуска):
  - http://127.0.0.1:8000/admin/
  - http://localhost/admin/
  - `http://<IP-адрес удаленного сервера>/admin/`

[⬆️Оглавление](#оглавление)

<br>

## Описание работы:

На странице `http://<hostname>/swagger/` представлена документация об эндпоинтах.

  - http://127.0.0.1:8000/api/v1/cinema/ - посмотреть все возможные кинотеатры методом GET
  - http://127.0.0.1:8000/api/v1/cinema/search_address/ - поиск кинотеатров по адресу например (г. Воронеж) нужно передать запрос методом POST вида {"address": "г.Воронеж"} 
  - http://127.0.0.1:8000/api/v1/cinema/search_name/ - поиск кинотеатров по имени например (Комсомолец) нужно передать запрос методом POST вида {"name": "Комсомолец"}
  - http://127.0.0.1:8000/api/v1/cinema/1/ - получение первой записи с возможностью читать, заменять, изменять и удалять запись методами GET, PUT, PATCH, DELETE 



[⬆️Оглавление](#оглавление)

<br>

## Удаление:
Для удаления проекта выполните следующие действия:
```bash
cd .. && rm -fr Django && deactivate
```
Удаление volume базы данных
```bash
sudo rm -f -r .pg/
```
  
[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Sapov Alexander](https://github.com/sapov)

[⬆️В начало](#Проект)