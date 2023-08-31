import boto3


# Initialize the Boto3 CloudFormation client
cf_client = boto3.client('cloudformation')

# Specify the target number you want to search for
target_number = '304184195773'

# List all the CloudFormation stacks with a status filter
status_filter = ['CREATE_COMPLETE', 'UPDATE_COMPLETE', 'ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE']
response = cf_client.list_stacks(StackStatusFilter=status_filter)

# Initialize a list to store matching stack names
matching_stack_names = []

# Iterate through the stacks
for stack_summary in response['StackSummaries']:
    stack_name = stack_summary['StackName']

    try:
        # Describe the stack to get its details
        stack_details = cf_client.describe_stacks(StackName=stack_name)

        # Check if the 'Outputs' field exists in the stack details
        if 'Outputs' in stack_details['Stacks'][0]:
            outputs = stack_details['Stacks'][0]['Outputs']

            # Iterate through the outputs to find if target_number exists
            for output in outputs:
                if target_number in output['OutputValue']:
                    matching_stack_names.append(stack_name)
                    break

        # Check if the 'Parameters' field exists in the stack details
        if 'Parameters' in stack_details['Stacks'][0]:
            parameters = stack_details['Stacks'][0]['Parameters']

            # Iterate through the parameters to find if target_number exists
            for parameter in parameters:
                if target_number in parameter['ParameterValue']:
                    matching_stack_names.append(stack_name)
                    break

    except Exception as e:
        # Log the exception for debugging
        print(f"Error processing stack {stack_name}: {str(e)}")

# Print the matching stack names
if matching_stack_names:
    print("Matching Stack Names:")
    for stack_name in matching_stack_names:
        print(stack_name)
else:
    print("No matching stacks found.")
