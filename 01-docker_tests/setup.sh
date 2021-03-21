#docker build app for local work without DockerHub
docker build -t simply_calc . 

#docker build image for tests app for local wokr without DockerHub 
docker build -t test_calc ./tests
