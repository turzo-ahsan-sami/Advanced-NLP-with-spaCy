# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:06:57 2019

@author: Josh
"""

import spacy

nlp = spacy.load("en_core_web_sm")

text = "New iPhone X release date leaked as Apple reveals pre-orders by mistake"

#Process the text
doc = nlp(text)

#Iterate over the entities
for ent in doc.ents:
    #Print the entity text and label
    print(ent.text, ent.label)
    
#Get the span for "iPhone X"
iphone_x = doc[1:3]

#Print the span text
print("Missing entity:", iphone_x.text)