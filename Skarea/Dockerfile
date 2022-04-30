FROM python:3.9.0

WORKDIR /home

RUN git clone https://github.com/Georgia-MAX-holic/django-study.git

WORKDIR /home

RUN pup install -r requirements.txt

RUN python manage.py migrate 

EXPOSE 8000

CMD ["python", "namage.py", "runsever", "0.0.0.0:8000"]