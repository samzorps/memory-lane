from TTS.api import TTS

# Running a multi-speaker and multi-lingual model

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)
"""
# Run TTS
# ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
# Text to speech with a numpy output
wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])
# Text to speech to a file
tts.tts_to_file(text="Hello world!", speaker=tts.speakers[0], language=tts.languages[0], file_path="output.wav")

# Running a single speaker model

# Init TTS with the target model name
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False, gpu=False)
# Run TTS
tts.tts_to_file(text="Ich bin eine Testnachricht.", file_path=OUTPUT_PATH)
"""
# Example voice cloning with YourTTS in English:
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)
tts.tts_to_file("This is voice cloning. Using about 30 seconds of text from Trudy Henry telling the bonnie and clyde story.", speaker_wav="/Users/samzorpette/Desktop/memory lane/speech audio/bonnie_clyde_by_Trudy_Henry.wav", language="en", file_path="output_trudy_henry.wav")
