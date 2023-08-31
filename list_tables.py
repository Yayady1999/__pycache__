import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

tables = list(dynamodb.tables.all())
print(tables)