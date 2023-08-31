import boto3

# Initialize the Boto3 CloudFormation client
cf_client = boto3.client('cloudformation')

# Specify the string you want to search for in stack names
target_string = '978908609334'

# List all the CloudFormation stacks
response = cf_client.list_stacks(StackStatusFilter=[])

# Print the list of stacks that contain the target string in their name
print(f"List of CloudFormation Stacks containing '{target_string}' in their name:")
for stack_summary in response['StackSummaries']:
    stack_name = stack_summary['StackName']
    if target_string in stack_name:
        print("Stack Name:", stack_name)
        print("Stack Status:", stack_summary['StackStatus'])
        print("Stack Creation Time:", stack_summary['CreationTime'])
        print("----------------------")
