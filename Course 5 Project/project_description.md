# Project Overview
In this project, you'll start with a completed ML project. The completed project contains code that trains and deploys an image classification model on AWS Sagemaker. Your goal in this project will be to use several important tools and features of AWS to adjust, improve, configure, and prepare the model you started with for production-grade deployment. Taking raw ML code and preparing it for production deployment is a common task for ML engineers, and it's very important for the following reasons:
1. ML code alone isn't sufficient for most business scenarios. Real business situations require ML code to integrate with other infrastructures, like API's, applications, or other websites that require ML code to be correctly configured. You'll configure some crucial production infrastructure for an ML pipeline in this project.
2. If ML code is deployed in a way that's not optimal, it can lead to cost overruns or bad performance. You'll choose and deploy optimal computing resources for your ML code in this project.
3. When ML code is moved to production deployment, security is always a concern, since poor security can lead to data leaks or performance issues. You'll configure and optimize ML pipeline security in this project.

Your final submission will show your understanding of all of the following aspects of AWS machine learning operations:
* Managing computing resources efficiently
* Training models with large datasets using multi-instance training
* Setting up high-throughput, low-latency pipelines
* AWS security

By improving and preparing an image classification project for production-grade deployment, you'll demonstrate that you have the skills to work on the most advanced ML pipelines in the world. You'll be prepared to do excellent work as an ML engineer with the ability to optimize ML pipelines for efficiency, speed, and security.

## Project Summary
In this project, you will complete the following steps:
1. Train and deploy a model on Sagemaker, using the most appropriate instances. Set up multi-instance training in your Sagemaker notebook.
2. Adjust your Sagemaker notebooks to perform training and deployment on EC2.
3. Set up a Lambda function for your deployed model. Set up auto-scaling for your deployed endpoint as well as concurrency for your Lambda function.
4. Ensure that the security on your ML pipeline is set up properly.

## What you'll submit
After you complete the project, you'll submit the following:
* a writeup describing the decisions you make during the project and justifications for them. This writeup should be named "writeup". Each answer in the writeup should be 1 paragraph. The final document should be between 1 and 2 pages long.
* code for your solutions (notebooks and Python files)
* screenshots for certain portions of the project (including Sagemaker instance setup, EC2 setup, Lambda function setup, and IAM security)

You can find more information about what to submit described in the individual Steps, and also on the "Project Submission" page.


# Step 1: Training and deployment on Sagemaker
## Initial Setup
First, find and download your starter files, which are located in the Resources section for this project lesson. The starter file called `train_and_deploy-solution.ipynb` is a Jupyter notebook that trains and deploys a computer vision model. The starter file called `hpo.py` is the "entry point" for the `train_and_deploy-solution.ipynb` notebook. You can upload both of these files to a Sagemaker instance and run them there, using Jupyter or JupyterLab.

Before you run these files, you'll have to create and open a Sagemaker instance. Decide which type of Sagemaker instance you should create for your training and deployment. Consider the cost, computing power, and speed of launching for each instance type. Write a short justification of why you chose the instance type you did. After you launch your Sagemaker instance, take a screenshot of your Sagemaker dashboard's `Notebooks > Instances` section to show what you've done.

__Note__: For this project, you should perform all of the Sagemaker steps using Sagemaker itself, not Sagemaker Studio.

