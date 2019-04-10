FROM python:3-alpine 

LABEL Description="This image holds a flask app for bonsai" Version="0.1.0"

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy --ignore-pipfile

COPY . /app

RUN pipenv install -e .
RUN env FLASK_APP=bonsai_web_api pipenv run flask init-db
ENTRYPOINT gunicorn -b :5000 bonsai_web_api:"create_app()"
