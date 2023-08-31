import boto3

client = boto3.client('cloudformation')

response = client.list_stacks(
    StackStatusFilter=[
        'CREATE_COMPLETE'       # The status of the stacks is a mandatory parameter
    ]
)



print[response['StackSummaries'('StackName')]]     # The dict value of all the stacks with their paramters and values are printed in key,value pair format

# try cf = boto3.Session().resource('cloudformation')
#     cf.meta.client.list_stacks(StackStatusFilter=['ROLLBACK_COMPLETE'])