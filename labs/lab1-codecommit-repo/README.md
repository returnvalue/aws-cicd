# Lab 1: Source Control (AWS CodeCommit)

**Goal:** Create a secure, private Git repository to hold our application code, `buildspec.yml`, and `appspec.yml` files.

```bash
# Create the CodeCommit repository
REPO_URL=$(awslocal codecommit create-repository \
  --repository-name portfolio-web-app \
  --repository-description "Main repository for the web application" \
  --query 'repositoryMetadata.cloneUrlHttp' --output text)
REPO_URL=$(aws codecommit create-repository \
  --repository-name portfolio-web-app \
  --repository-description "Main repository for the web application" \
  --query 'repositoryMetadata.cloneUrlHttp' --output text)

echo "Repository created at: $REPO_URL"
```

## 🧠 Key Concepts & Importance

- **AWS CodeCommit:** A fully managed source control service that hosts secure Git-based repositories. It makes it easy for teams to collaborate on code in a secure and highly scalable ecosystem.
- **Private Repositories:** Unlike public GitHub repositories, CodeCommit provides private storage for your sensitive application code, accessible only to authorized IAM principals.
- **Git Integration:** CodeCommit supports standard Git commands, allowing you to use your existing local Git tools to commit, branch, and merge code.
- **Security:** Integrated with IAM for fine-grained access control. CodeCommit also encrypts your files in transit and at rest.
- **Foundation for CI/CD:** A source repository is the entry point for any automated pipeline. Changes pushed to the repository typically trigger the build and deploy stages.

## 🛠️ Command Reference

- `codecommit create-repository`: Creates a new CodeCommit repository.
    - `--repository-name`: The name of the repository to create.
    - `--repository-description`: A brief description of the repository.
    - `--query`: Extracts the HTTP clone URL from the response metadata.

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
