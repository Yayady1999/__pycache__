import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('test1')


resp = table.delete_item(
    Key={
        'id': 3
    }
)