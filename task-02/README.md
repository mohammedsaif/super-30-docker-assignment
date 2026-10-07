# Task 2 — Install Python in an Ubuntu Container

## Objective

Create an Ubuntu Docker container, install Python inside the running container, and successfully execute a simple Python program.

## What You Need to Do

1. Pull the latest Ubuntu image from Docker Hub.
2. Create and start an Ubuntu container.
3. Open an interactive shell inside the container.
4. Update the Ubuntu package index.
5. Install Python 3 inside the container.
6. Verify that Python is installed correctly.
7. Create a simple Python program.
8. Execute the Python program successfully.
9. Exit the container.
10. Verify the container status from the host machine.

## Suggested Docker Commands

### 1. Pull Ubuntu

```bash
docker pull ubuntu:latest
```

### 2. Create and run the container

```bash
docker run -it --name super30-python ubuntu:latest
```

### 3. Update package information

Run inside the container:

```bash
apt update
```

### 4. Install Python

```bash
apt install -y python3
```

### 5. Verify Python

```bash
python3 --version
```

Expected output will be similar to:

```text
Python 3.x.x
```

### 6. Create a simple Python program

```bash
echo 'print("Hello from Python inside Docker!")' > hello.py
```

### 7. Execute the program

```bash
python3 hello.py
```

Expected output:

```text
Hello from Python inside Docker!
```

### 8. Exit the container

```bash
exit
```

## Verification

After exiting the container, run:

```bash
docker ps -a
```

You should see the `super30-python` container listed.

You can start and enter the same container again with:

```bash
docker start -ai super30-python
```

Then verify Python again:

```bash
python3 --version
```

And run the program:

```bash
python3 hello.py
```

## Expected Result

The task is successfully completed when:

- Ubuntu is running as a Docker container.
- Python 3 is installed inside the container.
- `python3 --version` works.
- A Python file is created inside the container.
- The Python program executes successfully.
- The program prints:

```text
Hello from Python inside Docker!
```

## Evidence to Capture

For the assignment/demo, capture screenshots or terminal output showing:

1. `docker images` showing the Ubuntu image.
2. `docker ps -a` showing the container.
3. `python3 --version` inside the container.
4. The Python program (`hello.py`).
5. Successful execution using `python3 hello.py`.

## Key Docker Concepts Demonstrated

- Docker images
- Docker containers
- Interactive containers
- Package installation inside containers
- Running commands inside containers
- Executing applications inside containers
- Container lifecycle management

## Cleanup

If the container is no longer required:

```bash
docker rm super30-python
```

If the container is still running, stop it first:

```bash
docker stop super30-python
docker rm super30-python
```
c