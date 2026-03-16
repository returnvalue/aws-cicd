import boto3

# Configure clients for LocalStack
codepipeline = boto3.client("codepipeline", endpoint_url="http://localhost:4566", region_name="us-east-1")
iam = boto3.client("iam", endpoint_url="http://localhost:4566", region_name="us-east-1")

def solution():
    # Fetch the pipeline role ARN
    try:
        role_response = iam.get_role(RoleName="CodePipelineServiceRole")
        pipeline_role_arn = role_response["Role"]["Arn"]
    except:
        pipeline_role_arn = "arn:aws:iam::000000000000:role/CodePipelineServiceRole"

    # Define the Pipeline structure
    pipeline_def = {
        "name": "WebApp-CI-CD-Pipeline",
        "roleArn": pipeline_role_arn,
        "artifactStore": {"type": "S3", "location": "cicd-artifact-store"},
        "stages": [
            {
                "name": "Source",
                "actions": [{
                    "name": "SourceAction",
                    "actionTypeId": {"category": "Source", "owner": "AWS", "provider": "CodeCommit", "version": "1"},
                    "outputArtifacts": [{"name": "SourceArtifact"}],
                    "configuration": {"RepositoryName": "portfolio-web-app", "BranchName": "main"}
                }]
            },
            {
                "name": "Build",
                "actions": [{
                    "name": "BuildAction",
                    "actionTypeId": {"category": "Build", "owner": "AWS", "provider": "CodeBuild", "version": "1"},
                    "inputArtifacts": [{"name": "SourceArtifact"}],
                    "outputArtifacts": [{"name": "BuildArtifact"}],
                    "configuration": {"ProjectName": "WebAppBuild"}
                }]
            },
            {
                "name": "Deploy",
                "actions": [{
                    "name": "DeployAction",
                    "actionTypeId": {"category": "Deploy", "owner": "AWS", "provider": "CodeDeploy", "version": "1"},
                    "inputArtifacts": [{"name": "BuildArtifact"}],
                    "configuration": {"ApplicationName": "WebAppDeploy", "DeploymentGroupName": "DevDeploymentGroup"}
                }]
            }
        ]
    }

    print("Creating CodePipeline: WebApp-CI-CD-Pipeline...")
    codepipeline.create_pipeline(pipeline=pipeline_def)
    print("Pipeline created successfully.")

if __name__ == "__main__":
    solution()
