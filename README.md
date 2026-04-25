# AWS CI/CD Pipeline Labs (LocalStack Pro)

![AWS](https://img.shields.io/badge/AWS-CI/CD_Pipeline-FF9900?style=for-the-badge&logo=amazonaws)
![LocalStack](https://img.shields.io/badge/LocalStack-Pro-000000?style=for-the-badge)

This repository contains hands-on labs demonstrating core AWS DevOps concepts, from source control and automated builds to continuous deployment and orchestration. Using [LocalStack Pro](https://localstack.cloud/), we simulate a complete AWS CI/CD environment locally.

## 🎯 Architecture Goals & Use Cases Covered
Based on AWS best practices (SAA-C03), these labs cover:
* **Source Control:** Managing private Git repositories with Amazon CodeCommit.
* **Pipeline Infrastructure:** Provisioning S3 artifact storage and IAM service roles.
* **Continuous Integration:** Automating builds and tests with AWS CodeBuild.
* **Deployment Targets:** Provisioning and tagging EC2 instances for automated deployments.
* **Continuous Deployment:** Automating application updates with AWS CodeDeploy.
* **Pipeline Orchestration:** Linking stages together with AWS CodePipeline for full automation.
* **Monitoring & Execution:** Triggering and tracking real-time pipeline status.
* **Infrastructure as Code:** (Upcoming) Automating resource provisioning within the pipeline.

## ⚙️ Prerequisites

* [Docker](https://docs.docker.com/get-docker/) & Docker Compose
* [LocalStack Pro](https://app.localstack.cloud/) account and Auth Token
* [`awslocal` CLI](https://github.com/localstack/awscli-local) (a wrapper around the AWS CLI for LocalStack)

## 🚀 Environment Setup

1. Configure your LocalStack Auth Token in `.env`:
   ```bash
   echo "YOUR_TOKEN=your_auth_token_here" > .env
   
```

2. Start LocalStack Pro:
   ```bash
   docker-compose up -d
   
```

> [!IMPORTANT]
> **Cumulative Architecture:** These labs are designed as a cumulative scenario. You are building an evolving CI/CD infrastructure.
>
> **Session Persistence:** These labs rely on bash variables (like `$BUILD_ROLE`, `$PIPELINE_ROLE`, `$DEPLOY_ROLE`, etc.). Run all commands in the same terminal session to maintain context.

## 📚 Labs Index
1. [Lab 1: Source Control (AWS CodeCommit)](./labs/lab1-codecommit-repo/README.md)
2. [Lab 2: Artifact Storage & IAM Foundations](./labs/lab2-artifacts-iam/README.md)
3. [Lab 3: Continuous Integration (AWS CodeBuild)](./labs/lab3-codebuild-project/README.md)
4. [Lab 4: Provisioning Deployment Targets (EC2)](./labs/lab4-ec2-deployment-target/README.md)
5. [Lab 5: Continuous Deployment (AWS CodeDeploy)](./labs/lab5-codedeploy-setup/README.md)
6. [Lab 6: Pipeline Orchestration (AWS CodePipeline)](./labs/lab6-codepipeline-orchestration/README.md)
7. [Lab 7: Pipeline Execution & Monitoring](./labs/lab7-pipeline-monitoring/README.md)

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
