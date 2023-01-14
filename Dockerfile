FROM python:3.9.16

RUN apt update && apt install -y postgresql postgresql-contrib libpq-dev python3-dev
RUN pip3 install --upgrade pip

WORKDIR /Flask-project
COPY ./newspapper ./newspapper
COPY ./migrations ./migrations

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY wait_for_pg.sh wait_for_pg.sh
RUN chmod +x ./wait_for_pg.sh

COPY wsgi.py wsgi.py
# CMD ["python3", "wsgi.py"]