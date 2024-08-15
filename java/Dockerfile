# Use an official OpenJDK runtime as a parent image
FROM openjdk:11-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Compile the Java application
RUN javac Main.java

# Specify the command to run the Java application
CMD ["java", "Main"]
