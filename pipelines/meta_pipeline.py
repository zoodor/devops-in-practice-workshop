#!/usr/bin/env python
from gomatic import *
import os, re

print "Updating Meta Pipeline..."

go_server_host = re.search('https?://([a-z0-9.\-._~%]+)', os.environ['GO_SERVER_URL']).group(1)
go_server_url = "%s:%s" % (go_server_host, "8153")
configurator = GoCdConfigurator(HostRestClient(go_server_url))
pipeline = configurator\
	.ensure_pipeline_group("defaultGroup")\
	.ensure_replacement_of_pipeline("Meta")\
	.set_git_material(GitMaterial("https://github.com/dtsato/devops-in-practice-workshop.git", branch="step-13", ignore_patterns=set(['pipelines/*'])))
stage = pipeline.ensure_stage("update-pipelines")
job = stage.ensure_job("update-pipelines")
job.add_task(ExecTask(['pipelines/update.sh']))

configurator.save_updated_config()
