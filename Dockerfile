FROM python:3.9-slim

COPY ./src /app/src
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

WORKDIR /app/src

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]