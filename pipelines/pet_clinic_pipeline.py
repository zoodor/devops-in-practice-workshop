#!/usr/bin/env python
from gomatic import *
import os, re

print "Updating PetClinic Pipeline..."
go_server_host = re.search('https?://([a-z0-9.\-._~%]+)', os.environ['GO_SERVER_URL']).group(1)
go_server_url = "%s:%s" % (go_server_host, "8153")
configurator = GoCdConfigurator(HostRestClient(go_server_url))
secret_variables = {'GCLOUD_SERVICE_KEY': 'AES:HTydN74xQhePzSdpaJw8lA==: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'}
pipeline = configurator\
	.ensure_pipeline_group("sample")\
	.ensure_replacement_of_pipeline("PetClinic")\
	.set_git_material(GitMaterial("https://github.com/dtsato/devops-in-practice-workshop.git", branch="devops-west-18", ignore_patterns=set(['pipelines/*'])))
stage = pipeline.ensure_stage("commit")
job = stage\
    .ensure_job("build-and-publish")\
    .ensure_environment_variables({'MAVEN_OPTS': '-Xmx1024m', 'GCLOUD_PROJECT_ID': 'devops-workshop-123'})\
    .ensure_encrypted_environment_variables(secret_variables)\
    .set_elastic_profile_id("docker-jdk")
job.add_task(ExecTask(['./mvnw', 'clean package']))
job.add_task(ExecTask(['bash', '-c', 'docker build --tag pet-app:$GO_PIPELINE_LABEL --build-arg JAR_FILE=target/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar .']))
job.add_task(ExecTask(['bash', '-c', 'docker login -u _json_key -p"$(echo $GCLOUD_SERVICE_KEY | base64 -d)" https://us.gcr.io']))
job.add_task(ExecTask(['bash', '-c', 'docker tag pet-app:$GO_PIPELINE_LABEL us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
job.add_task(ExecTask(['bash', '-c', 'docker push us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
stage = pipeline.ensure_stage("deploy")
job = stage\
    .ensure_job("deploy")\
    .ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-123', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})\
    .ensure_encrypted_environment_variables(secret_variables)\
    .set_elastic_profile_id("kubectl")
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
