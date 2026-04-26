# Lab 6: Pipeline Orchestration (AWS CodePipeline)

**Goal:** Stitch Source, Build, and Deploy stages together. CodePipeline automates the flow: when a commit happens in CodeCommit, it triggers CodeBuild, takes the output artifact, passes it to S3, and hands it to CodeDeploy for installation.
```bash
# 1. Create the Pipeline JSON definition
cat <<EOF > pipeline.json
{
  "pipeline": {
    "name": "WebApp-CI-CD-Pipeline",
    "roleArn": "$PIPELINE_ROLE",
    "artifactStore": { "type": "S3", "location": "cicd-artifact-store" },
    "stages": [
      {
        "name": "Source",
        "actions": [{
          "name": "SourceAction",
          "actionTypeId": { "category": "Source", "owner": "AWS", "provider": "CodeCommit", "version": "1" },
          "outputArtifacts": [{ "name": "SourceArtifact" }],
          "configuration": { "RepositoryName": "portfolio-web-app", "BranchName": "main" }
        }]
      },
      {
        "name": "Build",
        "actions": [{
          "name": "BuildAction",
          "actionTypeId": { "category": "Build", "owner": "AWS", "provider": "CodeBuild", "version": "1" },
          "inputArtifacts": [{ "name": "SourceArtifact" }],
          "outputArtifacts": [{ "name": "BuildArtifact" }],
          "configuration": { "ProjectName": "WebAppBuild" }
        }]
      },
      {
        "name": "Deploy",
        "actions": [{
          "name": "DeployAction",
          "actionTypeId": { "category": "Deploy", "owner": "AWS", "provider": "CodeDeploy", "version": "1" },
          "inputArtifacts": [{ "name": "BuildArtifact" }],
          "configuration": { "ApplicationName": "WebAppDeploy", "DeploymentGroupName": "DevDeploymentGroup" }
        }]
      }
    ]
  }
}
EOF

# 2. Create the Pipeline
awslocal codepipeline create-pipeline --cli-input-json file://pipeline.json
aws codepipeline create-pipeline --cli-input-json file://pipeline.json
```

## 🧠 Key Concepts & Importance

- **Continuous Orchestration:** AWS CodePipeline automates the build, test, and deploy phases of your release process every time there is a code change, based on the release model you define.
- **Workflow Stages:** A pipeline is divided into stages (e.g., Source, Build, Deploy). Each stage contains one or more actions that are performed on the application code.
- **Artifact Passing:** CodePipeline manages the flow of artifacts between stages. For example, the `SourceArtifact` output from CodeCommit becomes the input for CodeBuild.
- **Service Integration:** CodePipeline acts as the "glue," natively integrating with CodeCommit, CodeBuild, CodeDeploy, and other services like Lambda or CloudFormation.
- **Automation and Reliability:** By removing manual steps, pipelines ensure that deployments are consistent, repeatable, and less prone to human error.

## 🛠️ Command Reference

- `codepipeline create-pipeline`: Creates a new pipeline using a JSON structure.
    - `--cli-input-json`: The path to the JSON file defining the stages, actions, and roles for the pipeline.

---

💡 **Pro Tip: Using `aws` instead of `awslocal`**

If you prefer using the standard `aws` CLI without the `awslocal` wrapper or repeating the `--endpoint-url` flag, you can configure a dedicated profile in your AWS config files.

### 1. Configure your Profile
Add the following to your `~/.aws/config` file:
```ini
[profile localstack]
region = us-east-1
output = json
# This line redirects all commands for this profile to LocalStack
endpoint_url = http://localhost:4566
```

Add matching dummy credentials to your `~/.aws/credentials` file:
```ini
[localstack]
aws_access_key_id = test
aws_secret_access_key = test
```

### 2. Use it in your Terminal
You can now run commands in two ways:

**Option A: Pass the profile flag**
```bash
aws iam create-user --user-name DevUser --profile localstack
```

**Option B: Set an environment variable (Recommended)**
Set your profile once in your session, and all subsequent `aws` commands will automatically target LocalStack:
```bash
export AWS_PROFILE=localstack
aws iam create-user --user-name DevUser
```

### Why this works
- **Precedence**: The AWS CLI (v2) supports a global `endpoint_url` setting within a profile. When this is set, the CLI automatically redirects all API calls for that profile to your local container instead of the real AWS cloud.
- **Convenience**: This allows you to use the standard documentation commands exactly as written, which is helpful if you are copy-pasting examples from AWS labs or tutorials.
