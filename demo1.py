#taking a audio file from local and using gcp speech to text service
import io
from google.oauth2 import service_account
from google.cloud import speech

client_file = r'C:\Users\mande\python\pythonVenv\speech-to-text_demo\sa_speech_demo.json'
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

#load audio file
  
audio_file_name = r'C:\Users\mande\python\pythonVenv\speech-to-text_demo\speech_to_text_demo_recording.wav'
with io.open(audio_file_name, 'rb') as f:
    content = f.read()
    audio = speech.RecognitionAudio(content=content)


config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    enable_automatic_punctuation=True,
    audio_channel_count=2,
    sample_rate_hertz=48000,
    language_code="en-US",
    use_enhanced=True,
    model="video"
)

#print(frame_rate_channel(r'C:\Users\mande\python\pythonVenv\speech-to-text_demo\speech_to_text_demo_recording.wav'))
response = client.recognize(config=config, audio=audio)
for result in response.results:
    print(result.alternatives[0].transcript)