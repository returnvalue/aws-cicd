# Lab 4: Provisioning Deployment Targets (EC2)

**Goal:** We need servers to deploy our application to. We will provision a simulated EC2 instance and tag it with `Environment=Dev`. CodeDeploy will use this tag to know where to install the code.

```bash
# 1. Fetch a valid AMI ID
AMI_ID=$(awslocal ec2 describe-images --query 'Images[0].ImageId' --output text)

# 2. Launch an EC2 instance and Tag it
awslocal ec2 run-instances \
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
