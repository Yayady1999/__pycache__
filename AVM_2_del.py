import boto3

# Initialize the Boto3 CloudFormation client
cf_client = boto3.client('cloudformation')

# Specify the target account ID you want to search for
target_account_id = '304184195773'

# List all the CloudFormation stacks with a status filter
status_filter = ['CREATE_COMPLETE', 'UPDATE_COMPLETE', 'ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE']
response = cf_client.list_stacks(StackStatusFilter=status_filter)

# Iterate through the stacks
for stack_summary in response['StackSummaries']:
    stack_name = stack_summary['StackName']

    try:
        # Describe the stack to get its details
        stack_details = cf_client.describe_stacks(StackName=stack_name)

        # Extract the 'Outputs' field from the stack details
        if 'Outputs' in stack_details['Stacks'][0]:
            outputs = stack_details['Stacks'][0]['Outputs']

            # Iterate through the outputs to find 'BubbleAccountId'
            for output in outputs:
                if output['OutputKey'] == 'BubbleAccountId':
                    bubble_account_id = output['OutputValue']

                    # Check if the 'BubbleAccountId' matches the target account ID
                    if bubble_account_id == target_account_id:
                        print(f"Stack Name with 'BubbleAccountId' matching target: {stack_name}")
                        break

    except Exception as e:
        # Log the exception for debugging
        print(f"Error processing stack {stack_name}: {str(e)}")
