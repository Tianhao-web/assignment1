
## Part B Task 3
import re
import sys
import pandas as pd
import nltk
import os
import numpy

keyword=sys.argv[1:]
list_filename=[]
document_ID=[]

def pre_process(filename):
    with open('cricket/'+filename, "r") as a_file:
        text = a_file.read()
        text = re.sub(r'\d|\W',r' ',text)
        text = re.sub(r' +', r' ', text)
        text = text.lower()
    return text
for filename in os.listdir('cricket'):
    if filename == '.ipynb_checkpoints':
        continue
    text = pre_process(filename)
    i=0
    match = 0
    while i < len(keyword):
        if re.search(r'\b'+keyword[i].lower()+r'\b',text,re.IGNORECASE):
            match += 1
        i += 1
    if match == len(keyword):
        list_filename.append(filename)  
document=pd.read_csv('partb1.csv',encoding = 'ISO-8859-1')        
for file in list_filename:
    document_ID.append(list(document['documentID'][document['filename']==file]))  
document_ID=list(numpy.array(document_ID).flat)#https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
print(document_ID)