#!/usr/bin/env python
from gomatic import *
import os, re

print "Updating PetClinic Pipeline..."
go_server_host = re.search('https?://([a-z0-9.\-._~%]+)', os.environ['GO_SERVER_URL']).group(1)
go_server_url = "%s:%s" % (go_server_host, "8153")
configurator = GoCdConfigurator(HostRestClient(go_server_url))
secret_variables = {'GCLOUD_SERVICE_KEY': 'ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAiZGV2b3BzLXdvcmtzaG9wLTEyMyIsCiAgInByaXZhdGVfa2V5X2lkIjogIjc1MWRhYzIyOGUxMDQ3MmM2Mzg0MWUwMWQ1MWZjN2E2NzRmN2I3M2MiLAogICJwcml2YXRlX2tleSI6ICItLS0tLUJFR0lOIFBSSVZBVEUgS0VZLS0tLS1cbk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRREg0WkVkV0JJZW85MHZcbklRNVNNSE9kTkwwQ0kzSHZqNjhZRlJTRktLUlVTUWxGeXk2UnNIZU5DeDY3dlVoaG52cHE5Ri9hcCtHU1Q5Zklcbk1vZVVGUG93ZTkvcmtHeUFLY3NZZFFxUkp1K3BPeHNKZngwdUMvdVFySWVTV0lFZjRmQm5IQTRBRkdqbGdkdklcbkIyNTg3Y0k3WHhBbmFiTngrMHdrZ3dJWGtTb1BLR0NwVENaR291bzZQdVovVWNpWTNlbWNYUWZZSDZEWk50bVRcbmxLNWdZcXZ2RUFtLzVwRmNOTmMweTJKVVVMbDIrVEN0bndJWVpBUUNLMkVlUTJORmlSRXZQZ29BeGN5UVM1Ym9cbkthcDROU1VLbU12NzAwaUo2N0U2cnNmdFB5amcxV1g3UkNGbW5jTzdES1pvWFMycWhKQlNGb0V2Y1I4Ung5K0lcbmVnVlpKNmc5QWdNQkFBRUNnZ0VBQlR2ZmJQcXllMjhVTDk0b1RlMGxzek1LRkUxV3pWY3JGbnVZMDdWMmUzR0ZcbkpyaktZYUlTdUtvQm9PNEtLdW82M3U3dFlxQkhseFAwVDhlZVJybWlPbitkT1FISllZckJTTVRwejZ3S3dGanRcbjhvLzJTam9oN25qTXZQK0lkQXdGRzVkcVkyOVFEREJ4Wk84UzRpa1IrZ21FSVZxOUg1U0h1czRHWnVwcGI1ejFcbnRHNWdUcXhZaUtzS0p5VmcvcXdOOGNKQTlSVWtvUm45Tk5KT3EyV0VQSlJJMFhaYjc1d2RBSkF3dDNSYk5GaXdcbnhzb2NkTFBoTDRrUTRtcUNwR0doSkN4czZGRVpoMjlmVUt4ckNybzJ5WjRZQStmeW0vV3doN0E3cGVwV2cyWkJcbmxMVGdPeFZ2N0V2U2ViWTMwc0dqdGg3UTNKLzhGa3lkWElNcFZvbGllUUtCZ1FEL2ZzdDh1cDExelpjckFKRTVcbjRqWDJiM2tpaUpXbEljSVBoUmNWTVBLZVRRU253M1dBNGxmcVpUNG0xa2hNczRGVVR0STl3bnVEVkR0bjBYdktcbkQwZHIwQ3N2a01RRjJKYnd5bjhJWktZQjFxdXNsQ0V6Q0NWdjZ1SXZzaFY2aWNrL0YwOTdrQkIrMHlVYUdZZDZcbi9NTW12YjNmbzRjUEoyK3Y2WGI3ZVpSY1ZRS0JnUURJUnFYTDcvSnR2eWJJZ2dxd21Bcm1JMGFyR0E0WTkvSHpcbjE0cXdvMGg2QlVUUm1JUXk4L1Q1dk9uRWNLSW5IZzhoK2d3eFV4eGU1MDdmN2hyM25xb2tHZ2cyVzBVd25aYnNcbjVMdXh0TEcwLzZoT3RPTkYxM1QwaW9YeVRLUzVyZXBOMnlYeW02bi9SSUc3U3luYWRvcHUzN0JjdGRHUXhqbmFcbnNoYzJVc2dFU1FLQmdRRGdUNi9UcC91S2E1K21qMjd4Uk50ZnF1ck5HT0ZaQTFSZlQ5ZStNU1V4T2lrMktQTEdcbjN2R1V4cUpVY3BrelRmM2p5UGZvWlJFUGNpcGRzWnRmQVI4UlZzZ3prSU9wSmtrT3lwblJBcHlFekxZWVpFenBcbmd1TnJhT3FBT1hlR0IrWjV6N3RtbmtyOUxkOUxGTkxQZFk3WU9vbXpDTjBRdnV6ZG9ybGxlNDUzcVFLQmdEaEdcbldhbi9SMEI5T0xtWWlNWnNRb3UrRjhwVm5RaDVDeHg0VVRrbStHT0kvWGhqZ2FvTGtLZG41TXZVMWt0bGo5ejlcbk5OWGJRNXFMSmtlWDBTNEpBRWZhcExvWlZVeSt5enpQWE1vbk90UGdEbnZuS2dGaTlETU9oV3E3RElJOEV4MURcbldkdGMwQnl4TkQ3YmRPdzA2TnNVc2FxclVESjg4SjY1OGZuS3N2YzVBb0dCQUwybVdrS01KaHIxK3ZhMWgvY0dcbnZvZ0xKcjh2dmtkVXA1b3RwVXhiYjJpdmxvTG1BOGhOdEZHQjk3M0lOM3dRVVVOR3NpSFRNOFVqTjB3bHdlek9cblhDV0VXUHRGOHo5SHcrSER0aDcwYUU3b080UGpLb2lTSEs4WkkyYWVsQjdPN2tVTWFjOWZsam1ZSTRkRWJXaEJcblR0YWRvSXM4OW5ReEtIZVExeVhBYktTMVxuLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLVxuIiwKICAiY2xpZW50X2VtYWlsIjogImdvY2QtYWdlbnRAZGV2b3BzLXdvcmtzaG9wLTEyMy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgImNsaWVudF9pZCI6ICIxMTE3NjUxMDMxMTczNjA3NDE1NjIiLAogICJhdXRoX3VyaSI6ICJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20vby9vYXV0aDIvYXV0aCIsCiAgInRva2VuX3VyaSI6ICJodHRwczovL29hdXRoMi5nb29nbGVhcGlzLmNvbS90b2tlbiIsCiAgImF1dGhfcHJvdmlkZXJfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9vYXV0aDIvdjEvY2VydHMiLAogICJjbGllbnRfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9yb2JvdC92MS9tZXRhZGF0YS94NTA5L2dvY2QtYWdlbnQlNDBkZXZvcHMtd29ya3Nob3AtMTIzLmlhbS5nc2VydmljZWFjY291bnQuY29tIgp9Cg=='}
pipeline = configurator\
	.ensure_pipeline_group("sample")\
	.ensure_replacement_of_pipeline("PetClinic")\
	.set_git_material(GitMaterial("https://github.com/dtsato/devops-in-practice-workshop.git", branch="devops-west-18", ignore_patterns=set(['pipelines/*'])))
stage = pipeline.ensure_stage("commit")
job = stage\
    .ensure_job("build-and-publish")\
    .ensure_artifacts({BuildArtifact("target/surefire-reports", "surefire-reports")})\
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
