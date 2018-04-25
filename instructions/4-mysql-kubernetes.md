# Exercise 4 - Running MySQL on Kubernetes

## Goals

* Learn about Kubernetes concepts: Pods, Services, Deployments
* Learn about minikube
* Learn to provision a Persistent Volume in Kubernetes
* Learn to use Kubernetes to manage secrets
* Learn about the `kubectl` CLI tool
* Deploy a single-instance MySQL database in Kubernetes

## Acceptance Criteria

* Kubernetes files should be in a `kubernetes` folder
* Create a secret in kubernetes using `kubectl` to store the database password
securely
* Create a `deploy.sh` script at the root of the project that uses `kubectl` to
deploy MySQL
* MySQL user password is stored and managed as a kubernetes secret and not stored
in plain-text on any configuration file

## Step by Step Instructions

First of all, let's start minikube to launch a local Kubernetes cluster:

```shell
$ minikube start --bootstrapper kubeadm
Starting local Kubernetes v1.9.4 cluster...
Starting VM...
Getting VM IP address...
Moving files into cluster...
Setting up certs...
Connecting to cluster...
Setting up kubeconfig...
Starting cluster components...
Kubectl is now configured to use the cluster.
Loading cached images from config file.
```

You can check that the cluster started by running the `kubectl cluster-info` command
or opening a web dashboard by running `minikube dashboard`:

```shell
$ kubectl cluster-info
Kubernetes master is running at https://192.168.99.100:8443
KubeDNS is running at https://192.168.99.100:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
$ minikube dashboard
Opening kubernetes dashboard in default browser...
```

Create secret:
```shell
$ kubectl create secret generic mysql-pass --from-literal password=S3cr3t
secret "mysql-pass" created
$ kubectl get secrets
NAME                  TYPE                                  DATA      AGE
default-token-8856j   kubernetes.io/service-account-token   3         2d
mysql-pass            Opaque                                1         32s
```

Create the kubernetes definition file:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: pet-db
  labels:
    app: pet
spec:
  ports:
    - port: 3306
  selector:
    app: pet
    tier: db
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-pv-claim
  labels:
    app: pet
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 8Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pet-db
  labels:
    app: pet
spec:
  selector:
    matchLabels:
      app: pet
      tier: db
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: pet
        tier: db
    spec:
      containers:
      - image: mysql:5.7
        name: mysql
        env:
        - name: MYSQL_RANDOM_ROOT_PASSWORD
          value: "yes"
        - name: MYSQL_DATABASE
          value: petclinic
        - name: MYSQL_USER
          value: petclinic-user
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-pass
              key: password
        ports:
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - name: mysql-persistent-storage
          mountPath: /var/lib/mysql
      volumes:
      - name: mysql-persistent-storage
        persistentVolumeClaim:
          claimName: db-pv-claim
```

Create a file called `deploy.sh` with the following content:

```bash
#!/usr/bin/env bash
set -xe
kubectl apply -f kubernetes/mysql.yml
```

Change the file permission and execute it:

```shell
$ chmod a+x deploy.sh
$ ./deploy.sh
$ kubectl apply -f kubernetes/mysql.yml
service "pet-mysql" created
persistentvolumeclaim "mysql-pv-claim" created
deployment "pet-mysql" created
```

Validate:

```shell
$ kubectl get pods
NAME                         READY     STATUS    RESTARTS   AGE
pet-mysql-86955bcb8d-r5z9f   1/1       Running   0          39s
$ kubectl get service
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP    3d
pet-mysql    ClusterIP   None         <none>        3306/TCP   45s
```
