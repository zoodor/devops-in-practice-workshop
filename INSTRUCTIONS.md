# Exercise 13 - Pipeline as Code

## Goals

* Learn about Pipeline as Code
* Learn about GoMatic
* Create a new pipeline for updating GoCD pipelines

## Acceptance Criteria

* Pipeline code should be placed under a new `pipelines` folder at the root of
the project
* Configure a new Elastic Agent Profile that can execute `python` scripts
* Exclude the `pipelines` folder as a trigger to the "PetClinic" pipeline
* Create a new "Meta" pipeline triggered on changes to the `pipelines` folder
only, that executes the python scripts using GoMatic
* Use GoMatic locally to export the current pipeline configurations and convert
them into pipeline scripts

## Step by Step Instructions

### Creating placeholder scripts

First, let's create the folder and a few dummy scripts for each of the pipelines,
to serve as placeholder test scripts:

```shell
$ mkdir pipelines
$ echo "print \"Updating Meta Pipeline...\"" > pipelines/meta_pipeline.py
$ echo "print \"Updating PetClinic Pipeline...\"" > pipelines/pet_clinic_pipeline.py
```

Let's also create a `pipelines/update.sh` script that will be executed by the
meta pipeline to invoke the dummy scripts inside a Docker container with
Python and GoMatic:

```bash
#!/bin/bash
set -xe

CWD=$(cd $(dirname $0) && pwd)
for pipeline in $CWD/*.py; do
  docker run -it --rm -v "$CWD":/usr/src/meta -w /usr/src/meta python:2.7-slim /bin/bash -c "pip install gomatic && python $(basename $pipeline)"
done
```

Make sure the new script is executable:

```shell
$ chmod a+x pipelines/update.sh
```

Now let's update the current "PetClinic" pipeline configuration to not trigger
when changes occur to the `pipelines` folder. Click on the "ADMIN" menu and select
"Pipelines". Click on "Edit" for "PetClinc" pipeline and go to the "Materials"
tab. Opening the Git material, add the following configuration to the Blacklist:

* Paths to be excluded: `pipelines`

Now we can commit and push our changes to introduce the placeholder scripts and
it should not trigger a pipeline execution.

### Creating the meta pipeline

From the "ADMIN" menu, select "Pipelines", and click on "Create a new pipeline
within this group". The first step will setup the pipeline name to "Meta" and
click "NEXT". Then on the next step, use the following configuration:

* Material Type: `Git`
* URL: Same as before, use the Git URL for your repository
* Branch: `master`
* Blacklist: `pipelines`
* Invert the file filter: Checked

Once again, you can test by clicking on "CHECK CONNECTION" before proceeding with
clicking "NEXT". In the final step, use the following configuration:

* Stage Name: `update-pipelines`
* Job Name: `update-pipelines`
* Task Type: `More...`
* Command: `pipelines/update.sh`

We can then click on "FINISH". We can now unpause the pipeline and test that it
runs successfully.
