DOCKER_NAME=buildver-resource
DOCKER_REPO=lukaszz/${DOCKER_NAME}
DOCKER_VERSION=latest

all:
	@pip freeze > src/requirements.txt
	@docker build . -t ${DOCKER_REPO}:${DOCKER_VERSION}
	@docker push ${DOCKER_REPO}:${DOCKER_VERSION}
