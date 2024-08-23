A template repository for versioning and deploying Lambda functions to AWS using a Github Action.


Requires some Repository Actions Variables to be set on the repository, which should be handled by [the TF module](https://github.com/nphilbrook/terraform-aws-function-with-api)


Requires AWS auth to be configured. Ideally [via OIDC](https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/) and an assume role, which is how the YAML is currently written. See some [Terraform code](https://github.com/nphilbrook/lambda-playground/blob/main/gh_oidc.tf) to set up the AWS side of this OIDC configuration.


Actions secrets with long-lived token creds would work as well, the yaml would need to be modified.


Broadly does the following:

```
# Get the bucket name from TF output
aws s3 cp lambda_function.zip s3://S3_BUCKET/
```

```
# same, function name too
aws lambda update-function-code  --function-name FUNCTION_NAME  --s3-bucket S3_BUCKET --s3-key lambda_function.zip
```
