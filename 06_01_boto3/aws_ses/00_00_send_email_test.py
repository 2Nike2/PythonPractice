import os

import boto3
from dotenv import load_dotenv

load_dotenv()

SES_SOURCE = os.getenv("SES_SOURCE")
SES_DESTINATION = os.getenv("SES_DESTINATION")

send_args = {
  "Source": SES_SOURCE,
  "Destination": {
    "ToAddresses": [
      SES_DESTINATION
    ]
  },
  "Message": {
    "Subject": {"Data": "AWS SES 動作確認"},
    "Body": {
      "Text": {"Data": "AWS SESからのメールです。"},
      "Html": {"Data": "<p>AWS SESからのメールです。</p>"}
    }
  }
}

client = boto3.client("ses", region_name="ap-northeast-1")

response = client.send_email(**send_args)
print(response)