import boto3

client = boto3.client('cloudformation')

#Enter the bubble number
#The bubble number will be assigned to string to match the naming convention

b = 962139409500             #This value must be the acc number that we have to delete


c= str(b)
a='DSBA-ECAS-security-baseline'
name=a+c
response = client.list_stack_resources(
    StackName= name
)

print(response)     