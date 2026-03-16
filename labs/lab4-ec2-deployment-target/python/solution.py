import boto3

# Configure the EC2 client for LocalStack
ec2 = boto3.client("ec2", endpoint_url="http://localhost:4566", region_name="us-east-1")

def solution():
    # 1. Fetch a valid AMI ID
    print("Fetching AMI ID...")
    images = ec2.describe_images()
    ami_id = images["Images"][0]["ImageId"]
    print(f"Using AMI: {ami_id}")

    # 2. Launch an EC2 instance and Tag it
    print("Launching EC2 instance...")
    ec2.run_instances(
        ImageId=ami_id,
        InstanceType="t3.micro",
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [
                    {"Key": "Environment", "Value": "Dev"},
                    {"Key": "Name", "Value": "WebServer01"}
                ]
            }
        ]
    )
    print("EC2 instance launched and tagged.")

if __name__ == "__main__":
    solution()
