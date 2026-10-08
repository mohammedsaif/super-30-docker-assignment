What to build
Task: Complete all 23 Docker exercises below. The objective is to demonstrate that you understand images, containers, Dockerfiles, ports, volumes, networking, environment variables, Docker Compose, and containerizing an API.

1
Pull the latest Ubuntu Docker image and run it interactively. Execute at least five Linux commands inside the container.

2
Create an Ubuntu container, install Python inside it, and successfully execute a simple Python program.

3
Run an Ubuntu container with a custom container name such as super30-linux.

4
Run a container in detached mode, verify it using docker ps, stop it, restart it, and finally remove it.

5
Pull at least three different Docker images from Docker Hub and display all locally available images.

6
Create a simple Python application and write your first Dockerfile to containerize it.

7
Build a custom Docker image called:

docker build -t super30-python-app .

Run the image and verify that your Python program executes successfully.

8
Create a simple FastAPI application and containerize it using Docker.

9
Run your FastAPI container on port 8000 and access the API from your browser.

10
Run the same FastAPI Docker image using a different host port, for example:

docker run -p 5000:8000 super30-api

Explain why the API is now accessible through port 5000.

11
Create a Dockerfile using WORKDIR, COPY, RUN, EXPOSE, and CMD. Explain the purpose of every instruction.

12
Create a requirements.txt containing FastAPI, Uvicorn, and other required dependencies. Install them automatically while building the Docker image.

13
Pass an environment variable to a Docker container and access its value from your Python/FastAPI application.

14
Create a .env file containing application configuration and use those environment variables with your Dockerized application. Do not commit sensitive .env values to GitHub.

15
Create a Docker volume, store some data inside it, remove the container, create another container using the same volume, and prove that the data still exists.

16
Create two containers and connect them using a custom Docker network. Demonstrate that one container can communicate with the other.

17
Create a PostgreSQL Docker container with database name, username, and password configured through environment variables.

18
Create a FastAPI application that connects to the PostgreSQL container. Both applications should run as separate containers.

19
Create a docker-compose.yml that starts both:

FastAPI

↓

PostgreSQL

Start the complete application using

docker compose up

20
Extend the previous application to have three services:

Frontend

↓

FastAPI Backend

↓

PostgreSQL

All three should run as separate containers.

21
Implement a health check for your FastAPI application. Create a /health endpoint and configure Docker/Compose to check whether the service is healthy.

22
Create a small CRUD application using FastAPI + PostgreSQL + Docker Compose. Implement Create, Read, Update, and Delete operations and demonstrate that database data survives container restarts.

23
Final Challenge — Dockerize a Complete Mini Project. Build a Student Management System containing a frontend or simple UI/client, FastAPI backend, PostgreSQL database, environment configuration, persistent database volume, Docker network, and Docker Compose configuration. The entire project should start with one command:

docker compose up --build

The application should provide APIs for creating, viewing, updating, searching, and deleting students.

Submission Criteria

Students must complete all 23 problems and create a single GitHub repository, for example:

super30-docker-assignment

Organize each exercise clearly (task-01, task-02, etc.) and include a proper README.md containing setup instructions, Docker commands used, architecture for the final project, and instructions to reproduce the output.

Students must also create a YouTube explanation video demonstrating their work. They should show the Docker commands, Dockerfiles, images and running containers, port mapping, volumes, networking, Docker Compose, and the final application running.

Final submission must contain

1
GitHub Repository Link

2
YouTube Video Link

Your submission
Code
