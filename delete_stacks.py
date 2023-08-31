import boto3

client = boto3.client('cloudformation')

response = client.delete_stack(
    StackName='bubble-vpc'                    # bubble-vpc
    
)




#termination protection


# try catch impl for this with the Op
# create a class and define  a func within it
# parameterize the stack name