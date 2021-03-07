run-app:
	docker-compose up --build

stop:
	docker-compose down 

run-debug-client:
	docker-compose build && docker-compose run --service-ports client

run-debug-server:
	docker-compose build && docker-compose run --service-ports server
