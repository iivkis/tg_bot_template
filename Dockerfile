FROM python:3.11.7

WORKDIR /

RUN pip install poetry

COPY ./poetry.lock ./pyproject.toml ./

RUN poetry install

COPY . .

CMD ["poetry", "run", "python", "./main.py"]