import boto3

# Get the AWS session
# Make sure to assume the necessary role and its credentials
session = boto3.Session()

# Get the Cloudformation client
client = session.client('cloudformation')

# Get the list of stacks
stacks = client.list_stacks()

# For each stack, delete it
for stack in stacks['Stacks']:
    client.delete_stack(StackName=stack['bubble-vpc'])

#bubble-vpc stack deletion canbe done in this
