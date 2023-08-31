import boto3

# Replace 'your_access_key' and 'your_secret_key' with your AWS credentials.
aws_access_key = 'ASIAQTXTT7A5IEFTEF6R'
aws_secret_key = 'TiCzFpjprn2G7G2AWWWJ1LfnPVPNX3sQIDsHBof2'
aws_session_token = 'FwoGZXIvYXdzEHwaDJ9DEl6QIir8ODNsPiK1AVmmg1E84nxSwmYFZpByYCMP2tQLqYiTm7r1JPhAB0PC6gvjIoueIciNEH881lv5QtFo3NoByFFbFOQ7ODn6ZxfYitP6U7FG0Pp05oTfHxToj4LtfikJ/2spIHvKrz6rgO3sm4qtDSnw1HhkTAbqFwq51SU2aW9rFqXWQg6zOXwqilu/S2rVgBY695Lzlpds82+R1u0vmEI6ok9DxdWmhy+lz6FJXP33Mxf0TwsQ51tcMdR2VBcojbiepwYyLQ0s9PufKtxAZJwczpRksDAJ4tp8jo/fNre8jwuxduOiBbvzw3Gq7wHI8/j4cw=='
# Replace 'your_region' with your desired AWS region.
aws_region = 'eu-central-1'

# Replace 'your_account_number' with the account number you're looking for.
account_number = '510378530068'

def get_stacks_with_account_parameter(account_number):
    # Create a Boto3 CloudFormation client
    client = boto3.client('cloudformation', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    # List all CloudFormation stacks
    response = client.list_stacks(StackStatusFilter=['CREATE_COMPLETE'])

    for stack in response['StackSummaries']:
        stack_name = stack['StackName']

        # Describe the stack to get its parameters
        stack_description = client.describe_stacks(StackName=stack_name)

        if 'Parameters' in stack_description['Stacks'][0]:
            parameters = stack_description['Stacks'][0]['Parameters']

            for parameter in parameters:
                if parameter['ParameterKey'] == 'AccountNumber' and parameter['ParameterValue'] == account_number:
                    print(f"Stack Name: {stack_name}")

if __name__ == "__main__":
    get_stacks_with_account_parameter(account_number)
