import boto3

client = boto3.client('cloudformation')

response = client.update_termination_protection(
    EnableTerminationProtection=False,       #The staus needs to be set as false in order to delete the stack
    StackName='string'   #This value will be "bubble-vpc"
) 