# OPCUA with Docker

# Getting Started

After installing docker, you pretty much need 3 steps to run the backend 

- Clone the repository
- Run  `make run-app`  in the root of the project, if on Linux, else `docker-compose up`

If you want to debug the application with PDB

you can debug the client with 
`docker-compose build && docker-compose run --service-ports client`

and the server with

`docker-compose build && docker-compose run --service-ports server`

