import boto3

polly_client = boto3.client("polly")

response = polly_client.synthesize_speech(
    Text="こんにちは、よろしくね。",
    TextType="text",
    LanguageCode="ja-JP",
    OutputFormat="mp3",
    VoiceId="Mizuki",
)

binary_data = response["AudioStream"].read()
with open("output.mp3", "wb") as file:
    file.write(binary_data)