import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


#credential_path = "/app/sp2tx/credential/fintech-bd99846f49cd.json"
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = crendential_path
# Instantiates a client
# client = speech.SpeechClient()

# The name of the audio file to transcribe
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'resources',
#     'audio.raw')

# # Loads the audio into memory
# with io.open('/Users/mingshenglyu/Desktop/sample.wav', 'rb') as audio_file:
#     content = audio_file.read()
#     audio = types.RecognitionAudio(content=content)

# config = types.RecognitionConfig(
#     encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz=16000,
#     language_code='zh_TW')

# # Detects speech in the audio file
# response = client.recognize(config, audio)

# for result in response.results:
#     print('Transcript: {}'.format(result.alternatives[0].transcript))

def get_sp2tx(audio_path):

    client = speech.SpeechClient()

    # Loads the audio into memory
    with io.open(audio_path, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='zh_TW')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        return result.alternatives[0].transcript
