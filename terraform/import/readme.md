DRAFT

To test it:

log on your AWS account, and create:
- a lambda function my-bucket-test-1
- an s3 bucket named my-bucket-test-1

and import them by:

terraform import aws_lambda_function.my-lambda-test-2 my-lambda-test-2

terraform import aws_s3_bucket.bucket my-bucket-test-1

terraform import aws_network_acl.main acl-f1780b98

terraform import aws_lambda_layer_version.test_layer arn:aws:lambda:us-east-2:397270606208:layer:aws_lambda_read_s3:1


Them a terraform.tfstate will be generated or updated with your config.