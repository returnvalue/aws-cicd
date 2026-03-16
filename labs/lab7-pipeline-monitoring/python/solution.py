import boto3
import time

# Configure the CodePipeline client for LocalStack
codepipeline = boto3.client("codepipeline", endpoint_url="http://localhost:4566", region_name="us-east-1")

def solution():
    pipeline_name = "WebApp-CI-CD-Pipeline"

    # 1. Start a pipeline execution
    print(f"Starting execution for pipeline: {pipeline_name}...")
    codepipeline.start_pipeline_execution(name=pipeline_name)

    print("Pipeline triggered! Waiting 5 seconds for status update...")
    time.sleep(5)

    # 2. Check the real-time state
    print("Fetching pipeline state...")
    response = codepipeline.get_pipeline_state(name=pipeline_name)
    
    print(f"{'Stage':<20} | {'Status':<15}")
    print("-" * 38)
    for stage in response.get("stageStates", []):
        stage_name = stage.get("stageName")
        status = stage.get("latestExecution", {}).get("status", "Unknown")
        print(f"{stage_name:<20} | {status:<15}")

if __name__ == "__main__":
    solution()
