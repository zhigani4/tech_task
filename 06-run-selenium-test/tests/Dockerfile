FROM python:3.6-slim

ARG COUNT=1 

COPY . /tests

WORKDIR /tests

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest"]
