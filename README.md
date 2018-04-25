# DevOps in Practice Hands-On Workshop

This project is a fork of the [Spring Petclinic](https://github.com/spring-projects/spring-petclinic)
application. It is used as the sample application for the workshop "DevOps in Practice".

## Workshop Instructions

The workshop is divided into several steps, which build on top of each other. Instructions for
each exercise can be found in a file called `INSTRUCTIONS.md` at the root of the project. A
sample response, as well as instructions for the next step are found on a separate branch `step-N`,
where `N` corresponds to the next step number (e.g. `step-1`, `step-2`, ...)

I recommend you fork this project before cloning to your machine, to allow you to
make changes, commit them, and push to your own repository

## Pre-Workshop Setup

If you want to follow the hands-on exercises, I recommend that you perform the setup before
the workshop, since it will require you to download and install different tools, and that can
be time-consuming and risky given unreliable wifi connectivity.

### Workstation setup

1. Install Git
2. Install Docker 18+
3. Install kubectl 1.9.4+
4. Install VirtualBox 5.2+
5. Install minikube 0.26+
6. Install helm 2.8+
7. Install terraform 0.11+
8. Install google cloud SDK tools 196+

You can run the `setup-workstation.sh` script to check that all tools are installed.

### Google Cloud Platform account setup

If you don't have it already, you can sign-up for a Google Cloud Platform
[free trial](https://cloud.google.com/free/) for 12 months. Once you sign-up,
you can create a project for the workshop (let's call it "DevOps Workshop") and
make sure the following APIs are enabled for your project:

1. [Google Compute Engine API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)
2. [Google Container Engine API](https://console.cloud.google.com/apis/api/container.googleapis.com/overview)
3. [Google Container Registry API](https://console.cloud.google.com/apis/api/containerregistry.googleapis.com/overview)

### Download large files

I recommend you download the following Docker images prior to the workshop by
running the `docker pull <IMAGE>` command:

* `docker pull openjdk:8-jdk-alpine`
* `docker pull mysql:5.7`
* `docker pull dtsato/gomatic`

You can also follow the `INSTRUCTIONS.md` for step 0 to have Maven download all
dependencies by running `./mvnw clean install`.

Finally, to ensure the minikube VirtualBox VM is setup, you can run
`minikube start` once to download it and `minikube stop` to stop it.

# License

The materials for the workshop and the Spring PetClinic sample application are released
under version 2.0 of the [Apache License](http://www.apache.org/licenses/LICENSE-2.0).
