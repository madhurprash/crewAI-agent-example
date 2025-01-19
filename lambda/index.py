import json
import tools
import logging

# Configure the root logger
logger = logging.getLogger()
if logger.hasHandlers():
    # Avoid adding multiple handlers in AWS Lambda
    logger.handlers.clear()

# Add a new StreamHandler and set the format
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] p%(process)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Set the logging level
logger.setLevel(logging.INFO)

def handler(event, context):
    # Log the received event
    logger.info("Received event: %s", event)

    # Initialize response code to None
    response_code = None

    # Extract the action group, api path, and parameters
    action = event["actionGroup"]
    logger.info(f"action={action}")
    api_path = event["apiPath"]
    httpMethod = event["httpMethod"]
    logger.info(f"api_path={api_path}")

    body = event.get('requestBody')
    logger.info(f"body={body}")
    if body is None:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': 'content body not present, malformed request'
            })
        }
    # Extract fields
    parameters = body['content']['application/json']['properties']
    query = None
    model_id = None
    for param in parameters:
        if param['name'] == 'query':
            query = param['value']
        if param['name'] == 'model_id':
            model_id = param['value']

    # Validate required fields
    if query is None or model_id is None:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': 'Missing required fields: query and model_id are required'
            })
        }
    logger.info(f"query={query}, model_id={model_id}")

    if api_path == "/gen_code":
        # Call the code_gen_tool from the tools module
        body = tools.gen_code(query, model_id)
        response_body = {"application/json": {"body": str(body)}}
        response_code = 200
    else:
        # Unrecognized api path
        body = {"{}::{} is not a valid api, try another one.".format(action, api_path)}
        response_body = {"application/json": {"body": str(body)}}
        response_code = 400

    # Log the response body
    logger.info("Response body: %s", response_body)

    # Create a dictionary containing the response details
    action_response = {
        "actionGroup": action,
        "apiPath": api_path,
        "httpMethod": httpMethod,
        "httpStatusCode": response_code,
        "responseBody": response_body,
    }

    # Return the final response
    api_response = {"messageVersion": "1.0", "response": action_response}
    return api_response