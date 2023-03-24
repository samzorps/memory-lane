from speech_transcription import bonnie_runnels_audio_test, gcloud_example_audio_test
from text_analysis import bonnie_runnels_test_all, run_all
from text_summarization import summarize

transcript = gcloud_example_audio_test()
run_all(transcript)
response, split_response = summarize(transcript)