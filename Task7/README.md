# BigQuery for data processing and EDA + Training a regressor using Vertex AI to predict CLV

## Disclaimer

All the commands and info is directly taken from [google's qwiklab](https://www.qwiklabs.com/focuses/18940?parent=catalog). The additional value of this tutorial is to showcase how to reproduce the qwiklab results in your personal `google project` locally in your `jupyter notebook`.

## Overview

You will use BigQuery for data processing and exploratory data analysis and the Vertex AI platform to train and deploy a custom TensorFlow Regressor model to predict customer lifetime value. The goal is to introduce yourself to `Vertex AI` through a high value real world use case - predictive CLV. You will start with a local `BigQuery` and `TensorFlow` workflow that you may already be familiar with and progress toward training and deploying your model in the cloud with `Vertex AI`.

 ## Learning Objectives
 
 - Query data from BigQuery into your jupyter notebook and do EDA
 - Make a simple baseline model 
 - Train a TensorFlow Regressor locally and plot the decreasing loss
 - Create a tabular dataset from the BigQuery data source
 - Containerize your model training code and upload it to `GCP Artifact Registry`
 - Load the deployed model and create a `Vertex AI Endpoint` for online predictions

### Dataset and util functions

The dataset comes from [UCI](https://archive.ics.uci.edu/ml/datasets/online+retail). The cloned repo (from the official tutorial) provided some util functions:
  - `vertex-ai-qwikstart/utils/data_download.py`
      - This script is very useful and can be generally used in other projects as well. Mainly two functions come quite handy: `download_url2gcs()` that downloads a dataset from given `url` and uploads it to a `google cloud storage bucket` and `upload_gcs2bq()` that uploads the dataset from the `GCS bucket` into `BigQuery` (also some data cleaning takes place in this script) 

Usage (not necessary to run since all the commands are provided in the jupyter notebook itself):
```
python utils/data_download.py \
  --PROJECT_ID={PROJECT_ID} \
  --GCS_BUCKET={GCS_BUCKET} \
  --BQ_RAW_TABLE_NAME={BQ_RAW_TABLE_NAME} \
  --BQ_CLEAN_TABLE_NAME={BQ_CLEAN_TABLE_NAME} \
  --BQ_ML_TABLE_NAME={BQ_ML_TABLE_NAME} \
  --URL="https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online Retail.xlsx"
```

## Prerequsities

1. [Install](https://cloud.google.com/sdk/docs/install-sdk) the gcloud CLI 
2. Create a new project in the [GCP console](https://console.cloud.google.com)

## Steps

### 1. Create and activate a new environment
```
pyenv virtualenv 3.7.9 vertex-ai
pyenv global vertex-ai
```

If you have issues running your jupyter notebook in the new environment use the following:

How do I know if I am running my jupyter notebook in the new environment?

```
import sys
print(sys.executable) # This path should point to the correct python in the new environment
```
e.g.: `/.pyenv/versions/vertex-ai/bin/python`

If it doesn't you won't be able to import the packages that you install in the next step.
To fix it run:

```
pip install ipykernel  
python -m ipykernel install --user
```

Now when you run `jupyter notebook` (inside the environment) the python kernel should be set correctly.

### 2. Install dependencies
I added some packages that were not originally included so you can run the jupyter notebook locally.

```
pip install -U -r requirements.txt
```