## Sagemaker Dashboard screenshots
For the screenshot you submit for this part of the project, you should show the `Notebooks > Instances` section of Sagemaker. The example screenshot below shows an example (with the instance type censored).
![](https://video.udacity-data.com/topher/2021/July/60e74b47_udacityshot1/udacityshot1.png)

## Download data to an S3 bucket
The first three cells of the `train_and_deploy-solution.ipynb` will download data to your AWS workspace. The third cell copies the data to an S3 bucket. You need to set up an S3 bucket that you can copy the data to.

After you set up an S3 bucket, take a screenshot showing that you've set up an S3 bucket. Include this screenshot in your final submission.

After setting up an S3 bucket, you need to change some cells in the `train_and_deploy-solution.ipynb` notebook. In particular, the third cell, eighth cell, and sixteenth cell contain references to an S3 bucket called `s3://udacitysolution/`. You need to find all references to this bucket name and change them so they refer to the name of the S3 bucket that you created.

After changing all of these references, you will be prepared to run the first three cells of your `train_and_deploy-solution.ipynb` notebook. Run these cells to download training and validation data for the project's ML pipeline.

## Training and Deployment
After downloading your data to S3, you're ready to perform training and deployment. You can accomplish this by running the remaining cells in the `train_and_deploy-solution.ipynb` notebook. Start by running all of the cells from the fourth to the sixteenth cell. The sixteenth cell is the final cell in the section called "Creating an Estimator." The sixteenth cell will fit an estimator. You will have to wait some time for the estimator to complete the fitting process - it usually takes about 20 minutes for this process to complete. You can check the progress of this process by navigating to the "Training > Training Jobs" section of Sagemaker. While the fitting process is in progress, you will see a job listed here whose status is listed as "InProgress." After it completes, the status should be listed as "Completed."

After the estimator fitting process completes, you can run the remaining cells in the `train_and_deploy-solution.ipynb` notebook. This will deploy an endpoint to your Sagemaker account. You should navigate to the "Inference > Endpoints" section of Sagemaker so you can see the name of your deployed endpoint. You should make a note of the name of the deployed endpoint, because you will need to use a deployed endpoint later in the project. You should also take a screenshot showing the "Inference > Endpoints" section of SageMaker. This screenshot should show that you've deployed an endpoint. You should submit this screenshot in your final submission.

__Note__: Deployed endpoints generate AWS charges. If you need to take a long break from working on your project, you may wish to delete your deployed endpoint, then re-deploy it later, to avoid generating excessive charges.

## Multi-instance training
You have trained and deployed a model and endpoint on Sagemaker. Now, alter the code in your train_and_deploy-solution.ipynb so that it performs multi-instance training. You'll need to alter the estimator definition in the sixteenth cell of the notebook to accomplish this.

After altering your code to accomplish multi-instance training, run the train_and_deploy-solution.ipynb notebook again to deploy another model and endpoint in your AWS workspace. When you submit your solution, you'll submit the altered version of train_and_deploy-solution.ipynb that performs multi-instance training.

__Note__: it's not necessary to run the entire notebook again. Instead, you could re-run only the cells from the sixteenth cell to the end. Make sure you wait for the estimator fitting process to complete before you attempt to deploy an endpoint.


# Step 2: EC2 Training
## EC2 Setup
After completing Step 1, you should have a notebook that completes model training and deployment on Sagemaker. The next step is to set up an EC2 instance and accomplish model training there.

The first thing you'll need to do is create an EC2 instance. Think about what type of instance you want to create, based on cost, computing power, and launch speed. Decide the type of instance you want, create it in your workspace, and write a justification of why you chose the instance type you did.

__Note__: when you select an AMI for your EC2 instance, you should select the "Amazon Deep Learning AMI" so that you can use its libraries.

After you create your EC2 instance, launch it and connect to it. You will then be ready to proceed to the next step.

## Preparing for EC2 model training
Next, prepare for EC2 model training. Start by launching and connecting to an EC2 instance, as described in the previous section. After you've connected to the instance, obtain the data you need for training, by running the following two commands in your EC2 terminal:
```
wget https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip
unzip dogImages.zip
```
Next, create a directory for your trained models by running the following command in your EC2 terminal:
```
mkdir TrainedModels
```
Next, open a blank Python file by running the following command in your EC2 Terminal:
```
vim solution.py
```
This will open the text editor called `vim` in your terminal. You need to prepare to paste code into this file by typing the following in vim, then pressing Enter:
```
:set paste
```
Paste all of the code from the starter file called `ec2train1.py` into the file you've opened. After pasting the code in, type `:wq!` and press Enter to save the file and exit the `vim` program.

You're now ready to run the EC2 training code and save the model to your EC2 instance.

## Training and saving on EC2
Now, you're ready to run your code. You can run the code by running the following command in your EC2 terminal:
```
python solution.py
```
Your adjusted code should accomplish the following:
* Train the same model that is trained in the starter code. (You should use the same dataset and the same model parameters.)
* Save the model to a location (the TrainedModels directory) on your EC2 instance. (It's not possible to deploy directly, like we did on Sagemaker.)

After your code is finished running, you can open the TrainedModels directory on your EC2 instance and take a screenshot of the model that has been saved in it, to provide evidence that you completed this step.

## Write about the EC2 code
The code you worked with in Step 1, `train_and_deploy-solution.ipynb`, was specifically written to work in Sagemaker. In order to train the same model on an EC2 instance, you used the adjusted code in ec2train1.py.

The adjusted code in `ec2train1.py` is very similar to the code in `train_and_deploy-solution`,ipynb. But there are a few differences between the modules used - some modules can only be used in SageMaker. Much of the EC2 training code has also been adapted from the functions defined in the `hpo.py` starter script.

For the last part of this step, write at least one paragraph about the differences between the code in `ec2train1.py` and the code you used in Step 1. You may work on projects that require adaptation between EC2 and SageMaker code, and understanding the differences in this project can help you prepare for that kind of adaptation.


# Step 3: Lambda function setup
After training and deploying your model, setting up a Lambda function is an important next step. Lambda functions enable your model and its inferences to be accessed by API's and other programs, so it's a crucial part of production deployment.

You need to set up a Lambda function that uses Python 3 for its runtime. In the same starter files you downloaded in Step 1 of this project lesson, you will also find starter code for your Lambda function, in a file called `lambdafunction.py`. This file contains some of the basic Python code for a Lambda function, but you need to make an important adjustment to it:

Change the endpoint_name variable, to give it the same name as the endpoint you deployed in Step 1. You can find the name of this endpoint in the "Inference > Endpoints" section of Sagemaker.
After making this adjustment to your Lambda function, you should have a completed code file, `lambdafunction.py`, that reflects the adjustment listed above. Your `lambdafunction.py` file will be part of your final submission. Now, you're almost ready to test your Lambda function to make sure it works correctly. The next step contains information about how to add security to your Lambda function, and how to test it.

You should also notice the content of this Lambda function. You may have to set up many Lambda functions in your career, so do your best to understand how this one is set up so you can follow its example. In particular, you should notice how it invokes the endpoint (with the invoke_endpoint() method) and how it sets up the return statement. Write at least 1 paragraph describing how this function is written and how it works.


# Step 4: Security and testing
## Lambda function security
In Step 3, you configured a Lambda function to invoke your deployed endpoint. However, the lambda function will only be able to invoke your endpoint if it has the proper security policies attached to it. You'll have to find the "role" that the lambda function is using in the IAM interface. Then, attach the correct security policy to the role of the lambda function. The security policy you attach should be one that allows your lambda function to access all of your SageMaker endpoints.

## Lambda function testing
After resolving the lambda function security issue, you can test your lambda function. In order to test your function, you can click the "Test" button in the lambda function interface in AWS. You will need to configure a test event for testing. Your lambda function will return a classification of the photo you submit. You can use the following text for your test event:
```
{ "url": "https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/20113314/Carolina-Dog-standing-outdoors.jpg" }
```
Take a screenshot of your lambda function screen after running a test with this test event. Your test should return the result of invoking your deployed endpoint. This should be a list of 33 numbers, each of which represents a prediction about the class membership of the picture you submitted. Add the result that your lambda function returns (the list of 33 numbers) to your solution writeup.

## Other security considerations
Open the IAM section of your project. Check the roles that are defined for your project, and the security policies that are attached to each of these roles.

Take a screenshot of the IAM dashboard in your AWS account. The screenshot should show the policies that are attached to your Lambda function's role.

Write about the security of your AWS workspace in your writeup. Are there any security vulnerabilities that need to be addressed? Think about some common security vulnerabilities. For example, roles that have "FullAccess" policies attached may be too permissive and may lead to problems. Roles that are old or inactive may lead to vulnerabilities because they may belong to people who are no longer working on the project and who may not be careful about ensuring the project's success. You might also find roles for functions that the project is no longer using, which should probably be deleted.


# Step 5: Concurrency and auto-scaling
## Concurrency
You have successfully set up a Lambda function in AWS. Next, you should set up concurrency for your Lambda function. Concurrency will make your Lambda function better able to accommodate high traffic because it will enable your function to respond to multiple invocations at once.

To set up concurrency on your Lambda function, you will need to open your Lambda function in the Lambda section of AWS. Next, you should open the `Configuration` tab. Then, you should configure a `Version` for your function, in the `Version` section of the `Configuration` tab.

After configuring a Version for your Lambda function, navigate to the `Concurrency` section of the `Configuration` tab of your function. Use this section to configure concurrency for your Lambda function. You can choose to set up any type of concurrency and configure it however you think is best.

Auto-scaling
In addition to setting up concurrency for your Lambda function, you should also set up auto-scaling for your deployed endpoint. You can accomplish this by navigating to the `Inference > Endpoints` section of Sagemaker. This will open a list of your deployed endpoints. Click on the endpoint that you deployed in Step 1 of the project. This will open a configuration dashboard for your deployed endpoint. This dashboard has a table called `Endpoint runtime settings` that has a row for every `variant` of your endpoint. There should be one row in this table. Select the only row in this table, and click `Configure auto scaling` to start the process of configuring auto-scaling for your endpoint.

## Writing about your choices
When you set up concurrency and auto-scaling, you will make several choices about configuration. Write about the choices you made in the setup of concurrency and auto-scaling, and why you made each of those choices.