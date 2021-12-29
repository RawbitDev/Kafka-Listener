start: # Starts everything
	docker-compose up
	
detach: # Starts everything in detach mode
	docker-compose up -d

build: # Restart and force build everything
	docker-compose down -v
	docker-compose up --build

stop: # Shut down everything
	docker-compose down