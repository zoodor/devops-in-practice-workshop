# Exercise 2 - Running with a Persistent Database

## Goals

* Decouple database service from the Application
* Run a MySQL database on Docker
* Learn about Docker persistent volumes and linking container
* Re-run the application on Docker

## Acceptance Criteria

* Application configuration modified to connect to MySQL database
* Docker image is rebuilt and tagged as `pet-app`
* MySQL running in Docker
* Application running in Docker and linked to MySQL container
* Application can be accessed on http://localhost:8080
* New owner is created, with at least 1 pet
* Kill and restart application container
* Owner created in previous step is still available

## Step by Step Instructions


```shell
$ mkdir data
$ docker run -d --name pet-db -v $PWD/data:/var/lib/mysql -e MYSQL_RANDOM_ROOT_PASSWORD=yes -e MYSQL_DATABASE=petclinic -e MYSQL_USER=petclinic-user -e MYSQL_PASSWORD=S3cr3t mysql:5.7
```

```shell
$ docker run --name=pet-app-prod -d -p 8080:8080 -e "SPRING_PROFILES_ACTIVE=mysql" --link pet-db pet-app
ff776db53488ff18644bfd79e39f7101501dbfd4cc0216f041051a1155a8adaf
```

Then you should be able to access the application by going to http://localhost:8080.

To shutdown, you can stop and remove the container:

```shell
$ docker stop 11ac55ff100dc3
11ac55ff100dc3
$ docker rm 11ac55ff100dc3
11ac55ff100dc3
```
