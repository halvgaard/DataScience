# ZenML pipeline downloading data from BQ in one step and running a zenML pipeline in Vertex AI pipelines

## Notes
In the folder you will find two python scripts: `pipeline.py` and `run.py`, `pipeline.py` showcases how to download data from BQ in zenML pipeline and 
`run.py` is used to run another zenML pipeline (mnist) remotely in `Vertex AI` pipelines. The reasons for that is, that so far you can run only pipelines
that contain python modules installable with `zenml integration install <package>` (list of packages is [here](https://docs.zenml.io/features/integrations)).
And since to download data from `BigQuery` I used the recommended `pandas_gbq` (not included in zenML integrations) it fails when submitting the job to 
`Vertex AI` (because zenML defined an image where they install only their integrated packages).

Correction:
That is true by default, but when you are registering a new step-operator you can define your custom base image `--base_image=<CUSTOM_BASE_IMAGE>` 
for creating an environment to run your jobs on Vertex AI. (so you can download any packages you need, not only the ones included by default).

## ZenML pipeline downloading data from BigQuery

Please view `pipeline.py` for a description on how to do it.

## Running ZenML pipeline in Vertex AI pipelines

### 1. Configure your GCP project

1.1. `gcloud cli` set up
Make sure you are in the correct project `gcloud config list`

1.2. Make sure you have the right permissions to create and manage Vertex AI custom jobs.

Create a service account
```
gcloud iam service-accounts create NAME

#EXAMPLE
gcloud iam service-accounts create zenml-sa
```
Grant roles to the service account
```
gcloud projects add-iam-policy-binding <PROJECT_ID> --member="serviceAccount:<SA-NAME>@<PROJECT_ID>.iam.gserviceaccount.com" --role=<ROLE>

#EXAMPLE
gcloud projects add-iam-policy-binding zenml-vertex-ai --member="serviceAccount:zenml-sa@zenml-vertex-ai.iam.gserviceaccount.com" --role=roles/storage.admin
gcloud projects add-iam-policy-binding zenml-vertex-ai --member="serviceAccount:zenml-sa@zenml-vertex-ai.iam.gserviceaccount.com" --role=roles/aiplatform.admin
```
Generate the key file (it generates in the same location)
```
gcloud iam service-accounts keys create <FILE-NAME>.json --iam-account=<SA-NAME>@<PROJECT_ID>.iam.gserviceaccount.com

EXAMPLE
gcloud iam service-accounts keys create zenml-sa-file.json --iam-account=zenml-sa@zenml-vertex-ai.iam.gserviceaccount.com
```
Set the environment variable 
- To use service accounts with the Google Cloud CLI, you need to set an environment variable where your code runs
```
export GOOGLE_APPLICATION_CREDENTIALS=<KEY-FILE-LOCATION>

#EXAMPLE
export GOOGLE_APPLICATION_CREDENTIALS="/Users/co2yd4bcjgh6/Library/CloudStorage/OneDrive-Personal/myWorkspace/github/DataScience/Task8/zenml-sa-file.json"
```
1.3. Create a `GCP bucket` to which Vertex should output any artifacts from the training run
```
gsutil mb -l <REGION> gs://bucket-name

#EXAMPLE
gsutil mb -l europe-west1 gs://zenml-bucket
```

1.4. Configure and enable container registry in GCP

This registry will be used by ZenML to push your job images that Vertex will use.

a) [Enable](https://cloud.google.com/container-registry/docs) Container Registry
b) [Authenticate](https://cloud.google.com/container-registry/docs/advanced-authentication) your local `docker` cli with your GCP container registry 

```
docker pull busybox
docker tag busybox gcr.io/<PROJECT-ID/busybox
docker push gcr.io/<PROJECT-ID>/busybox
```
You can view this image in the gcp console (container registry) or by running
```
gcloud container images list-tags gcr.io/<PROJECT-ID>/busybox
```

1.5. [Enable](https://console.cloud.google.com/marketplace/product/google/aiplatform.googleapis.com?q=search&referrer=search&project=cloudguru-test-project) `Vertex AI API`

### 2. Set up the components requiered for your stack
2.1. Install integrations
```
zenml integration install sklearn vertex gcp

# Initialize
zenml init
```
2.2. Set the bucket created earlier
```
zenml artifact-store register <NAME> --type=gcp --path=<GCS_BUCKET_PATH>

# EXAMPLE
zenml artifact-store register gcp-store --type=gcp --path=gs://zenml-bucket
```
2.3. Create the vertex step operator
```
zenml step-operator register <NAME> \
    --type=vertex \
    --project=<PROJECT-ID> \
    --region=<REGION> \
    --machine_type=<MACHINE-TYPE> \
    --base_image=<CUSTOM_BASE_IMAGE> #this can be left out if you wish to use zenml's default image

# EXAMPLE
zenml step-operator register vertex \
    --type=vertex \
    --project=zenml-vertex-ai \
    --region=europe-west1 \
    --machine_type=n1-standard-4 \
```
List of available machines is [here](https://cloud.google.com/vertex-ai/docs/training/configure-compute#machine-types)

2.4. Register the container registry
```
zenml container-registry register <NAME> --type=default --uri=gcr.io/<PROJECT-ID>/<IMAGE>

#EXAMPLE
zenml container-registry register gcr_registry --type=default --uri=gcr.io/zenml-vertex-ai/busybox
```
2.5. Register the gcp stack (change names accordingly)
```
zenml stack register vertex_training_stack \
    -m default \
    -o default \
    -c gcr_registry \
    -a gcs-store \
    -s vertex
```
View all your stacks `zenml stack list`

2.6. Activate the stack
```
zenml stack set vertex_training_stack
```

Finally execute the script
```
python run.py --step_operator vertex
```
You can view the artifacts from the run in your gcp bucket.

## Useful links
https://docs.zenml.io/features/step-operators

https://docs.zenml.io/features/guide-aws-gcp-azure

https://cloud.google.com/docs/authentication/getting-started#create-service-account-gcloud

https://apidocs.zenml.io/0.7.3/cli/

https://blog.zenml.io/step-operators-training/
