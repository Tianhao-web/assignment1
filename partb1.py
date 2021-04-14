## Part B Task 1

import re
import pandas as pd
import os
import sys

name = sys.argv[1]
column_names = ['filename','documentID']
document = pd.DataFrame(columns = column_names)
filenames=[]
documentID=[]
path=os.getcwd()
for filename in os.listdir('cricket'):
    if filename.endswith(".txt"):        
        filenames.append(filename)
        with open('cricket/'+filename, "r") as a_file:
            match = re.search(r'[A-Z]{4}\-[0-9]{3}[A-Z]?', a_file.read())
            if match:
                documentID.append(match.group())                
    else:
        continue   
document['filename']=filenames
document['documentID']=documentID
document=document.sort_values(by='filename',ascending=True)
document.to_csv(name,index=False)