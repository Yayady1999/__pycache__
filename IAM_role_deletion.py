import boto3

# Initialize the Boto3 IAM client
iam_client = boto3.client('iam')

# Specify the name of the IAM role you want to delete
role_name = 'YOUR_ROLE_NAME'

# Delete the IAM role
try:
    iam_client.delete_role(RoleName=role_name)
    print(f"IAM role '{role_name}' has been deleted.")
except iam_client.exceptions.NoSuchEntityException:
    print(f"IAM role '{role_name}' does not exist.")
except Exception as e:
    print(f"An error occurred while deleting IAM role '{role_name}': {e}")
