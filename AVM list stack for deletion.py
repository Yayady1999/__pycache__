import boto3

# Initialize the Boto3 CloudFormation client
cf_client = boto3.client('cloudformation')

# Specify the target account ID you want to search for
target_account_id = '539103955266'     

# List all the CloudFormation stacks 
response = cf_client.list_stacks(StackStatusFilter=[])

# Iterate through the stacks and check if 'BubbleAccountId' contains the target account ID for deletionj
for stack_summary in response['StackSummaries']:
    stack_name = stack_summary['StackName']
    
    try:
        # Describe the stack to get its details
        stack_details = cf_client.describe_stacks(StackName=stack_name)
        
        # Get the stack details as a string
        stack_details_str = str(stack_details).lower()
        
        # Thi si to check if 'BubbleAccountId'   contains the target account ID
        if target_account_id in stack_details_str:
            print("Stack Name:", stack_name)
    
    except Exception as e:
        # Catch any exception and continue to the next stack
        pass
