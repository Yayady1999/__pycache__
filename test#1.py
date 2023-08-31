import boto3

def get_vpc_details(account_number):
    # Assume a role in the target account
    sts_client = boto3.client('sts')
    assumed_role = sts_client.assume_role(
        RoleArn=f"arn:aws:iam::{account_number}:role/YourAssumedRole",
        RoleSessionName="AssumedRoleSession"
    )
    
    # Create a session using the assumed role credentials
    session = boto3.Session(
        aws_access_key_id=assumed_role['Credentials']['AccessKeyId'],
        aws_secret_access_key=assumed_role['Credentials']['SecretAccessKey'],
        aws_session_token=assumed_role['Credentials']['SessionToken']
    )

    # Retrieve VPC details using the session
    ec2_client = session.client('ec2')
    response = ec2_client.describe_vpcs()

    # Process and print the VPC details
    for vpc in response['Vpcs']:
        vpc_id = vpc['VpcId']
        cidr_block = vpc['CidrBlock']
        print(f"VPC ID: {vpc_id}, CIDR Block: {cidr_block}")

# Replace '123456789012' with your desired account number
account_number = '123456789012'
get_vpc_details(account_number)


#run and chanfe name, get the VPC detaisl
