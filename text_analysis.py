"""
This is a ML pipeline that takes a 
audio file > transcript > abstract summarization > summarization read back in the user's own voice

"""

from google.cloud import language


def analyze_text_sentiment(text: str):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    print("TEXT SENTIMENT ANALYSIS:")
    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for key, value in results.items():
        print(f"{key:10}: {value}")

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
        

def classify_text(text: str):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.classify_text(document=document)
    print("TEXT CLASSIFICATION:")
    for category in response.categories:
        print("=" * 80)
        print(f"category  : {category.name}")
        print(f"confidence: {category.confidence:.0%}")
        

def run_all(text):
    analyze_text_sentiment(text)
    analyze_text_entities(text)
    analyze_text_syntax(text)
    classify_text(text)

bonnie_runnels_transcript_example="My name is Regent Nur, I am 16 years old. Today is November 25th and I'm speaking with Bonnie Reynolds, who is my Grandma, we're recording this interview in Arkansas. Can you tell me about one or two people who have been the biggest influences on your life? Well, probably my parents cuz they worked so hard and We're poor but but we never felt for anything. We didn't know we were poor. So they had a big influence and probably my family. Very impressed by my family. They're all hard workers. Can you tell me about the dumbest thing you ever did in your life? If you would like to answer that? I did not go to college right after high school and that was the dumbest thing I've ever done. So later after I married, I took College courses. Wherever we lived took classes at Indiana University. In Sacramento, State and University of Arkansas, and probably a couple more places but I wish I had gone right after high school. I feel like I missed a college last that way. What jobs did you have? When you were a teenager, how are your first job, probably working in a little grocery store on the corner of our street, cleaning shelves. And Stalking things and waiting on customers. Can you tell me about some of the most important lessons you've learned in life or 10, most important lessons to treat people kindly, and to respect everyone's opinion. So you don't have to agree with people, but you have to be civil and Agree to disagree and not be hateful about your disagreements. I agree with you. Your husband, Brian. We met on a summer vacation. In South Bend, Indiana. I went back to visit my cousins, who I, I grew up in South Bend, but we moved to California when I was 12. So, I went back for vacation and he was dating my cousin on and off when he was home from Purdue and I met him and we decided to date instead of and he got My cousin a date from double dated, and it's all history after that. What are you most grateful for my family? The love of my family. I couldn't be happier. Couldn't have picked better people and I'm just so fortunate for that and that we live, where we live. All right. Last one. What advice would you give to your teenage self? If you could go back and do it over again? Don't worry about what other people think of you and be a leader, not a follower. Thank you, Grandma. You're welcome. Thank you for interview."

def bonnie_runnels_test_all():
    run_all(bonnie_runnels_transcript_example)
