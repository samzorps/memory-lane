"""
This is a ML pipeline that takes a 
audio file > transcript > abstract summarization > summarization read back in the user's own voice

SETUP:
1. Activate virtual enviornment 
- in terminal run:
source venv/bin/activate

2. Authenticate google cloud 
- setup service account and download private key json file
- set enviornment variable which stores the location of private key. Change the path/to/keyfile.json and run this:
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"

- setting audio file: example - gs://cloud-samples-data/speech/brooklyn_bridge.flac

"""
from google.cloud import datastore
from google.cloud import speech

def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        #encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        #sample_rate_hertz=16000,
        #speech_contexts=, 
        #enable_word_time_offsets=, 
        #alternative_language_codes="",
        #audio_channel_count=2,
        enable_automatic_punctuation=True,
        language_code="en-US",

    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=36000) # TIMEOUT SET TO 10 MINUTES - TESTING ONLY

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    print(response) # TESTING
    total_transcript=""
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print("Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))
        total_transcript += result.alternatives[0].transcript
    print(total_transcript)
    return total_transcript


 
# Google cloud authentication, uses enviornment variable set in setup
client = datastore.Client()

def gcloud_example_audio_test():
    # example file 
    gcloud_example_audio = "gs://cloud-samples-data/speech/brooklyn_bridge.flac"
    res = transcribe_gcs(gcloud_example_audio)
    return res

def bonnie_runnels_audio_test():
    # example from storycorps in storage
    bonnie_runnels_example_audio = "gs://test_audio_memory_lane/BonnieRunnels.flac"
    res = transcribe_gcs(bonnie_runnels_example_audio)
    return res

def bonnie_clyde_trudy_henry_test():
    # 6 min, one speaker audio from storycorps
    res = transcribe_gcs("gs://test_audio_memory_lane/bonnie_clyde_by_Trudy_Henry.flac")
    with open('outfile.txt', 'w') as outfile:
        print >>outfile, res
    return res

def invisible_man_test():
    gcs = "gs://test_audio_memory_lane/invisible_man_01-02_wells_64kb.flac"
    res = transcribe_gcs(gcs)
    return res

invisible_man_test()

