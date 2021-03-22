FROM python:3.6-slim

ARG COUNT=1 

COPY . /03-scripts

COPY  app.py /app.py

WORKDIR /03-scripts

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 755 /app.py 

CMD ["/app.py"]