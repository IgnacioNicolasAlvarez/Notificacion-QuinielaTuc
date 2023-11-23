FROM python:3.10

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install

COPY . .

CMD ["poetry", "run", "python", "scheduler.py"]
