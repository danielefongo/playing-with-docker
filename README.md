# Playing with Docker

Go to the project directory.
Build a Docker image from ```Dockerfile``` using this command:
```
docker build -t myfirstdocker ./main
```

Then run the container using this command:
```
docker run -it -p 8080:80 myfirstdocker:latest
```

Then open a browser and try these URLS:
- ```http:localhost:8080/hello```
- ```http:localhost:8080/hello?name=Pippo```