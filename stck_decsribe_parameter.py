import boto3

client = boto3.client('CloudFormation.Stack.parameters')

response = client.describe_stacks(
    StackName='SC-080781648294-pp-22uk366nuzaus',
   
)