FROM openjdk:17-jdk-slim

WORKDIR /app

COPY . /app

WORKDIR /app/demo

EXPOSE 8080

CMD ["./gradlew", "bootRun"]
