# Exercise 6 - Scaling up our Application

## Goals

* Learn about Kubernetes concepts: replica sets and deployments
* Scaling a deployment

## Acceptance Criteria

* Create a `web.yml` file in the `kubernetes` folder to define the k8s objects
required to deploy a single-instance Pet application and connect it to the MySQL
service
* Update the `deploy.sh` script at the root of the project to deploy the application
* Update the application to read database configuration from environment variables
* Application is exposed on the host and can be accessed on `http://<CLUSTER_IP>:8080`

## Step by Step Instructions

Run the following `kubectl` command to increase the `pet-web` deployment to 5
replicas:

```shell
$ kubectl scale deployment pet-web --replicas=5
deployment "pet-web" scaled
```

Verify that it worked:

```shell
$ kubectl get deployment
NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
pet-db    1         1         1            1           17h
pet-web   5         5         5            5           3h
$ kubectl get pod
NAME                      READY     STATUS    RESTARTS   AGE
pet-db-7997cf844-lsppt    1/1       Running   0          17h
pet-web-bc5d4c9f6-2j26j   1/1       Running   0          3h
pet-web-bc5d4c9f6-l4klv   1/1       Running   0          28s
pet-web-bc5d4c9f6-nxf78   1/1       Running   0          28s
pet-web-bc5d4c9f6-r9c54   1/1       Running   0          28s
pet-web-bc5d4c9f6-zpkkl   1/1       Running   0          29s
```

Get the external service URL to test the application is working and accessible:

```shell
$ minikube service pet-web --url
http://192.168.99.100:30596
```

Visiting the URL in your browser (in this case http://192.168.99.100:30596)
should open the PetClinic application.
