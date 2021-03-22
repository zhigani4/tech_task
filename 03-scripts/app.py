#!/usr/bin/env python3

import docker
import os 

client = docker.from_env()

COUNT = int(os.environ.get('COUNT'))


for i in range(0, COUNT): 
    container = client.containers.run("alpine", detach=True )   
    print(container.id)
 