Installation:
Clone repository
https://github.com/aln092020/app092020.git
cd app092020

Installing dependencies:
pip install -r requirements.txt



#python version = 3.6

Migrations:
python manage.py makemigrations
python manage.py migrate

Create super user:
python manage.py createsuperuser

Run App:
python manage.py runserver


in browser go to http://localhost:8000/