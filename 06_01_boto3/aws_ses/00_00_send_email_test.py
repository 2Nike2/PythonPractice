import os

import boto3
from dotenv import load_dotenv

load_dotenv()

SES_SOURCE = os.getenv("SES_SOURCE")
SES_DESTINATION = os.getenv("SES_DESTINATION")
SES_MAIL_SUBJECT = os.getenv("SES_MAIL_SUBJECT")
SES_MAIL_BODY = os.getenv("SES_MAIL_BODY")

send_args = {
  "Source": SES_SOURCE,
  "Destination": {
    "ToAddresses": [
      SES_DESTINATION
    ]
  },
  "Message": {
    "Subject": {"Data": SES_MAIL_SUBJECT},
    "Body": {
      "Text": {"Data": SES_MAIL_BODY},
      "Html": {"Data": f"<p>{SES_MAIL_BODY}</p>"}
    }
  }
}

client = boto3.client("ses", region_name="ap-northeast-1")

response = client.send_email(**send_args)
print(response)