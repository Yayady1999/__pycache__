import boto3

# Create a Boto3 CloudFormation client
cf_client = boto3.client('cloudformation')

# List all stacks
response = cf_client.list_stacks()

# Search keywords
search_keywords = ["RCN", "rcn"]

# Initialize a flag to check if any stack contains the search keyword
found = False

# Iterate through the stack summaries
for stack in response['StackSummaries']:
    stack_name = stack['StackName']
    stack_status = stack['StackStatus']
    
    # Check if any of the search keywords are in the stack name
    if any(keyword in stack_name for keyword in search_keywords):
        print(f"Stack Name: {stack_name}")
        print(f"Stack Status: {stack_status}\n")
        found = True

# Check if no stack names contained the search keywords
if not found:
    print("No RCN")
