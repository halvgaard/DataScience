FROM python:3

ENV PIP_NO_CACHE_DIR=1
RUN pip3 install "poetry==1.1.12"

WORKDIR /app

COPY ["pyproject.toml", "poetry.lock", "/app/"]

RUN poetry config virtualenvs.create false
RUN poetry install

COPY ./helloworld /app/helloworld

EXPOSE 8000

CMD ["uvicorn", "helloworld.main:app", "--host=0.0.0.0", "--reload"]

