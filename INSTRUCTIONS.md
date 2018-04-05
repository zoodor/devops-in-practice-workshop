# Exercise 1 - Package and Run Application with Docker

## Goals

* Learn how to build and package Docker containers
* Run the application on Docker
* Learn about `Dockerfile`, Kitematic, and port forwarding

## Acceptance Criteria

* Docker image is created and tagged as `pet-app`
* Docker container is running and exposing port 8080 (can be seen in Kitematic, if installed)
* Application can be accessed on http://localhost:8080

## Step by Step Instructions

Create a new file called `Dockerfile` at the root of the project, with the following content:

```Dockerfile
FROM openjdk:8-jdk-alpine
VOLUME /tmp
ARG JAR_FILE

ADD ${JAR_FILE} app.jar
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
```

Ensure the `jar` file containing the application packaged in step 0 is still available
in the `target` folder. If not, rebuild it and remember the path to the file.

```shell
$ ls target/*.jar
target/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar
```

Build the container image, passing the path to the `jar` file as a build argument, as well as
the specified tag `pet-app`:

```shell
$ docker build --tag=pet-app --build-arg JAR_FILE=target/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar .
Sending build context to Docker daemon  49.91MB
Step 1/5 : FROM openjdk:8-jdk-alpine
 ---> 224765a6bdbe
Step 2/5 : VOLUME /tmp
 ---> Using cache
 ---> 974dde5c7d99
Step 3/5 : ARG JAR_FILE
 ---> Using cache
 ---> 240b721e4168
Step 4/5 : ADD ${JAR_FILE} app.jar
 ---> 4c7421b72aa8
Step 5/5 : ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
 ---> Running in fe55baeed48e
Removing intermediate container fe55baeed48e
 ---> 74ffe8466331
Successfully built 74ffe8466331
Successfully tagged pet-app:latest
```

Ensure the container image was created and tagged correctly:

```shell
$ docker image ls pet*
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
pet-app             latest              74ffe8466331        7 minutes ago       140MB
```

Let's run a docker container in daemon mode to start up our application and expose
the container port 8080 in the host:

```shell
$ docker run --name=pet-app-prod -d -p 8080:8080 pet-app
11ac55ff100dc341fb47e863f42e01b0579b81c62bc49c8b6f89daf0690c8d48
```

The long string returned from that command is the container ID. To check its logs:

```shell
$ docker logs -f 11ac55ff100dc3
```

Notice you only require the initial part of the long string. You can also ensure
the container is running by running the `docker ps` command:

```shell
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
11ac55ff100d        pet-app             "java -Djava.securit…"   10 minutes ago      Up 10 minutes       0.0.0.0:8080->8080/tcp   pet-app-prod
```

If you have Kitematic installed, you can also check the container is running from
its UI.

Then you should be able to access the application by going to http://localhost:8080.

To shutdown, you can stop and remove the container:

```shell
$ docker stop 11ac55ff100dc3
11ac55ff100dc3
$ docker rm 11ac55ff100dc3
11ac55ff100dc3
```
