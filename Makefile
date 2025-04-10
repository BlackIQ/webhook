APP_NAME = telegram-webhook
IMAGE_NAME = $(APP_NAME):latest
CONTAINER_NAME = $(APP_NAME)

.PHONY: all
all: build run

.PHONY: build
build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .

.PHONY: run
run:
	@echo "Running Docker container..."
	docker run -d --name $(CONTAINER_NAME) $(IMAGE_NAME)

.PHONY: update
update:
	@echo "Updating code from git..."
	git pull origin main

.PHONY: stop
stop:
	@echo "Stopping and removing container..."
	-docker stop $(CONTAINER_NAME)
	-docker rm $(CONTAINER_NAME)

.PHONY: redeploy
redeploy: stop update build run
	@echo "Redeployment complete!"

.PHONY: status
status:
	@echo "Checking container status..."
	docker ps -f name=$(CONTAINER_NAME)

.PHONY: logs
logs:
	@echo "Showing container logs..."
	docker logs $(CONTAINER_NAME)