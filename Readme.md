# Memory Lane 

## What it does
This is a machine learning pipeline which inputs spoken audio of a story and generates follow up questions about the story. It also will clone the speakers voice. 

## How it works
This takes an audio file, transcribes it using Google Cloud speech-to-text, summarizes the transcript and generates conversational follow up questions using ChatGPT, and clones the speakers voice using the YourTTS model from 🐸TTS. 

## Why it was made
It was made for memory-lane.ai as a minimum-viable-product. It gut-checked the feasability and cost of what they wanted to do, and help raise their seed round. 

## Read also: 
- model for voice cloning https://github.com/coqui-ai/tts 
- other voice clone projects https://paperswithcode.com/task/speech-synthesis/ 
- models for speech to text, summarization, NLP https://github.com/huggingface/transformers
- model for speech to text https://github.com/mozilla/DeepSpeech 
- speech datasets https://github.com/jim-schwoebel/voice_datasets 
