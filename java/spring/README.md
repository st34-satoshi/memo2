# Spring Hello World
## Build
- `docker build -t hello-spring .`
## Run
- `docker run -it --rm -p 8080:8080 hello-spring ./gradlew bootRun`
- open `http://localhost:8080`