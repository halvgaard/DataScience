from zenml.pipelines import pipeline
from zenml.steps import step, Output, BaseStepConfig
import pandas_gbq
import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.base import ClassifierMixin
from sklearn.linear_model import LogisticRegression

class BigQueryImporterConfig(BaseStepConfig):
    query: str = 'SELECT * FROM `computas_dataset.iris_data`'
    project_id: str = 'computas-project-345810'

@step
def bigquery_importer(config: BigQueryImporterConfig) -> pd.DataFrame:
    return pandas_gbq.read_gbq(config.query, project_id = config.project_id)

@step
def preparator(data: pd.DataFrame) -> Output(
    X_train=np.ndarray, X_test=np.ndarray, y_train=np.ndarray, y_test=np.ndarray
):
    encoder = OrdinalEncoder()
    data['target'] = encoder.fit_transform(data[['Species']])

    X = np.array(data[['SepalLengthCm','SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']])
    y = np.array(data['target'])

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

    return X_train, X_test, y_train, y_test 

@step
def trainer(
    X_train: np.ndarray,
    y_train: np.ndarray,
) -> LogisticRegression:
    """Train a simple sklearn classifier for the Iris dataset."""
    model = LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)
    return model

@step
def evaluator(
    X_test: np.ndarray,
    y_test: np.ndarray,
    model: LogisticRegression,
) -> float:
    """Calculate the accuracy on the test set"""
    test_acc = model.score(X_test, y_test)
    print(f"Test accuracy: {test_acc}")
    return test_acc
    
@pipeline
def iris_pipeline(
    bigquery_importer,
    preparator,
    trainer,
    evaluator,
):
    """Links all the steps together in a pipeline"""
    data = bigquery_importer() 
    X_train, X_test, y_train, y_test = preparator(data=data)
    model = trainer(X_train=X_train, y_train=y_train)
    evaluator(X_test=X_test, y_test=y_test, model=model)

pipeline = iris_pipeline(
    bigquery_importer=bigquery_importer(),
    preparator=preparator(),
    trainer=trainer(),
    evaluator=evaluator(),
)

pipeline.run()
