#!/usr/bin/env python
from gomatic import *
import os, re

print "Updating PetClinic Pipeline..."
go_server_host = re.search('https?://([a-z0-9.\-._~%]+)', os.environ['GO_SERVER_URL']).group(1)
go_server_url = "%s:%s" % (go_server_host, "8153")
configurator = GoCdConfigurator(HostRestClient(go_server_url))
secret_variables = {'GCLOUD_SERVICE_KEY': 'lKD+DoKDGtCsaToW/dLf+0IbaGDvD9WR1P8fk72BceCeKNPtxxDzUwZHEw+HyawKCxplxh0jZ61BQYia6u6NcK+lZJjnIDzCFYyEgbWGzH4ZZGt50Ycj6URgMJmfGzvlJ2f5jOuv078vnomsul3vU5zS9o1H77QDBpYMjPK5OMGa7v5Rye6lnG/oiYA6HKs/0N0EAg1jK+OjMgIlEXNyb5PRoPg0/hQQ1PfDyBgOK4yA+kD5T5y3n/lXKzto8DNxFXlGRdsg15RYdGI+lsotcrUIP8RVBuVPS8rnfuGSmHpNAYwjdwzAvL3g3Eh8VwLy9JxydVRgYDa3iNV7qPOFT4qArqCoIcTYhojB1M9y9M38OecMIJoZlfbvUifS7OdndB2wHdE8B+SGN1slxVXJfmtklglCWpGFPu2uhS61KPKaz5ir+Jc6V8bENW/bRo3jMi6ZwRq7zpV1aP1jVbRb3Ttr8TpsZEsf8MXmbtMf2M3ptmMbg5zxIgF/nfBkN1nsnh1XwDIKEYoNiJsqKHd7ue6ncTc/BXY9q/75g5sFPUF/ehDbJ/N3Xu7Nk/8yCKLjSYIKxEX56lOopmuobN9LFrC/RbKde5/jCqyl6Ms6kDy4swPW8hy+BIFbcjYbRsNyWjzWlqOoQ537ScoRk5aZBnE04bqks/iCz0GRm5yKmciQU2V3dEfMdW1OUUzVZ3KYl/IUxK4e5rwG/kl5ln3QN9neSAImjWMKxBqRSL22g2et1xYuFiU421PnQD2DGFL6llgJwfj5iWghBWHIJzQkuodE/AoFf3nkin9K+y2WMTrAPhs/Xh2PM4nKmWnU/mJJZcP0xt76iDQiEbzOfg2TwC9WgvFkUQY0xg0Z0EhuCIpda9/IPRZOLQkmJjJ6enUwbB6BykI3I1EiYL7I2MecDEfE1ONE3ImSWaSth8DtysdUAT6dKOEeMQYltM/5m3nEtiK5/fcEXB0dwicoPD5p5Yq60p+098Ku09P2AzI3de7Pj+5QriS37uuYXAHfQHLdzvpc2MAGm/NOXa15LLvY6dmlIVA9BdpSXOKwipctJSAMnwkVwT04NgYzFaKGnZ8CnhUhgbdks52B9EUHPSoT/TMvXsEJrSIC0B5+AJgXBYw0S3vAh/nh1G4DzQ7EnZ3mKCegeatC9otthspFH8Ob8O1cvs72ccO+Abwy0sfr23CIOPdimM38S/pyN1noQcRldogJG+Wa0l/xlw4YToWjlRqpWf7w7+r+tIUkVpXoPMXjG1e1kIUQCZdq6GU/assGIctNxoKyDfvDQpZ9rmupP6IF41fhgSRDVudCzXXZGGvUZcIZ6TyERcZ5VTHAGl1dfzBNxoYkAMhHvR7dOgyTe5JEzcsYD6nTueatj8YDhg+iXk+sfm053h1eDERydMME1D4l/vwrA3mH+mr2v1pLK993/HXbH3QGPi1nwgvB+JFjq+r2WiGd5y0WaYMRIKjbeqC/NbWLGiSJ27pmxK8LmvXUilIYEvtmmbEmXfR5agC2z0e0yyMb1Ik7jKj5HqYqx5gzzpIQdCE73OXfopAqbrLUNQZIVEAL3cCAvS7QE3MXa3dppeN97o35c7JC8LDXlr5C002oPwDYYY0NHMfCtQ9R0Hq6FaSaN5EXNhCYcE2VSK82CFPktKAueY9V/qeV7HMZQ//DvUrGzQsAc7vQYC1hRe0vmH1P4uHVW4zCamgwkU9KJrR95VwlfCjc7n/hWxBj7l/Mh3C/yo4V6XoWrPb2rBOiFjeXUcmVbvJV6ss5so3DheG9ggaz3zJeJVOFjehTkh7a8/2MbXpeRy95Va6CeU4/vCmdZgplO0EmYQdx60VvHqnq0mmwm4h96575lMmkhodKBBGqsqmb8k2tU2UUa1h3vG88urzwkhDvixnRcN79GYyTGjqj33BEfl47SqfB4CNZLMAaGjmd+NnA/v/EITtMPpLmwDzU2ZajpZF/mRmLnLnrT+NIZmVq7t+oQv73r3pXgBquqwHItIsFfyKwzwSyBuz/xzajjybDo2+OMTSeAMhvwMdkLnng0pYDnNLlEFiYot0zx9JGe+jGcFgebfqSFoRJyNVN6oxTL/ptJrbY9KawYaJi/NnAgqly4Mmxtj583l5rIv4Xe3PmbJInDy3+D+qO5d8MnOPpJprMRZYZ818xu3U2+PlVeq4kFqMSpXeOS4lyZzj2O5C59gozFozAPZrSVhCAlZ8oq3mfQyPYaUjvTQcQjt+Occh0giczGKexc/78aBSzu9ICG0IuqWMAR/8o9JcQbXgvLyH9W5ZisayzQS+/AARb2uBFIdmpoBchFN/nGcLgx1/zfPdjXQ6+V59lvwr6sXiST0u/Jp4TGq/L87/SkUrKTFxu/zVQynjMMA1x9+gfnfjaaXkNFqvWWCRdpOlzxCei83x+Tlv47swZQaVTSJVrjg9agBGLR43tLRr31yL0d/K87y8LIJy+TMjyGaCdzwwodRuYRQpIYrl1atPpQfey495stNI2YZ6eOI0Eodpon8nPjbKNlioNMmi6YyBMgY60clDBjoiev5lYKjPBRTAkjMDHdlSetaQKqH47ITh648mYUK9+1sSXaGXxkkrR0IKmPmU4R3dKka1wWYInf+11DfBA89RJD+w7rZOkeFguLDY7nVhvFCHnnj5gYBPEBFwV9xfHPOa3t0H/BOfScrm9U4/F0PFjhBDow05JbSb3OpmUKgQ+BBB4m/9w7pUeFHhPwq3CXTVrsgw3jlGR6lSsGPbQ/OMg8T6UIrnMJPYNFFwyzc+Njyv3bkxLuY9fiEC0SLw61DOoyo8URKp0EQ9neNEF6W2HTrkbfh7esLTBpBURoJ6V7SL1euUEzhVbqsQibYcVDpk5WtSuztTlZrKkfIVgxyJAFTeQY+wddxkZrdjP4NBkO3qzk9Vk9hVWQ4wmnyV5PjJGmL4CSgh6Wy0FAe35ybUE3vHektL25nJXGkKEk5XJv+BjrDcQPxWKqjUvp2XrJfwpRv7rEbkuVVImtJLAqSckWKwz1TCX7yIozTVhgK32m1Q2TzgwFJ/kH8O9pkhKefLodNVVHhdGGTVkd/HOVCaO5rOdNLjlSVmqodvGj3LlEwMtAhj4nnEhmb0+2uItF7iOyfESPq1TRUohhSNGquMzF2SfQdU9gRiS3QaUw2PiXd1vAu1cRsGyz86mUqc4j+hZxU7Uzsinsmd6asOeUD17q5YzDxW8Z6cYy5MvGv1oCMRlMi25Z1uNLh5AUlCfaC669XXfcgOXiv31Cj18xRjBEDixlZdbkzbrKerK+mv8rqH3H+Ba4fOnGib8X7AZ81fSJhnGFwwLtKmbuhR+ktl3YGTcL4NQByGV4x7FR89cxbHbXpxhjr00RZyhjrQO0Zkzudm7yRSvV3+yhX1+8f3ksOAuxRGhh3NIf4SJqMU/fknBwqHoebpV4bxp8oaBVXRuFndYwAPWbpFVSAj7NOD7KOW9rsWtSIghSi8w0lBlZ1/2PBEaGWBR7rjYkiGWyO0jhSSI6Te2WFes7PJgAizwIWWyPsVk9xcfpyAg5JHkCoYz7c+qREJaRbdTH+zjwuSFhHEx2v5JVKVb7stHS6RuoniXdVie56h4QXe0zEg8+w3ousNn8/KR65TaxwWp1Ogih10ttTA2x0A+FwzUnSRD+sVzzYjWw678s0HeoB04jF0/Rcr84EjD3UvHmC9JaL/U09DlDwJm7RgxmAfo5EdyZahVB0tPzSHBPmrAv1VXSFrbk7vWPXrnDMtsJ7OqpBGOmf/3UyTvxoxo6cVJFA7Dwx84yBH0NDzgNKnFq5GHk+nxiVKsduZc1c55UNhhpO+/5o/b2BwfaILXyf9vi5rGeXXEwENCRtqb++2ijWIVr63ihcaPB/7U7n6BROmLEIwEmmEQJA8DmA/IUzrdOr00pcj8M3oBV5qA7WW/RO1IKNZzCJ6OnHzXSwlH29DA7FaqwVA+cKHW3vVCZtIyDEwLI1fCg0ZKS0kwj4j2lvvoOuvt2PhB+Uw1rhAwqz53Jc0CmXO0eZNnFQkIGYCLNA9U1lZYU2wdw2dSsuPtqc5p8/5xuBkuIBNt8/QiQYBrOiNxn36yMh4JI4s/a2KZC5NvGYmjOdZxSRV3ejEY06mHSWDSddx6+aLnN3ojEAseG5MjStI2FmvnMYLVxZzUjdesUg9kAwwWYp7FeWttdA=='}
pipeline = configurator\
	.ensure_pipeline_group("defaultGroup")\
	.ensure_replacement_of_pipeline("PetClinic")\
	.set_git_material(GitMaterial("https://github.com/dtsato/devops-in-practice-workshop.git", branch="step-13", ignore_patterns=set(['pipelines/*'])))
