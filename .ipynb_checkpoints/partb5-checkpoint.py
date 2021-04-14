## Part B Task 5
import re
import os
import sys
import pandas as pd
import nltk
import numpy
from numpy import dot
from numpy.linalg import norm
import math
from nltk.stem.porter import *

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

term_counts=[]
tf=[]
for filename in stem_word_document['filename']:
    text= pre_process(filename)
    text_List = nltk.word_tokenize(text)
    text_List = [stemmer.stem(word) for word in text_List]
    text_List = ' '.join(text_List)
    counts=[]
    counts=[text_List.count(x) for x in keyword_root]
    term_frequency=[text_List.count(x)/len(text_List) for x in keyword_root]
    tf.append(term_frequency)
    term_counts.append(counts)

idf=[]
for word in keyword_root:
    appear=0
    for file in os.listdir('cricket'):
        if file == '.ipynb_checkpoints':
            continue
        if word.lower() in pre_process(file):
            appear += 1
    idf.append(math.log(float(len(document['filename']))/appear,10))

tf_idf=[]
for term in tf:
    tfidf=[]
    for amount in range(len(idf)):
        tfidf.append(term[amount]*idf[amount])
    tf_idf.append(tfidf)

key_word_tf=[]
for term in keyword_root:
    key_word_tf.append(1/len(keyword_root))
key_word_tfidf=[]
i=0
for term in key_word_tf:
    key_word_tfidf.append(idf[i]*term)
    i += 1
mag_tf_idf=[]
for h in tf_idf:
    square=[u**2 for u in h]
    mag_tf_idf.append(math.sqrt(sum(h)))
mag_key_word_tfidf=math.sqrt(sum(x**2 for x in key_word_tfidf))
dot_product=[]
for num in tf_idf:
    dot = 0
    for ind in range(len(num)):
        dot += num[ind]*key_word_tfidf[ind]
    dot_product.append(dot)
sims=[]
for numb in range(len(dot_product)):
    sims.append(round(dot_product[numb]/(mag_tf_idf[numb]*mag_key_word_tfidf),4))
stem_word_document['score']=sims
print(stem_word_document.sort_values(by='score',ascending=False))