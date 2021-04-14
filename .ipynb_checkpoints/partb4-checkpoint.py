## Part B Task 4
import re
import pandas as pd
import os
import sys
import nltk
from nltk.stem.porter import *
import numpy

new_key_word = sys.argv[1:]
stemmer = PorterStemmer()
list_filename=[]
document_ID=[]
keyword_root = [stemmer.stem(word) for word in new_key_word]

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
    text= pre_process(filename)
    text_List = nltk.word_tokenize(text)
    text_List = [stemmer.stem(word) for word in text_List]
    text_List = ' '.join(text_List)
    i=0
    match = 0
    while i < len(keyword_root):
        if re.search(r'\b'+keyword_root[i].lower()+r'\b',text_List,re.IGNORECASE):
            match += 1
        i += 1
    if match == len(keyword_root):
        list_filename.append(filename)  
document=pd.read_csv('partb1.csv',encoding = 'ISO-8859-1')  
for filename in list_filename:
    document_ID.append(list(document['documentID'][document['filename']==filename]))  
document_ID=list(numpy.array(document_ID).flat)#https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
column_names = ['filename','documentID']
stem_word_document=pd.DataFrame(columns = column_names)
stem_word_document['filename']=list_filename
stem_word_document['documentID']=document_ID
print(document_ID)