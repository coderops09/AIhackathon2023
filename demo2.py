#using just python module to convert speech to text and not using GCP
import speech_recognition as sr
#from google.oauth2 import service_account
#from google.cloud import speech

#client_file = r'C:\Users\mande\python\pythonVenv\speech-to-text_demo\sa_speech_demo.json'
#credentials = service_account.Credentials.from_service_account_file(client_file)
#client = speech.SpeechClient(credentials=credentials)


audio_file_name = r'C:\Users\mande\python\pythonVenv\speech-to-text_demo\speech_to_text_demo_recording.wav'

#audio = speech.RecognitionAudio(content))

# initialize the recognizer
r = sr.Recognizer()

# open the file
with sr.AudioFile(audio_file_name) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)