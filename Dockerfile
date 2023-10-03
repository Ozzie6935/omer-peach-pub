FROM python:3.7.3-alpine

LABEL R. Omer "omermedia@gmail.com"

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# CMD python /app/run.py