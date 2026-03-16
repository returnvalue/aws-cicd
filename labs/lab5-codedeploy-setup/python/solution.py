import boto3

# Configure clients for LocalStack
codedeploy = boto3.client("codedeploy", endpoint_url="http://localhost:4566", region_name="us-east-1")
iam = boto3.client("iam", endpoint_url="http://localhost:4566", region_name="us-east-1")

def solution():
    # Fetch the deploy role ARN
    try:
        role_response = iam.get_role(RoleName="CodeDeployServiceRole")
        deploy_role_arn = role_response["Role"]["Arn"]
    except:
        deploy_role_arn = "arn:aws:iam::000000000000:role/CodeDeployServiceRole"

    # 1. Create the CodeDeploy Application
    print("Creating CodeDeploy application: WebAppDeploy...")
    codedeploy.create_application(
        applicationName="WebAppDeploy",
        computePlatform="Server"
    )

    # 2. Create the Deployment Group
    print("Creating Deployment Group: DevDeploymentGroup...")
    codedeploy.create_deployment_group(
        applicationName="WebAppDeploy",
        deploymentGroupName="DevDeploymentGroup",
        deploymentConfigName="CodeDeployDefault.OneAtATime",
        ec2TagFilters=[
            {"Key": "Environment", "Value": "Dev", "Type": "KEY_AND_VALUE"}
        ],
        serviceRoleArn=deploy_role_arn
    )
    print("Deployment Group created successfully.")

if __name__ == "__main__":
    solution()
