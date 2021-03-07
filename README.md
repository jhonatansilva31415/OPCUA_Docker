# OPCUA with Docker

# Getting Started

After installing docker, you pretty much need 3 steps to run the backend 

- Clone the repository
- Run  `make run-app`  in the root of the project, if on Linux, else `docker-compose up`

With this, the API should spin up, but you still need to create the tables for the database

Linux

`make local-createdb`

Windows

`docker-compose exec api python manage.py recreate_db`

You can now go to http://localhost:5000 and you should see the Swagger for the API.

If you experience any problems with postgres setup, you may need to clean up your system, sometimes it happens, mostly if you have other APIs that use the same name conventions. You can try `make stop` and `docker system prune`, it's a bit harsh, but it'll clean up your docker system. After that everything should run smoothly.
