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

First, let's create the folder and a few dummy scripts for each of the pipelines,
to serve as placeholder test scripts:

```shell
$ mkdir pipelines
$ echo "print \"Updating Meta Pipeline...\"" > pipelines/meta_pipeline.py
$ echo "print \"Updating PetClinic Pipeline...\"" > pipelines/pet_clinic_pipeline.py
```

Let's update the current "PetClinic" pipeline configuration to not trigger when
changes occur to the `pipelines` folder. Click on the "ADMIN" menu and select
"Pipelines". Click on "Edit" for "PetClinc" pipeline and go to the "Materials"
tab. Opening the Git material, add the following configuration to the Blacklist:

* Paths to be excluded: `pipelines`

Now we can commit and push our changes to introduce the placeholder scripts and
it should not trigger a pipeline execution.
