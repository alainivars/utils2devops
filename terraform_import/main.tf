
provider "aws" {
  region = "us-east-2"
}

resource "aws_lambda_function" "lambda" {
    # (resource arguments)
}

resource "aws_s3_bucket" "bucket" {
  # (resource arguments)
}

resource "aws_network_acl" "main" {
  # (resource arguments)
}
