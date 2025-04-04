"""Entry point for Lambda Function."""

import json

import boto3


def lambda_handler(event, context):
    """Handle AWS Lambda function requests for binary data.

    Parameters
    ----------
    event : dict
        AWS Lambda event object
    context : object
        AWS Lambda context object

    Returns
    -------
    dict
        Response containing binary data with HTTP headers

    """
    print(json.dumps(event))

    bins = ""

    db = boto3.client("dynamodb")

    item = db.get_item(TableName="binaries", Key={"sketch": {"S": "clock"}, "shard": {"N": "0"}})

    shards = item["Item"]["shards"]["N"]
    print(f" There are {shards} shards to this")

    for shard in range(1, int(shards) + 1):
        item = db.get_item(TableName="binaries", Key={"sketch": {"S": "clock"}, "shard": {"N": str(shard)}})
        bins += str(item["Item"]["data"]["B"], "utf-8")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "binary/octet-stream"},
        "body": bins,
        "isBase64Encoded": True,
    }