stage = pipeline.ensure_stage("commit")
job = stage\
    .ensure_job("build-and-publish")\
    .ensure_artifacts({TestArtifact("target/surefire-reports", "surefire-reports")})\
    .ensure_environment_variables({'MAVEN_OPTS': '-Xmx1024m', 'GCLOUD_PROJECT_ID': 'devops-workshop-201010'})\
    .ensure_encrypted_environment_variables(secret_variables)
job.set_elastic_profile_id('docker')
job.add_task(ExecTask(['./mvnw', 'clean', 'package']))
job.add_task(ExecTask(['bash', '-c', 'docker build --tag pet-app:$GO_PIPELINE_LABEL --build-arg JAR_FILE=target/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar .']))
job.add_task(ExecTask(['bash', '-c', 'docker login -u _json_key -p"$(echo $GCLOUD_SERVICE_KEY | base64 -d)" https://us.gcr.io']))
job.add_task(ExecTask(['bash', '-c', 'docker tag pet-app:$GO_PIPELINE_LABEL us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
job.add_task(ExecTask(['bash', '-c', 'docker push us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
stage = pipeline.ensure_stage("deploy")
job = stage\
    .ensure_job("deploy")\
    .ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-201010', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})\
    .ensure_encrypted_environment_variables(secret_variables)
job.set_elastic_profile_id('docker-kubectl')
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './deploy.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))

configurator.save_updated_config()
