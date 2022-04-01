# Deploy a python package on GCP using poetry

## Todo
- [ ] Check if pyenv was the mistake (create a new python env using pyenv and redo the steps that made it work)
- [ ] Again install the global version of poetry 
- [ ] Try to replicate it with the newwest version of poetry

## Prerequsities

1. [Install](https://cloud.google.com/sdk/docs/install-sdk) the gcloud CLI 
2. Enable `Artifact Registry API` (in the [GCP console](https://console.cloud.google.com/))

## Steps to deploy a package on GCP using poetry and test it

1. Create an artifact repo on GCP (either by using gcloud or the [GCP console](https://console.cloud.google.com/))
```
gcloud artifacts repositories create REPOSITORY \
     --repository-format=FORMAT \
     [--location=LOCATION] \
     [--description="DESCRIPTION"] \
     [--kms-key=KMS-KEY] \
     [--async] \
```

Lets first go through the individual arguments and the specific values I set:

- `REPOSITORY`
    - info: arbitrary repository name
    - value: `artifact-repo`
- `FORMAT`
    - info: format of the repository ([view](https://cloud.google.com/artifact-registry/docs/repositories/create-repos#repo-formats)view the list of possible values)
    - value: `python` (since we wish to deploy a python package)
    

- `LOCATION`
    - info: regional or multi-regional location for the repository
    - view a list of supported location by: `gcloud artifacts locations list`
    - value: `europe-west1`
- `DESCRIPTION`
    - info: arbitrary description of the repo (do not include sensitive data)

- `KMS-KEY`


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
