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
