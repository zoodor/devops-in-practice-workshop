# Pre-Workshop Setup

To follow along with the hands-on exercises, I recommend that you perform this setup before
the workshop, since it will require you to download and install different tools, and that can
be time-consuming and risky given unreliable wifi connectivity.

## Installing Required Tools

1. Install Git
2. Install Docker 18+
3. Install kubectl 1.9.4+
4. Install VirtualBox 5.2+
5. Install minikube 0.26+
6. Install helm 2.8+
7. Install terraform 0.11+
8. Install google cloud SDK tools 196+

You can run the [`setup-workstation.sh`](./setup-workstation.sh) script to check that all
tools are installed (currently only supports MacOS, working on Linux and Windows versions).

## Google Cloud Platform Account Setup

You will need a working Google Cloud Platform account for the second half of the
workshop.

If you don't have one already, you can sign-up for a Google Cloud Platform
[free 12 months trial](https://cloud.google.com/free/). Once you sign-up,
you can create a project for the workshop (let's call it "DevOps Workshop") and
make sure the following APIs are enabled for your project:

1. [Google Compute Engine API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)
2. [Google Container Engine API](https://console.cloud.google.com/apis/api/container.googleapis.com/overview)
3. [Google Container Registry API](https://console.cloud.google.com/apis/api/containerregistry.googleapis.com/overview)

## Download large files

1. *Docker Images*: download the following Docker images by running the `docker pull <IMAGE>` command:
  * `docker pull openjdk:8-jdk-alpine`
  * `docker pull mysql:5.7`
  * `docker pull dtsato/gomatic`
2. *Maven Dependencies*: have Maven download all dependencies by running:
  * `./mvnw clean install`
3. *Minikube VM*: ensure you have the minikube VirtualBox VM images by running:
  * `minikube start --kubernetes-version v1.9.4`
  * `minikube stop`
