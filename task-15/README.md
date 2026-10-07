Task 15 — Docker Volume Persistence
Objective
Create a Docker volume, store data inside it, remove the container, create another container using the same volume, and prove that the data still exists.
1. Create a Docker Volume
docker volume create super30-data

Verify:
docker volume ls

You should see:
super30-data

2. Create a Container Using the Volume
Run an Ubuntu container:
docker run -it --name volume-container-1 -v super30-data:/data ubuntu

Inside the container, create a file:
echo "Docker volume data persists!" > /data/message.txt

Verify:
cat /data/message.txt

Expected:
Docker volume data persists!

Exit:
exit

3. Remove the First Container
docker rm volume-container-1

Check:
docker ps -a

The container should no longer exist.
Important: We removed the container, but we did not remove the volume.
4. Create Another Container Using the Same Volume
docker run -it --name volume-container-2 -v super30-data:/data ubuntu

Inside the new container:
cat /data/message.txt

Expected:
Docker volume data persists!

This proves that the data survived even though the original container was deleted.
5. Verify the Volume
From another PowerShell terminal:
docker volume inspect super30-data

You can see information about the volume and where Docker manages it.
Volume Concept
                 Docker Volume
                super30-data
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
 volume-container-1      volume-container-2
          │                     │
          │ write               │ read
          ▼                     ▼
     message.txt  ──────────> message.txt

The important point is:
Container data is temporary by default, but data stored in a Docker volume can survive container deletion.

Cleanup
After completing the demonstration:
docker rm volume-container-2
docker volume rm super30-data