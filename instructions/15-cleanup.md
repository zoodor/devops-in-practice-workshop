# Exercise 15 - Cleanup

## Goals

* Ensure all cloud resources are disposed

## Acceptance Criteria

* Use terraform to teardown the GKE infrastructure

## Step by Step Instructions

Since all our infrastructure was deployed to GKE, we can use the `terraform destroy`
command to cleanup everything and ensure we're not paying for unused cloud
resources:

```shell
$ terraform destroy terraform/
google_container_cluster.cluster: Refreshing state... (ID: devops-workshop-gke)

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  - google_container_cluster.cluster


Plan: 0 to add, 0 to change, 1 to destroy.

Do you really want to destroy?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

google_container_cluster.cluster: Destroying... (ID: devops-workshop-gke)
google_container_cluster.cluster: Still destroying... (ID: devops-workshop-gke, 10s elapsed)
google_container_cluster.cluster: Still destroying... (ID: devops-workshop-gke, 20s elapsed)
google_container_cluster.cluster: Still destroying... (ID: devops-workshop-gke, 30s elapsed)
google_container_cluster.cluster: Still destroying... (ID: devops-workshop-gke, 40s elapsed)
google_container_cluster.cluster: Still destroying... (ID: devops-workshop-gke, 50s elapsed)
google_container_cluster.cluster: Still destroying... (ID: devops-workshop-gke, 1m0s elapsed)
google_container_cluster.cluster: Still destroying... (ID: devops-workshop-gke, 1m10s elapsed)
google_container_cluster.cluster: Still destroying... (ID: devops-workshop-gke, 1m20s elapsed)
google_container_cluster.cluster: Still destroying... (ID: devops-workshop-gke, 1m30s elapsed)
google_container_cluster.cluster: Still destroying... (ID: devops-workshop-gke, 1m40s elapsed)
google_container_cluster.cluster: Destruction complete after 1m42s

Destroy complete! Resources: 1 destroyed.
```

Then, we can run the following script to cleanup all the unused `pet-app` images
from Google Container Registry, replacing your Project ID in two occurrences:

```shell
$ for image in $(gcloud container images list-tags us.gcr.io/devops-workshop-123/pet-app --format='get(digest)'); do gcloud container images delete --force-delete-tags -q us.gcr.io/devops-workshop-123/pet-app@$image; done
Digests:
- us.gcr.io/devops-workshop-201010/pet-app@sha256:ac317e98ec1bee6680b888ec2de907264493ce78567a72d0de7e98aa0aa411da
  Associated tags:
 - latest
Deleted [us.gcr.io/devops-workshop-201010/pet-app:latest].
Deleted [us.gcr.io/devops-workshop-201010/pet-app@sha256:ac317e98ec1bee6680b888ec2de907264493ce78567a72d0de7e98aa0aa411da].
Digests:
- us.gcr.io/devops-workshop-201010/pet-app@sha256:a3bbf730cabb85237ba3cd1089232f1ffb85ae117b50aa32af366831439652cf
  Associated tags:
 - 19
Deleted [us.gcr.io/devops-workshop-201010/pet-app:19].
Deleted [us.gcr.io/devops-workshop-201010/pet-app@sha256:a3bbf730cabb85237ba3cd1089232f1ffb85ae117b50aa32af366831439652cf].
Digests:
- us.gcr.io/devops-workshop-201010/pet-app@sha256:eb75759b588c3a11183bdc69b195b8e15eff9af8476a5d33d919220f3159c68c
  Associated tags:
 - 17
Deleted [us.gcr.io/devops-workshop-201010/pet-app:17].
Deleted [us.gcr.io/devops-workshop-201010/pet-app@sha256:eb75759b588c3a11183bdc69b195b8e15eff9af8476a5d33d919220f3159c68c].
```

Finally, we can delete the service account we created for the GoCD Agent, once
again replacing with your Project ID:

```shell
$ gcloud iam service-accounts delete gocd-agent@devops-workshop-123.iam.gserviceaccount.com
You are about to delete service account
[gocd-agent@devops-workshop-123.iam.gserviceaccount.com].

Do you want to continue (Y/n)?  Y

deleted service account [gocd-agent@devops-workshop-123.iam.gserviceaccount.com]
$ gcloud projects remove-iam-policy-binding devops-workshop-123 --member serviceAccount:gocd-agent@devops-workshop-123.iam.gserviceaccount.com --role roles/storage.admin
bindings:
- members:
  - serviceAccount:gocd-agent@devops-workshop-123.iam.gserviceaccount.com
  role: roles/container.admin
- members:
  - serviceAccount:gocd-agent@devops-workshop-123.iam.gserviceaccount.com
  role: roles/container.clusterAdmin
- members:
  - serviceAccount:service-190704809516@container-engine-robot.iam.gserviceaccount.com
  role: roles/container.serviceAgent
- members:
  - serviceAccount:190704809516-compute@developer.gserviceaccount.com
  - serviceAccount:190704809516@cloudservices.gserviceaccount.com
  - serviceAccount:service-190704809516@containerregistry.iam.gserviceaccount.com
  role: roles/editor
- members:
  - user:dtsato@gmail.com
  role: roles/owner
etag: BwVp2RX4cHA=
version: 1
$ gcloud projects remove-iam-policy-binding devops-workshop-123 --member serviceAccount:gocd-agent@devops-workshop-123.iam.gserviceaccount.com --role roles/container.admin
bindings:
- members:
  - serviceAccount:gocd-agent@devops-workshop-123.iam.gserviceaccount.com
  role: roles/container.clusterAdmin
- members:
  - serviceAccount:service-190704809516@container-engine-robot.iam.gserviceaccount.com
  role: roles/container.serviceAgent
- members:
  - serviceAccount:190704809516-compute@developer.gserviceaccount.com
  - serviceAccount:190704809516@cloudservices.gserviceaccount.com
  - serviceAccount:service-190704809516@containerregistry.iam.gserviceaccount.com
  role: roles/editor
- members:
  - user:dtsato@gmail.com
  role: roles/owner
etag: BwVp2RgXCis=
version: 1
```

These steps will destroy all resources we created during the workshop, but if
you want to also shut down your entire GCP "Devops Workshop" project, you can do
so through the Management Console, but going to the "IAM & admin" service,
choosing the "Settings" menu and clicking on "SHUT DOWN" button.
