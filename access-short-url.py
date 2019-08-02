import os
import json
import boto3

ddb = boto3.resource('dynamodb', region_name = 'us-east-2').Table('shortened-url-table')

def lambda_handler(event, context):
    print("debug::event content:",event)
    url_id = event.get('urlid')
    print("debug::", url_id)
    try:
        item = ddb.get_item(Key={'url-id': url_id})
        long_url = item.get('Item').get('long_url')
        print("debug::long_url:", long_url)
        # increase the hit number on the db entry of the url (analytics?)
        ddb.update_item(
            Key={'url-id': url_id},
            UpdateExpression='set hits = hits + :val',
            ExpressionAttributeValues={':val': 1}
        )

    except Exception as ex:
        print(ex)
        #Use home page of Baidu as 404 page for exception
        return {
            'statusCode': 301,
            'location': 'http://www.baidu.com'
        }

    return {
        "statusCode": 301,
        "location": long_url
    }
