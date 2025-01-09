import json

target_file = "result.json"

with open(target_file, "r") as f:
  transcription_data = json.load(f)

audio_segments = transcription_data["results"]["audio_segments"]

with open("transcript.vtt", "w") as f:
  f.write("WEBVTT\n\n")

  speaker_label = "spk_0"
  start_time = audio_segments[0]["start_time"]
  transcript = ""
  for tmp_audio_segment in audio_segments:
    tmp_speaker_label = tmp_audio_segment["speaker_label"]
    if tmp_speaker_label != speaker_label:
      f.write(f"{start_time} ---> {end_time}\n")
      f.write(transcript + "\n")
      f.write("\n")

      speaker_label = tmp_speaker_label
      start_time = tmp_audio_segment["start_time"]
      end_time = tmp_audio_segment["end_time"]
      transcript = tmp_audio_segment["transcript"]
    else:
      end_time = tmp_audio_segment["end_time"]
      transcript += tmp_audio_segment["transcript"]
  
  f.write(f"{start_time} ---> {end_time}\n")
  f.write(transcript + "\n")
  f.write("\n")
