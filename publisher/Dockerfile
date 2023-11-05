# Build stage
FROM maven:3.6.0-jdk-11-slim AS build
WORKDIR /home/app
COPY ./src /home/app/src
COPY ./pom.xml /home/app
RUN mvn -f /home/app/pom.xml clean package

# Package stage
FROM openjdk:11-jre-slim
WORKDIR /home/app
COPY ./target/publisher-jar-with-dependencies.jar publisher.jar
ENTRYPOINT ["java", "-jar", "publisher.jar", "#.publish"]
EXPOSE 9000