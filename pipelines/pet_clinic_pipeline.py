#!/usr/bin/env python
from gomatic import *
import os, re

print "Updating PetClinic Pipeline..."
go_server_host = re.search('https?://([a-z0-9.\-._~%]+)', os.environ['GO_SERVER_URL']).group(1)
go_server_url = "%s:%s" % (go_server_host, "8153")
configurator = GoCdConfigurator(HostRestClient(go_server_url))
secret_variables = {'GCLOUD_SERVICE_KEY': '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'}
pipeline = configurator\
	.ensure_pipeline_group("sample")\
	.ensure_replacement_of_pipeline("PetClinic")\
	.set_git_material(GitMaterial("https://github.com/dtsato/devops-in-practice-workshop.git", branch="step-14", ignore_patterns=set(['pipelines/*'])))
stage = pipeline.ensure_stage("commit")
job = stage\
    .ensure_job("build-and-publish")\
    .ensure_artifacts({TestArtifact("target/surefire-reports", "surefire-reports")})\
    .ensure_environment_variables({'MAVEN_OPTS': '-Xmx1024m', 'GCLOUD_PROJECT_ID': 'devops-workshop-123'})\
    .ensure_encrypted_environment_variables(secret_variables)
job.set_elastic_profile_id('docker-jdk')
job.add_task(ExecTask(['./mvnw', 'clean', 'package']))
job.add_task(ExecTask(['bash', '-c', 'docker build --tag pet-app:$GO_PIPELINE_LABEL --build-arg JAR_FILE=target/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar .']))
job.add_task(ExecTask(['bash', '-c', 'docker login -u _json_key -p"$(echo $GCLOUD_SERVICE_KEY | base64 -d)" https://us.gcr.io']))
job.add_task(ExecTask(['bash', '-c', 'docker tag pet-app:$GO_PIPELINE_LABEL us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
job.add_task(ExecTask(['bash', '-c', 'docker push us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
stage = pipeline.ensure_stage("deploy")
job = stage\
    .ensure_job("deploy")\
    .ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-123', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})\
    .ensure_encrypted_environment_variables(secret_variables)
job.set_elastic_profile_id('kubectl')
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
