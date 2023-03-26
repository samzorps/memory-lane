from speech_transcription import bonnie_runnels_audio_test, gcloud_example_audio_test, bonnie_clyde_trudy_henry_test
from text_analysis import bonnie_runnels_test_all, run_all
from text_summarization import summarize
from mimic_voice import YourTTS


transcript = bonnie_clyde_trudy_henry_test()

analysis = run_all(transcript)

split_response = summarize(transcript)

YourTTS(text_to_read, speech_to_mimic, location_to_save_output)