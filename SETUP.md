# Pre-Workshop Setup

To follow along with the hands-on exercises, I recommend that you perform this
setup before the workshop, since it will require you to download and install
different tools, and that can be time-consuming and risky given unreliable wi-fi
connectivity.

## Installing Required Tools

These are the tools required for the workshop and the links for installation
instructions if you want to install them manually:

* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Docker](https://docs.docker.com/install/) 18+
* [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) 1.9.4+
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) 5.2+
* [Install minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) 0.25+
* [helm](https://github.com/kubernetes/helm/blob/master/docs/install.md) 2.8+
* [terraform](https://www.terraform.io/intro/getting-started/install.html) 0.11+
* [Google Cloud SDK tools](https://cloud.google.com/sdk/downloads) 196+

### Auto-Install on Mac OS X

You can run the [`setup-workstation.sh`](./setup-workstation.sh) script to
install the required tools using [HomeBrew](https://brew.sh/).

### Auto-Install on Windows + Powershell

If you have Powershell, make sure you open an [administrative shell](http://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/)
and you can execute the [`setup/windows.ps1`](./setup/windows.ps1) script to
install the required tools using [Chocolatey](https://chocolatey.org).

### Auto-Install on Linux

In progres...

## Google Cloud Platform Account Setup

You will need a working Google Cloud Platform account for the second half of the
workshop.

If you don't have one already, you can sign-up for a Google Cloud Platform
[free 12 months trial](https://cloud.google.com/free/). Once you sign-up, you
can create a project for the workshop and name it "DevOps Workshop".

## Download large files

1. **Docker Images**: download the following Docker images by running:
  * `docker pull openjdk:8-jdk-alpine`
  * `docker pull mysql:5.7`
  * `docker pull dtsato/gomatic`
2. **Maven Dependencies**: have Maven download all dependencies by running:
  * `./mvnw clean install`
3. **Minikube VM**: ensure you have the minikube VirtualBox VM image by running:
  * `minikube start --kubernetes-version v1.9.4`
  * `minikube stop`
