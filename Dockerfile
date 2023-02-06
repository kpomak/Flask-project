FROM python:3.9.16

# # Dockerfile for docker-compose # # # # # # # # 

# RUN apt update && apt install -y postgresql postgresql-contrib libpq-dev python3-dev
# RUN pip3 install --upgrade pip

# WORKDIR /Flask-project
# COPY ./newspapper ./newspapper
# COPY ./migrations ./migrations

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt

# COPY wait_for_pg.sh wait_for_pg.sh
# RUN chmod +x ./wait_for_pg.sh

# COPY wsgi.py wsgi.py
# CMD ["python3", "wsgi.py"]

# # End of Dockerfile # # # # # # # # # # # # # #

# # Dockerfile for fly.io # # # # # # # # # # # # 

WORKDIR /Flask-project

COPY ./newspapper ./newspapper
COPY ./migrations ./migrations
COPY requirements.txt requirements.txt
COPY wsgi.py wsgi.py

RUN pip3 install -r requirements.txt

# RUN flask db upgrade
# RUN flask create-admin admin admin@admin.com
# RUN flask create-tags

CMD ["gunicorn", "-b", "0.0.0.0:8080",  "wsgi:app"]