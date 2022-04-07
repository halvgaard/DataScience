# BigQuery for data processing and EDA and training a regressor using Vertex AI to predict CLV

## Disclaimer

All the commands and info is directly taken from [google's qwiklab](https://www.qwiklabs.com/focuses/18940?parent=catalog). The additional value of this tutorial is to showcase how to reproduce the qwiklab results in your personal google project locally in your jupyter notebook.

## Overview

You will use BigQuery for data processing and exploratory data analysis and the Vertex AI platform to train and deploy a custom TensorFlow Regressor model to predict customer lifetime value. The goal of the is to introduce yourself to Vertex AI through a high value real world use case - predictive CLV. You will start with a local BigQuery and TensorFlow workflow that you may already be familiar with and progress toward training and deploying your model in the cloud with Vertex AI.

 ## Learning Objectives
 
 - Query data from BigQuery into your jupyter notebook and do EDA
 - Make a simple baseline model 
 - Train a TensorFlow Regressor locally and plot the decreasing loss
 - Create a tabular dataset from the BigQuery data source
 -

### Dataset and util functions

The dataset comes from [UCI](https://archive.ics.uci.edu/ml/datasets/online+retail). The cloned repo provided some util functions:
  - `vertex-ai-qwikstart/utils/data_download.py`
      - This script is very useful and can be generally used in other projects as well. Mainly two functions are very useful: `download_url2gcs()` that downloads a dataset from given `url` and uploads it to a `google cloud storage bucket` and `upload_gcs2bq()` that uploads the dataset from `GCS bucket` into `BigQuery` (also some data cleaning takes place in this script) 

