import json
#testado aprovacoes
def lambda_handler(event, context):
    try:
        test=event.get('queryStringParameters')
        id=test.get('id')
    except:
        id = 0
    return {
        'statusCode': 200,
        'body': json.dumps(f'{id}')
        }
