import boto3

# Configure clients for LocalStack
codebuild = boto3.client("codebuild", endpoint_url="http://localhost:4566", region_name="us-east-1")
iam = boto3.client("iam", endpoint_url="http://localhost:4566", region_name="us-east-1")

def solution():
    # Fetch the build role ARN (assuming it was created in Lab 2)
    try:
        role_response = iam.get_role(RoleName="CodeBuildServiceRole")
        build_role_arn = role_response["Role"]["Arn"]
    except:
        # Fallback if role doesn't exist in current session
        build_role_arn = "arn:aws:iam::000000000000:role/CodeBuildServiceRole"

    print("Creating CodeBuild project: WebAppBuild...")
    codebuild.create_project(
        name="WebAppBuild",
        source={
            "type": "CODECOMMIT",
            "location": "https://git-codecommit.us-east-1.amazonaws.com/v1/repos/portfolio-web-app"
        },
        artifacts={"type": "NO_ARTIFACTS"},
        environment={
            "type": "LINUX_CONTAINER",
            "image": "aws/codebuild/amazonlinux2-x86_64-standard:3.0",
            "computeType": "BUILD_GENERAL1_SMALL"
        },
        serviceRole=build_role_arn
    )
    print("CodeBuild project created successfully.")

if __name__ == "__main__":
    solution()
