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
	.set_git_material(GitMaterial("https://github.com/dtsato/devops-in-practice-workshop.git", branch="devops-west-18", ignore_patterns=set(['pipelines/*'])))
stage = pipeline.ensure_stage("commit")
job = stage\
    .ensure_job("build-and-publish")\
    .ensure_artifacts({TestArtifact("target/surefire-reports", "surefire-reports")})\
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

configurator.save_updated_config()
