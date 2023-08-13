# Memory Lane 

## What it does
This is a machine learning pipeline which inputs spoken audio of a story and generates follow up questions about the story. It also will clone the speakers voice and read back a summary of their story with the cloned voice.


## How it works
This takes an audio file, transcribes it using Google Cloud speech-to-text, summarizes the transcript and generates conversational follow up questions using ChatGPT, and clones the speakers voice using the YourTTS model from 🐸TTS. 


## Why it was made
It was made for [memory-lane.ai](memory-lane.ai) as a minimum-viable-product (MVP) for their core product. It gut-checked the feasability and cost of what they wanted to do, and helped raise their seed round. 


## Instructions for use
1. Activate virtual enviornment. Open a terminal and type the following command: source venv/bin/activate

2. Authenticate Google Cloud 
- Setup service account and download private key json file
- Set enviornment variable which stores the location of private key by running the following in your terminal:
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"

3. Authenticate OpenAI
- Inside the file text_summarization.py, set openai.api_key_path to the path to the file which contains the api key
- Example: openai.api_key_path = "path/to/secret_key/openai.txt"

4. Run main.py
- change the variable in main.py to the audio file you would like to use (Local or in Google Cloud) and run main.py

## Read also: 
- model for voice cloning https://github.com/coqui-ai/tts 
- other voice clone projects https://paperswithcode.com/task/speech-synthesis/ 
- models for speech to text, summarization, NLP https://github.com/huggingface/transformers
- model for speech to text https://github.com/mozilla/DeepSpeech 
- speech datasets https://github.com/jim-schwoebel/voice_datasets 
