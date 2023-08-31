import boto3

# Create a client for the AWS CloudFormation service.
client = boto3.client('cloudformation')

# Get a list of all stacks in the current region.
stacks = client.list_stacks()

# Print the name of each stack.
for stack in stacks['Stacks']:
    print(stack['StackName'])