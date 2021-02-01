FROM python:3.8

RUN pip install numpy gunicorn
RUN pip install pandas
RUN pip install flask
RUN pip install sklearn
RUN pip install firebase-admin

COPY src/ app/

WORKDIR /app

ENV PORT 6001

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app