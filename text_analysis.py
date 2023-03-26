"""
This is a ML pipeline that takes a 
audio file > transcript > abstract summarization > summarization read back in the user's own voice

Authenticate google cloud 
- setup service account and download private key json file
- set enviornment variable which stores the location of private key. Change the path/to/keyfile.json and run this:
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"

"""

from google.cloud import language


def analyze_text_sentiment(text: str):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for key, value in results.items():
        print(f"{key:10}: {value}")
    print(response)
    return response

def analyze_text_entities(text: str):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    print("TEXT ENTITY ANALYSIS:")
    for entity in response.entities:
        print("=" * 80)
        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1%}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        for key, value in results.items():
            print(f"{key:15}: {value}")
    return response

def analyze_text_syntax(text: str):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_syntax(document=document)

    line = "{:10}: {}"
    print("TEXT SYNTAX ANALYSIS:")
    print(line.format("sentences", len(response.sentences)))
    print(line.format("tokens", len(response.tokens)))
    for token in response.tokens:
        print(line.format(token.part_of_speech.tag.name, token.text.content))
    return response
        

def classify_text(text: str):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.classify_text(document=document)
    print("TEXT CLASSIFICATION:")
    for category in response.categories:
        print("=" * 80)
        print(f"category  : {category.name}")
        print(f"confidence: {category.confidence:.0%}")
    return response
        

def run_all(text):
    res_analyze_text_sentiment = analyze_text_sentiment(text)
    res_analyze_text_entities = analyze_text_entities(text)
    res_analyze_text_syntax = analyze_text_syntax(text)
    res_classify_text = classify_text(text)
    # with open('outfile.txt', 'w') as outfile:
    #     print >>outfile, "-------------------------1: analyze_text_sentiment-------------------------"
    #     print >>outfile, res_analyze_text_sentiment
    #     print >>outfile, "-------------------------2: analyze_text_entities--------------------------"
    #     print >>outfile, res_analyze_text_entities
    #     print >>outfile, "-------------------------3: analyze_text_syntax----------------------------"
    #     print >>outfile, res_analyze_text_syntax
    #     print >>outfile, "-------------------------4: classify_text----------------------------------"
    #     print >>outfile, res_classify_text

