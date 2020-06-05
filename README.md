# AWS infrastructure for a static-webpage

Quick [CDK-template](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html) in Python for hosting static websites (such as hugo, jekyll, etc.) on AWS S3, Cloudfront, Route53 and Certificate Manager. 

The code gets everything ready, and even generates a public certificate. Note: The scripts take time to run the first time, because of validation of the certificate and propagation of the Cloudfront distribution. 

Altså creates a write-user connected to the s3-bucket, to be used for deployment.


# HOW
* Make sure to change the domain and bucket names inside the code.
* You also need to have an existing hosted zone in Route53, and update the code with the zone-id.

And simply run...
```bash
  $ pip3 install -r requirements.txt
  $ cdk bootstrap
  $ cdk deploy
  $ aws s3 sync <folder with website> s3://<bucketname>
```
The aws-cli-command should be run with a profile using the api-keys of the new user generated.
