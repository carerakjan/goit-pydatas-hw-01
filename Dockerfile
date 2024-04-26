FROM python:3.9.6

ENV APP_HOME /app

# VOLUME ${APP_HOME}/addressbook.pkl

WORKDIR $APP_HOME

COPY . .

RUN python -m pip install pipenv
RUN pipenv install

ENTRYPOINT ["pipenv", "run", "python", "main.py"]