def invisible_man_test():
    the_invisible_man_test = "The Stranger came early in February one, wintry day through a biting wind in the driving snow. The last snowfall of the year over the down walking from bramblecrest railway station and carrying a little black portmanteau in steak left. And he was wrapped up from head to foot and the brim of his soft felt hat. He's every inch of his face but the shiny tip of his nose, how to tell if a gangster, shoulders and chest and added a white Crest to the bed and he can read He staggered into the coach and horses more dead than alive and flung his portmanteau down a fire. He cried in the name of human charity, a room and the fire. He stomped on circus, no form of himself in the ball and followed. Mrs. Hole into head gasket, Paula to strike is bogging. And was that much introduction? That's in a couple of sovereigns. Flung upon the table. He took up his quarters in the oven. Behold Let the Fire and left him there. While she went to prepare my meal with her own hands. I guess to stop a typing in the winter time was an unheard-of piece of luck that loan against to was no Hagler. And she was out to show thyself worthy of her good fortune. Soon as the bacon was well underway, mellieha lymphatic Aid at being burst database by a few Dal, Nick persons of contempt. She carried the cloth plates and glasses into the Parlor and began to lay them with the utmost a clam. What does a fire was burning up briskly? She was surprised to see that. If it does still wore his hat and coat standing with his back to her and staring out of the window at the falling snow in the yard, his glove hands, were clasped behind him and he seemed to be lost in. Thought she noticed that the melting snows, still sprinkle his shoulders draped up on her account. Can I take your hat and coat? So she said and give them a good drawing the kitchen. No, he said without turning. She was not sure she had heard him. I was about to repeat the question. He turned his head and looked at her over his shoulder. I prefer to keep them on. He said with emphasis and she noticed that he wore big blue spectacles with sidelights and had a bush side, risk of his code, call other completely hate his cheeks and face. Very well said. She said, as you like in a bit, the room movie woman, He made no answer. I said turned his face away from her again. I miss his whole feeling this whole conversation with a phone says what? It was time to lay the rest of the table. Things in a quick staccato and whisked out of the room. When she returned, he was still sounding that like a man of studying his back hunched, his collar turned up, his dripping hat, brim turned down hiding his face and he is completely. She put down the eggs and bacon with considerable emphasis and cold. Rather than said to him, your lunch is served Thank you. He said at the same time I'm did not start until she was closing the door. Then he swung around and approached the table, that says Antigua quickness. That she went behind the ball to the kitchen. She had a sound repeated at regular intervals. Check check, check check when the sound of a spoon being rapidly whisked around the basement. Go. She said that I clean forgot that it's her being so long. I wash yourself, finished mixing the mustard. She gave me a few. Verbals tabs for her excessive, slowness. She could cook the ham and eggs laid, the table, and done everything. While midi help, and I'd only succeeded in delaying the mustard and him a new guest and wanting to stay. Then she filled the most apart and putting it with a sentence stating us upon a gold and black tea. Tray converted into the problem. She rapped, I dented prompting. As she did, so who visited moved quickly, so that she got us a glimpse of a white object disappearing behind the table. It would seem, he was picking something from the floor. She rapped down the must oppose on the table that you noticed, the overcoat and has been taken off and put over a chair in front of the fire out a pair of wet boots so I can trust us steel. Fender. she went to these things resolutely I suppose I may have them to dry. Now, she said in a voice that Brooks, no, denial. Leave the Hat set up, visitor, in a muffled voice and turning. She's so he raised his head and was sitting and looking at her. Remember G still gaping at him to surprise to speak? He held a white cloth. It was a 78 brought with him over the lower part of his face, so that his mouth and drawers were completely hidden and that was the reason it was muffled voice. But it was not that would start with Miss his whole. It was the fact that all his full head about his blue glasses, was covered by a white bandage on but another covered, it is leaving not a scrap of his face exposed accepting. Only his pink Peach knows it was bright pink and shiny. Just as is our being at first, he wore a dark brown velvet jacket with a high black new line called that a doctor about his neck. A thick black hair escaping as it could blow in between the cross bandages, projected, incurious tails and horns. Getting him, the strangest appearance. Conceivable is muffled and bandaged head was so unlike what she had anticipated, look for a moment. She was rigid. He did not remove the 7:00 yet, but remains holding it, as she saw a no, with a brown glove hand and regarding her with his inscrutable blue glasses, leave the Hat. He said, speaking very distinctly with a washcloth, The nurse began to recover from the shock that they had received. She placed a hand on the chair Again by the fire. I didn't know. So she began that and she stopped and baptized Thank you. He said Riley glancing from her to the door. Then turn again. I'll have the nice seed right side once she said and can reduce clothes out of the room. She comes to his white suede head and blue goggles again if she was going out of the door but his napkin was stood in front of his face. You should have done it unless she closed the door behind her and her face was eloquent. If I surprised and complexity I never she was the hair. She went quite self to do the kitchen and was too preoccupied to ask many. What you was messing about with. Now, when she got there, the baby just sat and listened to her retreating feet. You don't think wiring it the window before he removed his self, he had and resumed his meal. He took a mouthful glance suspiciously at the window, took another mouthful, then Rose and taking the Sevilla to meet and walk across the room and put the blind down to the top of the white moved into the secured, the lower pains. Just left the room in a toilet. This time, he returned with an easy, add to the table and his meal. The post office have next to door knob duration, or something that misses hole or two, and then bandages to give me TV show. She put on some Moco, I'm folded, the clothes, horse, and extended The Travelers coat upon this and they goggles, why you look more like a diving helmet than a human man. Huggies muffler on the corner of the horse and holding that handkerchief over his mouth all the time. Talking to it. That's his mouth with her to maybe. She turned around us one who suddenly remembers, bless my soul alive. She said going off at a tangent and you done them tight as yet Millie. When mrs. Hold went to clear away the strangers, launch her idea that his mouth must also have been cut or disfigured in the accident. She supposed to have suffered was confirmed that he was smoking a pipe at all the time that she was in the room. He never loosen. The silk Muffler, he had wrapped around the lower part of his face to put the mouthpiece to his lips. If you would not forgetfulness but she's so he glanced at, it doesn't mold it out. He sat in the corner with his back to the window blind and spoke. Now, I haven't eaten and drunk and being comfortably. Warm through with less aggressive, brevity them before the reflection of the file. And to kind of read animation to his big spectacles that they had locked his attitude. I have some luggage, she said at Brambleton station and he asked her, how he could have it? Send about his bandaged head quite politely in acknowledgment of hibernation tomorrow. You said there's no speedia delivery. And seemed quite disappointed when she answered no more. She quite sure. No. Man was a tramp, could go over. This is whole nothing loath. Answer his questions and developed a conversation. It's a steep Road by the downside. She said you, no answer to the question about your trip and then snatching an opening said it was dead for a carriage was upset the year ago and more a gentleman killed, besides his Coachman accidents happen in a moment done. They but the visitor was not to be drawn so easily. They do. He said, through his Muffler, I ain't her quietly through his impenetrable glasses. But they take long enough to get well don't they? It was my sister's son, Tom, just cut it down with a side and tumbled on it in the a field and blessed me. He was 3 months, tied up. There you are me believe it. It's regular given the right of a saucer. I can quite understand that to the president. It was afraid one time that he have to have an operation. You put that bad sir. Visit the Loft abruptly about Kavanaugh, the teaching to B and killing his mouth. Was he, he said you also I know nothing matters of them has had for doing for him, cuz I had my sister being took out with our little one so much. That was bandages to do seven bandages to undo. So that if I might be so bold as to say, so. When you get me some matches into the visitor quite abruptly, my pipe is out. This is hold with pulled up Suddenly. It was sent me rude to him after telling him all she had done, she got 15 for a moment and then remembered the two, sovereigns, and she went to the matches. Thanks. He said, concisely as she put them down until she showed up on her and stayed out of the window again. It was altogether too. Discouraging evidently, he was sensitive on the topic of operations on the bandages. She did not make so bold as to say however after all. But his snubbing way, it imitated her and Lily had a hard time of it that often. The visitor remained in The Parlor until 4 without giving the ghost of an excuse, for an intrusion. the most policy was quite still doing that time as he would seem he sat in the growing Darkness, smoking in the firelight, perhaps dozing Once or twice a curious listening, might have had him at the Coles and to the space of five minutes he was older bull pacing the room. He seemed to be talking to himself. Then the object because he sat down again. "
    #analyze_text_sentiment(the_invisible_man_test)
    #analyze_text_entities(the_invisible_man_test)
    #analyze_text_syntax(the_invisible_man_test)
    classify_text(the_invisible_man_test)


