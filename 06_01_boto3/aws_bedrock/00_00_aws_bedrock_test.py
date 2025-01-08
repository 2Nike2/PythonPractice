# 環境変数に
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY
# AWS_S3_BUCKET
# を設定しておく。

# 参考URL
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/converse.html#


import boto3

bedrock_client = boto3.client("bedrock-runtime", region_name="ap-northeast-1")
model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"

conversation = [
  {"role": "user", "content": [{"text": "こんにちは、よろしくね。"}]}
]

response = bedrock_client.converse(
  modelId=model_id,
  messages=conversation,
  system=[{"text": "日本語で応答してください。"}],
  inferenceConfig={"maxTokens": 512, "temperature": 0.8, "topP": 0.9},
)

response_text = response["output"]["message"]["content"][0]["text"]

print(response_text)