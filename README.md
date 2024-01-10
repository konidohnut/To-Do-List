# To-Do List


### Building the Docker Image
1. Clone the repository to your machine:
```bash
git clone https://github.com/your-repo.git
```

2. Build the Docker image using the docker build command:

```bash
docker build -t my-app -f Dockerfile .
```
This command will create a Docker image based on the Dockerfile located in the root of the project and assign it the name my-fastapi-app.

### Running the Docker Container

After successfully building the Docker image, you can run the container using the following command:

```bash
 docker compose up  
```

### Create and restart containers
```bash
docker compose up --build
```


### Stopping the Container

```bash
docker stop my-fastapi-container
```

### Migrations with Alembic for SQLAlchemy models
1. Initialize Alembic:

Inside your Docker container's command line, run the command
```bash
alembic init alembic
```

2. Create the First Migration:
```bash
docker exec -it (name) alembic revision --autogenerate -m "Initial migration"
or
docker compose exec (name) alembic revision --autogenerate -m ""
```

3. Apply Migrations:
```bash
alembic upgrade head
```