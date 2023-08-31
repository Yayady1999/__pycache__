import boto3

client = boto3.client('cloudformation')

response = client.list_stacks(
    StackStatusFilter=[
        'CREATE_COMPLETE'      #check and add more status if req
    ]
)



dict =(response['StackSummaries'])     # you can take this dict value and then extract the variable to get the name and then delete


#stack summaries in direcrtly called now, next think how to call Keys
#Key: value

#print(dict['StackId'])   works but some error ......need to debug

for key, value in dict.items():
    # Is condition satisfied?
    if key == 'StackName':
        newDict[key] = value