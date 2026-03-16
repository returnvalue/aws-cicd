import boto3
import json

# Configure clients for LocalStack
s3 = boto3.client("s3", endpoint_url="http://localhost:4566", region_name="us-east-1")
iam = boto3.client("iam", endpoint_url="http://localhost:4566", region_name="us-east-1")

def solution():
    # 1. Create the S3 Artifact Bucket
    bucket_name = "cicd-artifact-store"
    print(f"Creating S3 bucket: {bucket_name}...")
    s3.create_bucket(Bucket=bucket_name)

    # 2. Define Trust Policies
    build_trust = {"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"codebuild.amazonaws.com"},"Action":"sts:AssumeRole"}]}
    deploy_trust = {"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"codedeploy.amazonaws.com"},"Action":"sts:AssumeRole"}]}
    pipeline_trust = {"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"codepipeline.amazonaws.com"},"Action":"sts:AssumeRole"}]}

    # 3. Create IAM Roles
    roles = [
        ("CodeBuildServiceRole", build_trust),
        ("CodeDeployServiceRole", deploy_trust),
        ("CodePipelineServiceRole", pipeline_trust)
    ]

    for role_name, trust_policy in roles:
        print(f"Creating IAM Role: {role_name}...")
        response = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy)
        )
        print(f"Created Role ARN: {response['Role']['Arn']}")

if __name__ == "__main__":
    solution()
