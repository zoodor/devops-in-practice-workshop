#!/usr/bin/env python
from gomatic import *
import os, re

print "Updating PetClinic Pipeline..."

go_server_host = re.search('https?://([a-z0-9.\-._~%]+)', os.environ['GO_SERVER_URL']).group(1)
go_server_url = "%s:%s" % (go_server_host, "8153")
configurator = GoCdConfigurator(HostRestClient(go_server_url))
pipeline = configurator\
	.ensure_pipeline_group("sample")\
	.ensure_replacement_of_pipeline("PetClinic")\
	.set_git_material(GitMaterial("https://github.com/dtsato/devops-in-practice-workshop.git", branch="devops-east-18", ignore_patterns=set(['pipelines/*'])))
secret_variables = {'GCLOUD_SERVICE_KEY': 'AES:tm5lGAE1kRl+LeSVvMgEGw==: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'}
stage = pipeline.ensure_stage("commit")
job = stage.ensure_job("build-and-publish").ensure_environment_variables({'MAVEN_OPTS': '-Xmx1024m', 'GCLOUD_PROJECT_ID': 'devops-workshop-123'}).ensure_encrypted_environment_variables(secret_variables).set_elastic_profile_id("docker-jdk")
job.add_task(ExecTask(['./mvnw', 'clean package']))
job.add_task(ExecTask(['bash', '-c', 'docker build --tag pet-app:$GO_PIPELINE_LABEL --build-arg JAR_FILE=target/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar .']))
job.add_task(ExecTask(['bash', '-c', 'docker login -u _json_key -p"$(echo $GCLOUD_SERVICE_KEY | base64 -d)" https://us.gcr.io']))
job.add_task(ExecTask(['bash', '-c', 'docker tag pet-app:$GO_PIPELINE_LABEL us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
job.add_task(ExecTask(['bash', '-c', 'docker push us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
stage = pipeline.ensure_stage("deploy")
job = stage.ensure_job("deploy").ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-123', 'GCLOUD_CLUSTER': 'devops-workshop-gke'}).ensure_encrypted_environment_variables(secret_variables).set_elastic_profile_id("kubectl")
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './deploy.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))
stage = pipeline.ensure_stage("approve-canary")
stage.set_has_manual_approval()
job = stage\
	.ensure_job("complete-canary")\
    .ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-123', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})\
    .ensure_encrypted_environment_variables(secret_variables)
job.set_elastic_profile_id('kubectl')
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './complete-canary.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))

configurator.save_updated_config()
