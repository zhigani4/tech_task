#!/usr/bin/env python3

import docker
import os
import requests

client = docker.from_env()

PATH = os.path.dirname(os.path.abspath(__file__)) + "/tests"
DRIVER_HOST = os.environ.get('DRIVER_HOST')
DRIVER_URL  = [ "http://" + DRIVER_HOST + ":4444/wd/hub/status"]
COUNT_THREADS = os.environ.get('COUNT_THREADS')
COUNT_NODES = int(os.environ.get('COUNT_NODES'))

client.images.build(
    path=PATH,
    dockerfile='Dockerfile',
    tag='selenium_test:latest'
    )

try:
    r = requests.get("http://" + DRIVER_HOST + ":4444/wd/hub/status", timeout=3)
    r.raise_for_status()
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)
for i in range(0, COUNT_NODES):
    container = client.containers.run(image="selenium_test:latest", command=["pytest", "-v", "-n" + COUNT_THREADS ], environment=["DRIVER_HOST=" + DRIVER_HOST], detach=True, )

for line in container.logs(stream=True):
    print(line.strip())