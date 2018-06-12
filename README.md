# Playing with Docker

Go to the project directory.
Build a Docker images and run containers from ```docker-compose.yml``` using this command:
```
docker-compose up
```

Then open a browser and try these URLS:
- Welcome message: ```http:localhost:8080/hello?name=Pippo```
- Add person: ```http:localhost:8080/insert?name=Pippo&surname=Bond```
- View people: ```http:localhost:8080/query```