FROM python:3

ENV PIP_NO_CACHE_DIR=1
RUN pip3 install "poetry==1.1.12"

RUN python -m venv /venv
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY ["pyproject.toml", "poetry.lock", "/app/"]

RUN poetry install

COPY ./src /app/src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]

