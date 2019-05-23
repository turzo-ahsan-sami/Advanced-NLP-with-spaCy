# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:24:15 2019

@author: Josh
"""

from spacy.lang.en import English

nlp = English()

#Import the Doc and Span classes
from spacy.tokens import Doc, Span

words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True, False]

#Create a doc from the words and spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

#Create a span for "David Bowie" from the doc and assign it the label "PERSON"
span = Span(doc, 2,4, label="PERSON")
print(span.text, span.label_)

#Add the spa to the doc's entities
doc.ents = [span]

#Print the entities' text and labels
print([(ent.text, ent.label_) for ent in doc.ents])