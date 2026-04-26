# Lab 2: Artifact Storage & IAM Foundations

**Goal:** CodePipeline needs a place to store files as they move between stages. We will create an S3 Artifact Bucket and the foundational IAM Trust Policies for the Build, Deploy, and Pipeline services.
```bash
# 1. Create the S3 Artifact Bucket
awslocal s3api create-bucket --bucket cicd-artifact-store
aws s3api create-bucket --bucket cicd-artifact-store

# 2. Create Trust Policies for Build, Deploy, and Pipeline services
cat <<EOF > build-trust.json
{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"codebuild.amazonaws.com"},"Action":"sts:AssumeRole"}]}
EOF

cat <<EOF > deploy-trust.json
{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"codedeploy.amazonaws.com"},"Action":"sts:AssumeRole"}]}
EOF

cat <<EOF > pipeline-trust.json
{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"codepipeline.amazonaws.com"},"Action":"sts:AssumeRole"}]}
EOF

# 3. Create the IAM Roles
BUILD_ROLE=$(awslocal iam create-role --role-name CodeBuildServiceRole --assume-role-policy-document file://build-trust.json --query 'Role.Arn' --output text)
BUILD_ROLE=$(aws iam create-role --role-name CodeBuildServiceRole --assume-role-policy-document file://build-trust.json --query 'Role.Arn' --output text)
DEPLOY_ROLE=$(awslocal iam create-role --role-name CodeDeployServiceRole --assume-role-policy-document file://deploy-trust.json --query 'Role.Arn' --output text)
DEPLOY_ROLE=$(aws iam create-role --role-name CodeDeployServiceRole --assume-role-policy-document file://deploy-trust.json --query 'Role.Arn' --output text)
PIPELINE_ROLE=$(awslocal iam create-role --role-name CodePipelineServiceRole --assume-role-policy-document file://pipeline-trust.json --query 'Role.Arn' --output text)
PIPELINE_ROLE=$(aws iam create-role --role-name CodePipelineServiceRole --assume-role-policy-document file://pipeline-trust.json --query 'Role.Arn' --output text)
```

## 🧠 Key Concepts & Importance

- **CI/CD Artifacts:** Files such as source code, built binaries, or deployment packages that are passed between different stages of a pipeline.
- **S3 Artifact Bucket:** A secure, centralized storage location used by AWS CodePipeline to maintain state and hand off data between CodeCommit, CodeBuild, and CodeDeploy.
- **Service Roles & Trust Policies:** Each CI/CD service requires an IAM role to perform actions on your behalf. The **Trust Policy** defines which AWS service (e.g., `codebuild.amazonaws.com`) is allowed to "assume" the role and use its permissions.
- **Security Isolation:** By creating separate roles for build, deploy, and orchestration, you adhere to the principle of least privilege, ensuring that a compromise in the build stage doesn't automatically grant access to production deployment resources.

## 🛠️ Command Reference

- `s3api create-bucket`: Creates a new S3 bucket for artifact storage.
- `iam create-role`: Provisions a new IAM role with a specific trust relationship.
    - `--role-name`: The unique name for the service role.
    - `--assume-role-policy-document`: The JSON file defining the trust relationship.

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
