from aws_cdk import (
    aws_s3 as s3,
    aws_iam as iam,
    aws_cloudfront as cloudfront,
    aws_certificatemanager as certmgr,
    aws_route53 as route53,
    aws_route53_targets as targets,
    core,
)
class AccelerateTemplate(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id)
        #create an S3 bucket
        domainName = 'accelerate.dev'
        myBucket = s3.Bucket(self, 'accelerate.dev-s3bucket', 
            bucket_name='accelerate-website',
            public_read_access= True,
            website_index_document='index.html',
            website_error_document='404.html',
            removal_policy= core.RemovalPolicy.DESTROY)
        myBucket.grant_public_access
        myBucket.add_to_resource_policy(    #Grant read access to everyone in your account
            iam.PolicyStatement(
                    actions=['s3:GetObject'],
                    resources=[myBucket.arn_for_objects('*')],
                    principals=[iam.AccountPrincipal(account_id=core.Aws.ACCOUNT_ID)]))
        myUser = iam.User(self,'deploy_'+domainName)    #Grant write access to a specific user
        myBucket.grant_write(myUser)
        hostedZone = route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone_"+domainName,
            hosted_zone_id='Z00154093I7THXRTRF8QB',
            zone_name=domainName)
        cert = certmgr.DnsValidatedCertificate(self, "cert_"+domainName, 
            domain_name=domainName, 
            hosted_zone=hostedZone)
        distribution = cloudfront.CloudFrontWebDistribution(self, "accelerate.dev-distribution",
            price_class=cloudfront.PriceClass.PRICE_CLASS_100,
            origin_configs=[cloudfront.SourceConfiguration(
            s3_origin_source=cloudfront.S3OriginConfig(s3_bucket_source=myBucket),
            behaviors=[cloudfront.Behavior(is_default_behavior=True)])],
            viewer_certificate=cloudfront.ViewerCertificate.from_acm_certificate(cert,
                aliases=['accelerate.dev']))
                
        route53.ARecord(self, "Alias_"+domainName,
            zone=hostedZone,
            target=route53.RecordTarget.from_alias(targets.CloudFrontTarget(distribution)))

app = core.App()
AccelerateTemplate(app, "AccelerateTemplate", env={'region':'us-east-1'})
app.synth()