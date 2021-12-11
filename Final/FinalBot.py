import nltk
from nltk.corpus import stopwords
import random
import string


Goodby_Statements=("Hope to see you agean.","I've had a nice chat.","I've enjoyed our chat")
stop_words= stopwords.words('english')
askforinfo=("Please teach me about","Could you tell me about", "Please explain", "I'd like to learn about")
different=("Let's talk about something else.", "Let's move to a diffrent topic.","Can you explane someting else.")
nowords=("I don't understand.","I don't know what to ask about.", "Hmmm...I'll have to think about that.")

def goodbye():
    print(random.choice(Goodby_Statements),"\nGoodbye.\n")
    return

def chop(input):
    input=nltk.word_tokenize(input)
    text = [w for w in input if not w.lower() in stop_words]
    text = [w for w in text if not w.lower() in string.punctuation]
    #text=nltk.pos_tag(text)
    return text
Remembered_Words=[]
check=True
print("Hello I am chatbot,\n",random.choice(askforinfo),"about any info")
while check:
    taco = input("\nOr say goodbye to end\n")
    if taco.lower()=="goodbye":
        check=False
    elif len(taco) == 0 or taco.lower=="no":
            print("Ok,",random.choice(different), random.choice(askforinfo), "\n")
    else:
        #[w for w in input if not w.lower() in stop_words]
        tacof=[w for w in chop(taco) if not w.lower() in Remembered_Words]
        if len(tacof) == 0:
            print(random.choice(nowords), random.choice(askforinfo), "something else","\n")
        else:
            word=random.choice(tacof)
            Remembered_Words.append(word.lower())
            print(random.choice(askforinfo),word)
        
goodbye()

