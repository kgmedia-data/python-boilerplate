IMAGE := myimage
GIT_ID := $(shell git rev-parse --short HEAD)

docker-build:
	docker build -t ${IMAGE}:${GIT_ID} .

docker-push:
	docker push ${IMAGE}:${GIT_ID}

docker-deploy: docker-build docker-push