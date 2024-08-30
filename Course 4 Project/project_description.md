# Project Overview

## Introduction to the Project
Welcome to the capstone project of this course, where you will apply the skills and knowledge you've gained to a real-world challenge. You will be leveraging AWS SageMaker to fine-tune a pre-trained model for the task of image classification. This project is designed to simulate a typical machine learning workflow that a professional ML Engineer would undertake. You will have the freedom to choose a dataset of your interest.

For instance, you can use the [dog breed classication](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip) dataset to classify between different breeds of dogs in images.

## Project Objectives and Outcomes
Your task is to utilize AWS SageMaker's comprehensive suite of tools to build, train, and deploy a machine learning model. Here's what you're expected to accomplish:

## Model Fine-Tuning:
Choose a pre-trained model, such as ResNet50, and apply transfer learning techniques to adapt it to your chosen dataset. While ResNet50 is recommended due to our course content, feel free to explore other pre-trained models available in frameworks like TensorFlow or PyTorch.

## SageMaker Features:
* Implement SageMaker's profiling and debugging tools to monitor model training and performance.
* Conduct hyperparameter tuning to optimize your model's performance.
* Adopt best ML engineering practices throughout your workflow.

## Model Deployment:
* Deploy your fine-tuned model to a SageMaker endpoint.
* Ensure that you can query the deployed model with a sample image to retrieve a prediction.

## Project Pipeline Overview
As an ML Engineer, you will manage the flow of various components such as data, models, metrics, and predictions through the following stages:
* __Data Preparation__: Process and prepare your image data for training.
* __Model Training and Tuning__: Train your model using SageMaker and fine-tune it with hyperparameter optimization.
* __Model Deployment and Testing__: Deploy the trained model to an endpoint and test it with real-world data to ensure functionality.
![](https://video.udacity-data.com/topher/2021/May/60ad3417_project-diagrams/project-diagrams.png)

## The Goal of the Project
The primary goal of this project is to demonstrate the setup of an ML infrastructure that can facilitate the training of accurate models by you or other developers. It's not just about achieving high accuracy but about understanding and implementing the end-to-end process that makes ML development sustainable, scalable, and efficient.


# Step 1: Project Setup and Preparing Data
By the end of this task, you should have completed setting up your environment for building this project and preparing your data for training your models.
## Setup AWS
To build this project, you will have to use AWS through your classroom. Below are your main steps:
1. Open AWS
2. Open SageMaker Studio and create a folder for your project

## Download the Starter Files
We have provided a project template and some helpful starter files for this project. You can clone the [Github Repo](https://github.com/udacity/CD0387-deep-learning-topics-within-computer-vision-nlp-project-starter).
1. Clone or download starter files
2. Upload starter files to your workspace

## Preparing Data
You are free to use any image classification data you want (like the dog breed classification data available [here](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip)):
1. Download the dataset
2. Unzip the files (if needed)
3. Upload them to an S3 bucket
4. OPTIONAL: Verify that the data hast been updated correctly


# Step 2: Train and Deploy the Model
In this step, you will write code to use Sagemaker to finetune a pretrained model with hyperparameter tuning. Once you have found the best hyperparameters, you can use them to train an estimator with model debugging and profiling. This model will then need to be deployed and tested.

## Get Familiar with the Starter Code
Make sure that you have a basic understanding of what the different files are and how they will be used in this project.
* `train_and_deploy.ipynb`
* `train_model.py`

## Complete the train_model.py script
* Read and Preprocess data: Before training your model, you will need to read, load and preprocess your training, testing and validation data
* Finetune a Pretrained Model: You can choose any pretrained model to finetune for this project
* Model Debugging and Profiling: Make sure that your code can use Sagemaker's model debugging and profiling
* Hyperparameter Tuning: Make sure that you code can use Sagemaker's hyperparameter tuning

## Train the Model
The `train_model.py` script is what will train the model. The `train_and_deploy.ipynb` notebook will help you interface with Sagemaker and submit training jobs to it. Inside it are some `TODO` comments.
* Install necessary dependencies
* Setup the Hyperparameter search space
* Set up the model debugging and profiling rules
* Create the model estimator and Hyperparameter tuning job
* Submit the job
* Fetch the best training job

## Complete the `train_and_deploy.ipynb` Notebook
In addition to the above steps, you also need to do the following steps in the `train_and_deploy.ipynb` notebook:
* Fetch the Debugger Profiling Report
* Deploy the best training job
* Query the model endpoint with an input and get a result


# Step 3: Complete the README
An important part of your project is creating a `README` file that describes the project, explains how to set up and run the code, and describes your results. We've included a template in the starter files (that you downloaded earlier), with `TODOs` for each of the things you should include.


# Step 4: Standout Suggestions
Standout suggestions are some recommendations to help you take your project further and turn it into a nice portfolio piece. If you have been having a good time working on this project and want some additional practice, then we recommend that you try them. However, these suggestions are all optional and you can skip any (or all) of them and submit the project on the next page.

Here are some of the suggestions to improve your project:
* Package Your Model: Can you package your model as a [Docker Container](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers.html) so that it can be easily deployed
* Multi-Model Endpoint: Can you finetune multiple (different) pretrained models and try to deploy them to the same endpoint in the form of a [Multi-Model Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)?
* Batch Transform: Can you create a [batch transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html) that performs inference on the whole test set together?
* Model Explainability: Can you use [Amazon Sagemaker Clarity](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-explainability.html) to make your models more interpretable?

Once you have completed the standout suggestions, make sure that you explain what you did and how you did it in the `README`. This way the reviewers will look out for it and can give you helpful tips and suggestions