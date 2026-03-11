# Lab 5: Continuous Deployment (AWS CodeDeploy)

**Goal:** Create a CodeDeploy Application and a Deployment Group. The Deployment Group tells AWS to look for any EC2 instances tagged with `Environment=Dev` and deploy the code to them using the instructions in the `appspec.yml` file.

```bash
# 1. Create the CodeDeploy Application
awslocal deploy create-application \
  --application-name 'WebAppDeploy' \
  --compute-platform 'Server'

# 2. Create the Deployment Group targeting our EC2 tag
awslocal deploy create-deployment-group \
  --application-name 'WebAppDeploy' \
  --deployment-group-name 'DevDeploymentGroup' \
  --deployment-config-name 'CodeDeployDefault.OneAtATime' \
  --ec2-tag-filters 'Key=Environment,Value=Dev,Type=KEY_AND_VALUE' \
  --service-role-arn $DEPLOY_ROLE
```

## 🧠 Key Concepts & Importance

- **AWS CodeDeploy:** A fully managed deployment service that automates software deployments to various compute services such as Amazon EC2, AWS Fargate, AWS Lambda, and your on-premises servers.
- **Application:** A container that ensures the correct combination of revision, deployment configuration, and deployment group are used during a deployment.
- **Deployment Group:** Defines the set of individual instances or groups of instances to which a revision is deployed. In this lab, we use EC2 tags to define the group.
- **Deployment Configuration:** A set of deployment rules and success/failure conditions used by CodeDeploy during a deployment (e.g., `CodeDeployDefault.OneAtATime` ensures high availability by deploying to one instance at a time).
- **AppSpec File:** A YAML-formatted file used by CodeDeploy to manage a deployment. It defines the files to be installed and the lifecycle event hooks to run (e.g., `BeforeInstall`, `AfterInstall`, `ApplicationStart`).

## 🛠️ Command Reference

- `deploy create-application`: Creates a new CodeDeploy application.
    - `--application-name`: The name of the application.
    - `--compute-platform`: The compute platform on which you want to deploy applications (e.g., `Server`, `Lambda`, or `ECS`).
- `deploy create-deployment-group`: Creates a deployment group to which application revisions will be deployed.
    - `--application-name`: The name of the application associated with the deployment group.
    - `--deployment-group-name`: The name of the deployment group.
    - `--deployment-config-name`: Predefined deployment configuration (e.g., `CodeDeployDefault.OneAtATime`).
    - `--ec2-tag-filters`: The tags used to identify the EC2 instances in this group.
    - `--service-role-arn`: The ARN of the service role that allows CodeDeploy to act on your behalf.
