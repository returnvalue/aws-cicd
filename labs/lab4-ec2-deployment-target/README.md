# Lab 4: Provisioning Deployment Targets (EC2)

**Goal:** We need servers to deploy our application to. We will provision a simulated EC2 instance and tag it with `Environment=Dev`. CodeDeploy will use this tag to know where to install the code.
```bash
# 1. Fetch a valid AMI ID
AMI_ID=$(awslocal ec2 describe-images --query 'Images[0].ImageId' --output text)
AMI_ID=$(aws ec2 describe-images --query 'Images[0].ImageId' --output text)

# 2. Launch an EC2 instance and Tag it
awslocal ec2 run-instances \
  --image-id $AMI_ID \
  --instance-type 't3.micro' \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Environment,Value=Dev},{Key=Name,Value=WebServer01}]'
aws ec2 run-instances \
  --image-id $AMI_ID \
  --instance-type 't3.micro' \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Environment,Value=Dev},{Key=Name,Value=WebServer01}]'
```

## 🧠 Key Concepts & Importance

- **Deployment Targets:** The physical or virtual servers where your application code is installed and run. In this lab, we use Amazon EC2 instances.
- **Resource Tagging:** A critical mechanism for organizing and managing AWS resources. CodeDeploy uses tags (like `Environment=Dev`) to identify the specific group of instances that should receive a deployment.
- **Dynamic Identification:** Instead of hardcoding IP addresses or instance IDs, tagging allows the pipeline to remain flexible. If you launch new instances with the same tag, they can automatically be included in future deployments.
- **Infrastructure Requirements:** For CodeDeploy to work on EC2, the instances typically need the CodeDeploy Agent installed and an IAM Instance Profile with permissions to read from the artifact S3 bucket.

## 🛠️ Command Reference

- `ec2 describe-images`: Retrieves information about available AMIs.
- `ec2 run-instances`: Launches one or more EC2 instances.
    - `--image-id`: The ID of the AMI to use.
    - `--instance-type`: The compute and memory capacity.
    - `--tag-specifications`: Applies metadata tags to the instance during creation.

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
