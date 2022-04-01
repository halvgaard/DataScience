# Deploy a python package on GCP using poetry

## Todo
- [ ] Check if pyenv was the mistake (create a new python env using pyenv and redo the steps that made it work)
- [ ] Again install the global version of poetry 
- [ ] Try to replicate it with the newwest version of poetry

## Prerequsities

1. [Install](https://cloud.google.com/sdk/docs/install-sdk) the gcloud CLI 
2. Enable `Artifact Registry API` (in the [GCP console](https://console.cloud.google.com/))

## Steps to deploy a package on GCP using poetry and test it

1. Create artifact repo on GCP (either by using gcloud or the console)
```
gcloud artifacts repositories create REPOSITORY \
     --repository-format=FORMAT \
     [--location=LOCATION] \
     [--description="DESCRIPTION"] \
     [--kms-key=KMS-KEY] \
     [--async] \
```


View details
```
gcloud artifacts print-settings python \
    --project=computas-project-345810 \
    --repository=artifact-repo \
    --location=europe-west1
```

2. Create virtual env
3. pip install poetry
4. pip install the google key shit
5. poetry config 
gcloud auth login
gcloud auth application-default login
