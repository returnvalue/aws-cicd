# Lab 7: Pipeline Execution & Monitoring

**Goal:** Manually trigger the pipeline to simulate a developer pushing code, and check the real-time execution status of each stage to ensure successful delivery.

```bash
# 1. Start a pipeline execution
awslocal codepipeline start-pipeline-execution \
  --name 'WebApp-CI-CD-Pipeline'
aws codepipeline start-pipeline-execution \
  --name 'WebApp-CI-CD-Pipeline'

echo 'Pipeline triggered! Waiting 5 seconds for the orchestration engine to spin up...'
sleep 5

# 2. Check the real-time state of all pipeline stages
awslocal codepipeline get-pipeline-state \
  --name 'WebApp-CI-CD-Pipeline' \
  --query 'stageStates[*].{Stage:stageName, Status:latestExecution.status}' \
  --output table
aws codepipeline get-pipeline-state \
  --name 'WebApp-CI-CD-Pipeline' \
  --query 'stageStates[*].{Stage:stageName, Status:latestExecution.status}' \
  --output table
```

## 🧠 Key Concepts & Importance

- **Pipeline Execution:** An occurrence of the release process. Each execution has its own unique ID and tracks the progress of a set of changes through the pipeline.
- **Manual Triggers:** While pipelines are typically triggered by source code changes (automated), manual triggers are useful for testing, emergency rollbacks, or re-running a failed stage.
- **State Monitoring:** Monitoring the status of each stage (e.g., `InProgress`, `Succeeded`, `Failed`) is critical for visibility into the health of your deployment process.
- **Querying API for Status:** Using the CLI or SDK to query pipeline state allows for integration with custom dashboards, Slack notifications, or automated health checks.
- **End-to-End Validation:** Successfully monitoring an execution proves that the entire chain—from CodeCommit through CodeBuild to CodeDeploy—is correctly configured and operational.

## 🛠️ Command Reference

- `codepipeline start-pipeline-execution`: Triggers the specified pipeline to start running.
    - `--name`: The name of the pipeline to start.
- `codepipeline get-pipeline-state`: Returns information about the state of a pipeline, including the status of each stage.
    - `--name`: The name of the pipeline.
    - `--query`: Filters the output to display only the stage names and their latest execution status.
    - `--output table`: Formats the result as a human-readable table.

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
