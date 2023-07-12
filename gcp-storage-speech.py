import io
from google.oauth2 import service_account
from google.cloud import speech

client_file = r'C:\Users\mande\python\pythonVenv\speech-to-text_demo\sa_speech_demo.json'
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

gcs_uri='gs://speech_text_demo_bucket/speech_to_text_demo_recording.wav'
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    enable_automatic_punctuation=True,
    audio_channel_count=2,
    sample_rate_hertz=48000,
    language_code="en-US",
    use_enhanced=True,
    model="video"
)

audio = speech.RecognitionAudio(uri=gcs_uri)
operation = client.long_running_recognize(config=config, audio=audio)

print("waiting for operation to complete...")
#if file more than 5 minutes then increase the timeout 
response = operation.result(timeout=120)
for result in response.results:
    print(result.alternatives[0].transcript)

