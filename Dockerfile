FROM python:3.12
WORKDIR /app

COPY pyproject.toml .
COPY requirements-dev.txt .

RUN pip install -r requirements-dev.txt

COPY . .

RUN pip install .

