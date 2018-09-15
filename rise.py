import spacy
import requests
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
TXT = open("m1.txt","r")
CON = TXT.read()
doc = nlp(CON.decode("utf-8"))
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
          [child for child in token.children])
def email_alert(first):
    report = {}
    report["value1"] = first
    requests.post("https://maker.ifttt.com/trigger/Alert/with/key/SECRET_KEY", data=report)
email_alert("There is a priority notification in RiSE")
displacy.serve(doc, style='ent')
