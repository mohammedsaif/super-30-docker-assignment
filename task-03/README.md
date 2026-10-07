# README.md

```markdown
# Task 3 — Run an Ubuntu Container with a Custom Name

## Objective

Run an Ubuntu Docker container with a custom container name such as `super30-linux`.

## Steps

### 1. Pull the Ubuntu Image

```bash
docker pull ubuntu:latest
```

Verify the image:

```bash
docker images
```

### 2. Run Ubuntu with a Custom Name

```bash
docker run -it --name super30-linux ubuntu:latest
```

### 3. Verify Ubuntu

Inside the container, run:

```bash
cat /etc/os-release
```

You can also run:

```bash
pwd
ls
```

### 4. Exit the Container

```bash
exit
```

### 5. Verify the Container Name

From the host machine:

```bash
docker ps -a
```

Check the `NAMES` column. It should show:

```text
super30-linux
```

### 6. Start the Container Again

```bash
docker start -ai super30-linux
```

Verify Ubuntu:

```bash
cat /etc/os-release
```

Then exit:

```bash
exit
```

## Expected Result

The task is successfully completed when:

- Ubuntu is pulled successfully.
- An Ubuntu container is created.
- The container name is `super30-linux`.
- `docker ps -a` displays `super30-linux`.
- The same container can be started and accessed again.

## Evidence to Capture

Capture screenshots showing:

1. Ubuntu image using `docker images`
2. Container creation using `docker run`
3. Ubuntu verification using `cat /etc/os-release`
4. `docker ps -a` showing `super30-linux`

## Key Docker Concepts

- Docker images
- Docker containers
- `docker pull`
- `docker run`
- Interactive containers
- Custom container names
- `docker ps -a`
- `docker start`

## Cleanup

To remove the container:

```bash
docker rm super30-linux
```

If it is running:

```bash
docker stop super30-linux
docker rm super30-linux
```

## Task Status

**Task 3 — Completed Successfully**
```