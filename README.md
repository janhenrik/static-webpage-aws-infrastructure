# AWS infrastructure for a static-webpage

Quick CDK-template in Python for hosting static websites (such as hugo, jekyll, etc.) on AWS S3, Cloudfront, Route53 and Certificate Manager. 

The code gets everything ready, and even generates a public certificate. Note: The scripts take time to run the first time, because of validation of the certificate and propagation of the Cloudfront distribution.

Altså creates a write-user connected to the s3-bucket, to be used for deployment.

# HOW
Make sure to change the domain and bucket names inside the code.
And simply run...
```bash
  $ pip3 install -r requirements.txt
  $ cdk bootstrap
  $ cdk deploy
  $ export AWS_PROFILE=XX && aws s3 sync <folder with website> s3://<bucketname>
```
