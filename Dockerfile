FROM python:3.9.5 AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update -y&&\
    apt-get install nano libpq-dev python-dev -y && \ 
    apt-get clean

RUN pip install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev


COPY ./entrypoint.sh /entrypoint.sh


COPY ./ .

RUN chmod +x /entrypoint.sh


EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]

CMD gunicorn Bigbox.wsgi:application --bind 0.0.0.0:$PORT
