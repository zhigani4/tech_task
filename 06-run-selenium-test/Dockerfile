FROM python:3.6-slim

ARG COUNT=1 

COPY . /selenium

WORKDIR /selenium

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest"]
