import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='test1',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    },
)

print("Table status", table.table_status)