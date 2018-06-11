# Playing with Docker

Go to the project directory.
Build a Docker image from ```Dockerfile``` using this command:
```
docker build -t myfirstdocker ./main
```

Then run the container using this command:
```
docker run -it myfirstdocker:latest 
```