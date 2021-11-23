import json
import boto3
from random import randrange


def lambda_handler(event, context):
	client = boto3.resource('dynamodb')
	table = client.Table('WebSocketTest')
	
	# generate random id for dynamodb table
	RandomId = randrange(5)
        return RandomId
	
	# Get Item By Id
	response = table.get_item(
		Key={
			'Id' : RandomId
		}
	)
	
	return {
		'body': response['Item']['NewValue']
	}
