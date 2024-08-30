# Exercise: Create a transformation job in Lambda
In this exercise, you will create a lambda function to preprocess the review data we used in the previous exercises.

First, navigate to lesson 3 in the course Github repo which contains a python script named `HelloBlazePreprocessLambda.py`.

You will need to rename two constants at the top of the file: `BUCKET_NAME` and `PREFIX`. Rename `BUCKET_NAME` to a bucket in your account, and rename 'PREFIX' to the valid name of your choice. This is where the output of your lambda function will be directed to.

## Steps:
###Setup Environment:
1. Navigate to the course GitHub repository, lesson 3.
2. Download `HelloBlazePreprocessLambda.py`.
3. Update constants:
    * `BUCKET_NAME`: Assign to an existing S3 bucket in your account.
    * `PREFIX`: Choose a valid name for the output directory.
### Create IAM Role:
1. Go to the AWS IAM console.
2. Create a new role for Lambda with S3 read/write access.
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListObjectsInBucket",
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": ["arn:aws:s3:::your-bucket-name"]
    },
    {
      "Sid": "AllObjectActions",
      "Effect": "Allow",
      "Action": "s3:*Object",
      "Resource": ["arn:aws:s3:::your-bucket-name/*"]
    }
  ]
}
```
### Create Lambda Function:
1. Use AWS Lambda console.
2. Create a function named "PreprocessLambda" with Python 3.8 (latest supported runtime)
3. Upload `HelloBlazePreprocessLambda.py` after zipping it.
### Configure Lambda Function:
1. In lambda_handler, invoke the preprocess method from HelloBlazePreprocessLambda.
2. Process events with "s3-dataset-uri" key, format: `BUCKET/PREFIX/FILEOBJ`.
3. Modify the response to indicate success, e.g., 'Preprocessing Successful!'
4. Set the function timeout to 1 minute.
### Prepare Test Data:
1. Upload the zipped file of musical instrument reviews to your S3 bucket.
2. Create a test event in Lambda:
```
{
  "s3-dataset-uri": "your-bucket-name/your-prefix/reviews_Musical_Instruments_5.json.zip"
}
```
### Test and Validate:
1. Execute the test event in Lambda.
2. Verify that the function runs successfully and outputs data to the specified S3 location.
### Outcome:
* Upon successful execution, your Lambda function will preprocess the data and output results to S3, showcasing serverless computing efficiency.
### Tips:
* Regularly review AWS documentation for any updates in services and best practices.
* Consider integrating AWS CloudWatch for monitoring and logging Lambda function executions.
* Explore AWS Step Functions for orchestrating more complex workflows involving Lambda.