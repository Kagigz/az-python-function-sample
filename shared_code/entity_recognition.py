import spacy
import en_core_web_sm

def get_entities(text):

    nlp = en_core_web_sm.load()
    doc = nlp(text)
    entities = ""

    for ent in doc.ents:
        entity = "/ %s - %s /" % (ent.text,ent.label_)
        entities = entities + entity

    return entities 