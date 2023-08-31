import boto3
import botocore

client = boto3.client('organizations')

response = client.close_account(
    AccountId='962139409500'                     #accID is mandatory for this
)