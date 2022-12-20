# docker-container-flask
This repository contains a basic Dockerfile configuration alongside  a minimal python flask template.

## Commands to run in order to build and load the image.

Building the container image:
```sh
docker build -t flask-container-demo .
```

Running the container image:
```sh
docker run -p 5000:5000 -d flask-container-demo
```

Entering the container:
```sh
docker exec -ti -u root <container_name/container_id> bash
```

Exporting the container filesystem into a .tar archive:
```sh
docker container export -o filesystem.tar <container_name/container_id>
```

Tagging and Pushing the container to dockerhub:
```sh
docker tag flask-container-demo vladadochitei/flask-container-demo
docker push vladadochitei/flask-container-demo
```