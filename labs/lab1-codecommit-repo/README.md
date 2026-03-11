# Lab 1: Source Control (AWS CodeCommit)

**Goal:** Create a secure, private Git repository to hold our application code, `buildspec.yml`, and `appspec.yml` files.

```bash
# Create the CodeCommit repository
REPO_URL=$(awslocal codecommit create-repository \
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
