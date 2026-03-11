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
* **Continuous Deployment:** (Upcoming) Automating application updates with AWS CodeDeploy.
* **Pipeline Orchestration:** (Upcoming) Linking stages together with AWS CodePipeline.
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
> **Session Persistence:** These labs rely on bash variables (like `$BUILD_ROLE`, `$PIPELINE_ROLE`, `$AMI_ID`, etc.). Run all commands in the same terminal session to maintain context.

## 📚 Labs Index
1. [Lab 1: Source Control (AWS CodeCommit)](./labs/lab1-codecommit-repo/README.md)
2. [Lab 2: Artifact Storage & IAM Foundations](./labs/lab2-artifacts-iam/README.md)
3. [Lab 3: Continuous Integration (AWS CodeBuild)](./labs/lab3-codebuild-project/README.md)
4. [Lab 4: Provisioning Deployment Targets (EC2)](./labs/lab4-ec2-deployment-target/README.md)
