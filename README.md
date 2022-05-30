## Backend for simple shop/store app

### Technical requirements for Project:

Python 3.9, Django 3.0, PostgreSQL, Django Rest Framework
please, refer to requirements.txt for details

---

## 1. Project Description
This project was developed with Python/Django, it's a backend / simple API for 
mobile application, which can be used by shop/store auditors, to check follow 
below steps:
1) Create at least 2 users, 2 stores, you can do it at admin panel of the project
2) to view list of stores, go to API url, for example: http://localhost:8000/api/store-list/?phone=009967707771771
3) to create store visiting log, go to api, for example: http://localhost:8000/api/store-visit/

---

## 2. Installation Steps:

```bash
$git clone
$virtualenv -p python3.9 .venv
$source .venv/bin/activate
$pip install -r requirements.txt
```

### Running Project locally, enter to core dorectory of project and start development server

```bash
$./manage.py runserver
```


### Starting Project at Production server

```bash
$docker-compose build .
$docker-compose up
```

---

## Architecture

**admin** - contains admin panel settings and configurations,

**Views** - contains logic for accepting request data and passing to API 

**Urls** - contains URL matching patterns with Views, ViewSets

**Models** - contains data and object presentation logic

**Settings** - Contains Project common settings like DB, Time, etc


