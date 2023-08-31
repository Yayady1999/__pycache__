import boto3

client = boto3.client('cloudformation')

response = client.list_stacks(
    StackStatusFilter=[
        'CREATE_COMPLETE'      #check and add more status if req
    ]
)
print(response)    # you can take this dict value and then extract the variable to get the name and then delete
