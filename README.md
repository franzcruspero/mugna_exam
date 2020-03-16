# Pokedex
Pokedex app utilizing PokeAPI using Python 3.8.2 and Django ver. 3.0.4

## Software requirements
- Postgres
- Python 3.8
- Pipenv

## Setup postgres db and user (this assumes you already have a user)
```bash
sudo -u postgres psql

CREATE DATABASE pokedex;

GRANT ALL PRIVILEGES ON DATABASE pokedex TO myprojectuser;
```
If you don't have a user, run these command (while still inside psql) before running the GRANT ALL PRIVILEGES line:
```bash
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```

## Setup of settings.py
- In settings.py change the database settings (line 82) to your respective postgres db user

```bash
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'pokedex',
      'USER': 'myprojectuser',
      'PASSWORD': 'password',
      'HOST': 'localhost',
      'PORT': '',
  }
}
```

## Initialization of app (inside project folder)

```bash
pipenv --python 3.8 install django

pipenv shell

pipenv install

cd src/ 

python manage.py download_pokemon

python manage.py runserver
```
