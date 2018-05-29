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
	.set_git_material(GitMaterial("https://github.com/dtsato/devops-in-practice-workshop.git", branch="step-13", ignore_patterns=set(['pipelines/*'])))
stage = pipeline.ensure_stage("commit")
job = stage.ensure_job("build-and-publish")\
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
job = stage.ensure_job("deploy")\
    .ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-123', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})\
    .ensure_encrypted_environment_variables(secret_variables)\
    .set_elastic_profile_id("kubectl")
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './deploy.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))

configurator.save_updated_config()
