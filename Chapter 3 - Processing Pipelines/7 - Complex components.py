# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:28:08 2019

@author: Josh
"""

import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")
animals = ["Golden Retriever", "cat", "turtle", "Rattus norvegicus"]
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns:", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", None, *animal_patterns)

#Define the custom component
def animal_component(doc):
    #Apply the matcher to the doc
    matches = matcher(doc)
    spans = [Span(doc, start, end, label="ANIMAL") for match_id,
             start, end, in matches]
    #Overwrite the doc.ents with matched spans
    doc.ents = spans
    return doc
    
#Add the component to the pipeline aafter the 'ner' component
nlp.add_pipe(animal_component, last=True)
print(nlp.pipe_names)

#Process the text and print the text and label for doc.ents
doc = nlp("I have a cat and a Golden Retriever")
print([(ent.text, ent.label_) for ent in doc.ents])