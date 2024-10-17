# Spring Hello World
## Build
- `docker build -t hello-spring .`
## Run
- `docker run -v $(pwd)/demo:/app -p 8080:8080 --rm hello-spring ./gradlew bootRun`
- open `http://localhost:8080`