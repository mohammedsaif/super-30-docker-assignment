Task 16 — Connect Two Containers Using a Custom Docker Network
Objective
Create a custom Docker network, connect two containers to it, and demonstrate communication between them.
We'll use:
- Container 1: super30-server
- Container 2: super30-client
- Network: super30-network
1. Create a Custom Network
docker network create super30-network

Verify:
docker network ls

You should see:
super30-network

2. Create the Server Container
Run an Nginx container:
docker run -d --name super30-server --network super30-network nginx

Verify:
docker ps

You should see:
super30-server

3. Create the Client Container
Run an Ubuntu container on the same network:
docker run -it --name super30-client --network super30-network ubuntu

Inside the client container, install curl:
apt update
apt install -y curl

4. Communicate With the Server
From inside super30-client, run:
curl http://super30-server

You should receive an Nginx response similar to:
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
</html>

This proves that:
super30-client
       │
       │ HTTP request
       ▼
super30-server
       │
       ▼
     Nginx

The client can communicate with the server using the container name:
super30-server

You don't need to find or hard-code the server's IP address.
5. Inspect the Network
Exit the client:
exit

Then run:
docker network inspect super30-network

You should see both:
super30-server
super30-client

connected to the network.
6. Demonstrate That They Are on the Same Network
Run:
docker inspect super30-server

and:
docker inspect super30-client

Both should show:
super30-network

Network Architecture
              super30-network
        ┌─────────────────────────┐
        │                         │
        │  super30-client         │
        │       │                 │
        │       │ HTTP            │
        │       ▼                 │
        │  super30-server         │
        │       │                 │
        │       ▼                 │
        │      Nginx              │
        │                         │
        └─────────────────────────┘

Key Concept
Docker's custom network provides container-to-container communication.
Instead of:
http://172.x.x.x

the client can use:
http://super30-server

Docker's internal DNS resolves the container name to the appropriate container IP.
Cleanup
Remove the containers:
docker rm -f super30-client
docker rm -f super30-server

Remove the network:
docker network rm super30-network

Verify:
docker network ls
