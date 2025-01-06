# 環境変数に
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY
# AWS_S3_BUCKET
# を設定しておく。

# 参考URL
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/start_transcription_job.html#

import os
import datetime
import time
import uuid

import boto3


AWS_S3_BUCKET = os.environ["AWS_S3_BUCKET"]

target_filepath = "sample.mp4"
target_filename = os.path.basename(target_filepath)
extension = target_filename.split(".")[-1]
s3_upload_file_key = f"movie/{target_filename}"
update_file_uri = f"s3://{AWS_S3_BUCKET}/{s3_upload_file_key}"
transcription_jobname = f"transcription-test-{uuid.uuid4()}"

s3_client = boto3.client("s3")
transcribe_client = boto3.client("transcribe")

print("S3アップロード処理開始")
start = datetime.datetime.now()

s3_client.upload_file(target_filepath, AWS_S3_BUCKET, s3_upload_file_key)

print("S3アップロード処理終了")
end = datetime.datetime.now()

print(f"S3アップロード処理時間: {end - start}")

print("書き下し開始")
start = datetime.datetime.now()

transcribe_client.start_transcription_job(
  TranscriptionJobName=transcription_jobname,
  Media={
    "MediaFileUri": update_file_uri
  },
  MediaFormat=extension,
  LanguageCode="ja-JP",
  Settings={
    "ShowSpeakerLabels": True, # 話者識別
    "MaxSpeakerLabels": 2 # 最大話者数
  },
  # Subtitles= { # 字幕設定、有名な字幕のファイル形式にすることができるが、AWS Transcribeでは話者識別の情報が落とされてしまう模様
  #   "Formats": ["srt"], # vtt(WebVTT) or srt(SubRip)
  #   "OutputStartIndex": 1 # AWS Transcribeのデフォルトだと「0」だが、一般的には「1」から始まるので「1」推奨
  # }
)

count = 10 
while count > 0:
  count -= 1

  job = transcribe_client.get_transcription_job(TranscriptionJobName=transcription_jobname)
  job_status = job["TranscriptionJob"]["TranscriptionJobStatus"]
  if job_status in ["COMPLETED", "FAILED"]:
    print(f"Job {transcription_jobname} is {job_status}.")
    if job_status == "COMPLETED":
      transcription_url = job["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]
      print(f"Download the transcription from {transcription_url}.")
      break
  else:
    print(f"Waiting for {transcription_jobname}. Current status is {job_status}.")
  time.sleep(10)


print("書き下し終了")
end = datetime.datetime.now()

print(f"書き下し実行時間: {end - start}")