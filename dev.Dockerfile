FROM python:3.11

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml .

RUN poetry install
