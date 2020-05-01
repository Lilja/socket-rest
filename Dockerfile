FROM python:3.8-alpine

LABEL maintainer="Erik <erikvlilja+socket-rest@gmail.com>"

RUN mkdir /app

COPY pyproject.toml /app/
COPY poetry.lock /app/

WORKDIR /app

RUN apk add --no-cache libressl-dev musl-dev libffi-dev gcc g++ make
RUN pip --no-cache-dir install poetry poetry-setup \
    && poetry install \
    && rm -rf ~/.config/pypoetry

COPY . /app

EXPOSE 8000

CMD ["poetry", "run", "python", "/app/app.py"]
