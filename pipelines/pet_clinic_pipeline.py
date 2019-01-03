#!/usr/bin/env python
from gomatic import *
import os, re

print "Updating PetClinic Pipeline..."
go_server_host = re.search('https?://([a-z0-9.\-._~%]+)', os.environ['GO_SERVER_URL']).group(1)
go_server_url = "%s:%s" % (go_server_host, "8153")
configurator = GoCdConfigurator(HostRestClient(go_server_url))
secret_variables = {'GCLOUD_SERVICE_KEY': 'AES:BgBbXz2ZD0XRDKnuuYyA0w==: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'}
pipeline = configurator\
	.ensure_pipeline_group("sample")\
	.ensure_replacement_of_pipeline("PetClinic")\
	.set_git_material(GitMaterial("https://github.com/zoodor/devops-in-practice-workshop.git", ignore_patterns=set(['pipelines/*']))).ensure_environment_variables({'GCLOUD_PROJECT_ID': 'devops-workshop-112233'}).ensure_encrypted_environment_variables(secret_variables)
stage = pipeline.ensure_stage("commit")
job = stage.ensure_job("build-and-publish").ensure_environment_variables({'MAVEN_OPTS': '-Xmx1024m'}).set_elastic_profile_id("docker-jdk")
job.add_task(ExecTask(['./mvnw', 'clean package']))
job.add_task(ExecTask(['bash', '-c', 'docker build --tag pet-app:$GO_PIPELINE_LABEL --build-arg JAR_FILE=target/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar .']))
job.add_task(ExecTask(['bash', '-c', 'docker login -u _json_key -p"$(echo $GCLOUD_SERVICE_KEY | base64 -d)" https://us.gcr.io']))
job.add_task(ExecTask(['bash', '-c', 'docker tag pet-app:$GO_PIPELINE_LABEL us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
job.add_task(ExecTask(['bash', '-c', 'docker push us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
stage = pipeline.ensure_stage("deploy").ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})
job = stage.ensure_job("deploy").set_elastic_profile_id("kubectl")
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './deploy.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))
stage = pipeline.ensure_stage("approve-canary")
stage.set_has_manual_approval()
job = stage\
    .ensure_job("complete-canary")\
    .ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})
job.set_elastic_profile_id('kubectl')
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './complete-canary.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))

configurator.save_updated_config()