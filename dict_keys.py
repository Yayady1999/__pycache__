import boto3

client = boto3.client('cloudformation')

response = client.list_stacks(
    StackStatusFilter=[
        'CREATE_COMPLETE'   #check and add more status if req
    ]
)

newdict = dict()
for key, value in response.items():
    if (key == 'StackStatus') :
       newdict[key]= value
print(newdict)