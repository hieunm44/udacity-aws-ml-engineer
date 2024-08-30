import sagemaker
from sagemaker.tuner import (
    IntegerParameter,
    CategoricalParameter,
    ContinuousParameter,
    HyperparameterTuner,
)
from torchvision.datasets import CIFAR10
from torchvision import transforms
from sagemaker.pytorch import PyTorch
import gzip 
import numpy as np
import random
import os

sagemaker_session = sagemaker.Session()

bucket = sagemaker_session.default_bucket()
prefix = "sagemaker/DEMO-pytorch-cifar"

role = sagemaker.get_execution_role()

local_dir = 'data'
CIFAR10.mirrors = ["https://sagemaker-sample-files.s3.amazonaws.com/datasets/image/CIFAR10/"]
CIFAR10(
    local_dir,
    download=True,
    transform=transforms.Compose(
        [transforms.ToTensor()]
    )
)

inputs = sagemaker_session.upload_data(path="data", bucket=bucket, key_prefix=prefix)
print("input spec (in this case, just an S3 path): {}".format(inputs))

estimator = PyTorch(
    entry_point="cifar.py",
    role=role,
    py_version='py36',
    framework_version="1.8",
    instance_count=1,
    instance_type="ml.m5.large"
)

hyperparameter_ranges = {
    "lr": ContinuousParameter(0.001, 0.1),
    "batch-size": CategoricalParameter([32, 64, 128, 256, 512]),
    "epochs": IntegerParameter(2, 4)
}

objective_metric_name = "average test loss"
objective_type = "Minimize"
metric_definitions = [{"Name": "average test loss", "Regex": "Test set: Average loss: ([0-9\\.]+)"}]

tuner = HyperparameterTuner(
    estimator,
    objective_metric_name,
    hyperparameter_ranges,
    metric_definitions,
    max_jobs=4,
    max_parallel_jobs=2,
    objective_type=objective_type,
)

tuner.fit({"training": inputs})

predictor = tuner.deploy(initial_instance_count=1, instance_type="ml.t2.medium")

# Query the Endpoint

file = 'data/cifar-10-batches-py/data_batch_1'
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

data=unpickle(file)
data=np.reshape(data[b'data'][0], (3, 32, 32))

response = # TODO: Query the endpoint
print(response)