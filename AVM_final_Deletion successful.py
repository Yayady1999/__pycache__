import boto3

# Specify AWS access key, secret key, and session token
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
aws_session_token = 'YOUR_SESSION_TOKEN'

# Initialize the Boto3 CloudFormation client with credentials
cf_client = boto3.client(
    'cloudformation',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

# Specify the target account ID you want to search for
target_account_id = 'YOUR_TARGET_ACCOUNT_ID'     

# List all the CloudFormation stacks 
response = cf_client.list_stacks(StackStatusFilter=[])

# Iterate through the stacks and check if 'BubbleAccountId' contains the target account ID for deletion
for stack_summary in response['StackSummaries']:
    stack_name = stack_summary['StackName']
    
    try:
        # Describe the stack to get its details
        stack_details = cf_client.describe_stacks(StackName=stack_name)
        
        # Get the stack details as a string
        stack_details_str = str(stack_details).lower()
        
        # Check if 'BubbleAccountId' contains the target account ID
        if target_account_id in stack_details_str:
            print("Stack Name:", stack_name)
            
            # Delete the stack
            cf_client.delete_stack(StackName=stack_name)
            print(f"Stack {stack_name} deleted.")

    except Exception as e:
        # Catch any exception and continue to the next stack
        pass
