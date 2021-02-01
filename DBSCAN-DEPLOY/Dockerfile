FROM python:3.8

RUN pip install numpy pandas json os flask sklearn gunicorn

COPY src/ app/

WORKDIR /app

ENV PORT 6001

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app