def bonnie_runnels_test_all():
    bonnie_runnels_transcript_example="My name is Regent Nur, I am 16 years old. Today is November 25th and I'm speaking with Bonnie Reynolds, who is my Grandma, we're recording this interview in Arkansas. Can you tell me about one or two people who have been the biggest influences on your life? Well, probably my parents cuz they worked so hard and We're poor but but we never felt for anything. We didn't know we were poor. So they had a big influence and probably my family. Very impressed by my family. They're all hard workers. Can you tell me about the dumbest thing you ever did in your life? If you would like to answer that? I did not go to college right after high school and that was the dumbest thing I've ever done. So later after I married, I took College courses. Wherever we lived took classes at Indiana University. In Sacramento, State and University of Arkansas, and probably a couple more places but I wish I had gone right after high school. I feel like I missed a college last that way. What jobs did you have? When you were a teenager, how are your first job, probably working in a little grocery store on the corner of our street, cleaning shelves. And Stalking things and waiting on customers. Can you tell me about some of the most important lessons you've learned in life or 10, most important lessons to treat people kindly, and to respect everyone's opinion. So you don't have to agree with people, but you have to be civil and Agree to disagree and not be hateful about your disagreements. I agree with you. Your husband, Brian. We met on a summer vacation. In South Bend, Indiana. I went back to visit my cousins, who I, I grew up in South Bend, but we moved to California when I was 12. So, I went back for vacation and he was dating my cousin on and off when he was home from Purdue and I met him and we decided to date instead of and he got My cousin a date from double dated, and it's all history after that. What are you most grateful for my family? The love of my family. I couldn't be happier. Couldn't have picked better people and I'm just so fortunate for that and that we live, where we live. All right. Last one. What advice would you give to your teenage self? If you could go back and do it over again? Don't worry about what other people think of you and be a leader, not a follower. Thank you, Grandma. You're welcome. Thank you for interview."
    run_all(bonnie_runnels_transcript_example)

invisible_man_test()