# README.md — Task 4: Container Lifecycle Management

```markdown
# Task 4 — Run, Verify, Stop, Restart, and Remove a Container

## Objective

Run a Docker container in detached mode, verify that it is running using `docker ps`, stop the container, restart it, and finally remove it.

This task demonstrates the basic Docker container lifecycle.

---

## Docker Container Lifecycle

The lifecycle demonstrated in this task is:

```text
Create → Run → Verify → Stop → Restart → Remove
```

---

## Step 1: Pull the Ubuntu Image

Pull the Ubuntu image if it is not already available:

```bash
docker pull ubuntu:latest
```

Verify the image:

```bash
docker images
```

---

## Step 2: Run the Container in Detached Mode

Run an Ubuntu container in detached mode:

```bash
docker run -d --name super30-detached ubuntu:latest sleep 3600
```

### Command Explanation

- `docker run` — Creates and starts a new container.
- `-d` — Runs the container in detached/background mode.
- `--name super30-detached` — Assigns a custom name.
- `ubuntu:latest` — Uses the Ubuntu image.
- `sleep 3600` — Keeps the container running for 1 hour.

Expected output:

```text
<container-id>
```

---

## Step 3: Verify the Running Container

Run:

```bash
docker ps
```

You should see:

```text
super30-detached
```

The container should have a status similar to:

```text
Up ...
```

Example:

```text
CONTAINER ID   IMAGE           COMMAND        STATUS        NAMES
xxxxxxxxxxxx   ubuntu:latest   "sleep 3600"   Up 10 sec     super30-detached
```

---

## Step 4: Stop the Container

Stop the running container:

```bash
docker stop super30-detached
```

Verify:

```bash
docker ps
```

The container should no longer appear because `docker ps` only displays running containers.

To see stopped containers:

```bash
docker ps -a
```

You should see:

```text
super30-detached
```

with a status similar to:

```text
Exited (137) ...
```

---

## Step 5: Restart the Container

Restart the stopped container:

```bash
docker start super30-detached
```

Verify that it is running again:

```bash
docker ps
```

The container should now show a status similar to:

```text
Up ...
```

---

## Step 6: Stop the Container Again

Stop the container:

```bash
docker stop super30-detached
```

Verify:

```bash
docker ps -a
```

The container should appear with an `Exited` status.

---

## Step 7: Remove the Container

Remove the stopped container:

```bash
docker rm super30-detached
```

Expected output:

```text
super30-detached
```

---

## Step 8: Verify That the Container Was Removed

Run:

```bash
docker ps -a
```

The `super30-detached` container should no longer appear.

---

## Complete Command Sequence

For a quick demonstration, the complete sequence is:

```bash
docker pull ubuntu:latest

docker run -d --name super30-detached ubuntu:latest sleep 3600

docker ps

docker stop super30-detached

docker ps -a

docker start super30-detached

docker ps

docker stop super30-detached

docker rm super30-detached

docker ps -a
```

---

## Expected Result

The task is successfully completed when:

- The Ubuntu container runs in detached mode.
- `docker ps` confirms that the container is running.
- The container can be stopped successfully.
- The stopped container can be restarted.
- The restarted container appears in `docker ps`.
- The container can finally be removed.
- `docker ps -a` confirms that the container no longer exists.

---

## Evidence to Capture

Capture screenshots or terminal output showing:

### 1. Container Running in Detached Mode

```bash
docker run -d --name super30-detached ubuntu:latest sleep 3600
```

### 2. Verify Running Container

```bash
docker ps
```

### 3. Stop Container

```bash
docker stop super30-detached
```

### 4. Verify Stopped Container

```bash
docker ps -a
```

### 5. Restart Container

```bash
docker start super30-detached
```

### 6. Verify Restarted Container

```bash
docker ps
```

### 7. Remove Container

```bash
docker rm super30-detached
```

### 8. Final Verification

```bash
docker ps -a
```

The container should no longer be listed.

---

## Key Docker Concepts Demonstrated

- Detached mode
- Running containers
- `docker run`
- `docker ps`
- `docker stop`
- `docker start`
- `docker rm`
- Container lifecycle
- Container status verification

---

## Task Status

**Task 4 — Completed Successfully**
```