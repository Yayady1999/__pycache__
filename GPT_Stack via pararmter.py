import boto3

# Initialize the Boto3 CloudFormation client
cf_client = boto3.client('cloudformation')

# List all the CloudFormation stacks
response = cf_client.list_stacks(StackStatusFilter=[])

# Print the list of stacks
print("List of CloudFormation Stacks:")
for stack_summary in response['StackSummaries']:
    print("Stack Name:", stack_summary['StackName'])
    print("Stack Status:", stack_summary['StackStatus'])
    print("Stack Creation Time:", stack_summary['CreationTime'])
    print("----------------------")
