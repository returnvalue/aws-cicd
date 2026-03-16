import boto3

# Configure the CodeCommit client for LocalStack
codecommit = boto3.client("codecommit", endpoint_url="http://localhost:4566", region_name="us-east-1")

def solution():
    print("Creating CodeCommit repository: portfolio-web-app...")
    response = codecommit.create_repository(
        repositoryName="portfolio-web-app",
        repositoryDescription="Main repository for the web application"
    )
    
    repo_url = response["repositoryMetadata"]["cloneUrlHttp"]
    print(f"Repository created at: {repo_url}")

if __name__ == "__main__":
    solution()
