from TTS.api import TTS

# Running a multi-speaker and multi-lingual model

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)
"""
# Run TTS
# Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
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
def YourTTS(text_to_read, speech_to_mimic, location_to_save_output):
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=True, gpu=False)
    tts.tts_to_file(text_to_read, speaker_wav=speech_to_mimic, language="en", file_path=location_to_save_output)

def test_great_gatsby():
    text_to_read = "Chapter 2 of 'The Great Gatsby' begins with Nick Carraway, the narrator, describing the valley of ashes, \
                    a desolate and industrial area between West Egg and New York City. Nick visits Tom Buchanan, his wealthy \
                    and unfaithful cousin, at his mistress's apartment in New York. Tom introduces Nick to Myrtle Wilson, his mistress, and her sister Catherine.\
                    Tom and Myrtle, along with Nick and some others, take a train to New York City, where they continue to drink \
                    and party. They eventually end up at the apartment of Tom's friends, the McKees. Myrtle becomes increasingly drunk\
                    and begins to talk loudly and flirt with Tom, much to Nick's discomfort.\
                    As the night wears on, Tom becomes increasingly aggressive and hostile, leading to a physical altercation between \
                    him and Myrtle. The party eventually comes to an end, and Nick is left to reflect on the destructive nature of Tom's \
                    affair and the decadence and moral decay of the wealthy elite. The chapter ends with Nick returning to his small cottage \
                    in West Egg, feeling disillusioned with the world he has encountered in New York."
    speech_to_mimic = "/Users/samzorpette/Desktop/memory lane/input audio/greatgatsby_02_fitzgerald_64kb.mp3"
    location_to_save_output = "/Users/samzorpette/Desktop/memory lane/output/great_gatsby_test2/out.wav"
    YourTTS(text_to_read, speech_to_mimic, location_to_save_output)

def test_the_invisible_man():
    text_to_read = "Chapter 1: The novel begins with an unnamed stranger arriving at the Coach and Horses Inn in Iping, a small town in Sussex, England. The stranger is wrapped in bandages and wears a hat and goggles to conceal his face. He takes a room at the inn and begins conducting strange experiments in his room. The innkeeper's wife, Mrs. Hall, becomes suspicious of the stranger's behavior and tries to investigate. However, the stranger becomes violent and refuses to reveal his identity or the nature of his experiments.\
                    Chapter 2: The next morning, the stranger is still in his room and refuses to come out. Mrs. Hall brings him breakfast, but he throws it against the wall. She also notices that his clothes and bandages are covered in blood. Eventually, the stranger comes out of his room and reveals that he has made himself invisible through a scientific experiment. He tells Mrs. Hall that he needs to conduct further experiments to reverse the process and become visible again."
    speech_to_mimic = "/Users/samzorpette/Desktop/memory lane/input audio/invisible_man_01-02_wells_64kb.mp3"
    location_to_save_output = "/Users/samzorpette/Desktop/memory lane/output/the_invisible_man_test3/out.wav"
    YourTTS(text_to_read, speech_to_mimic, location_to_save_output)

test_the_invisible_man()