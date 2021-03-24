FROM python:3.6-slim

COPY . /06-run-selenium-tests

WORKDIR /06-run-selenium-tests

RUN pip install --no-cache-dir -r requirements.txt && chmod +x app.py

CMD ["./app.py"]
