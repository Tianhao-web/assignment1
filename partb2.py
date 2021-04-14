# Part B Task 2
import re
import os
import sys
filename = sys.argv[1]
def pre_process(filename):
    with open('cricket/'+filename, "r") as a_file:
        text = a_file.read()
        text = re.sub(r'\d|\W',r' ',text)
        text = re.sub(r' +', r' ', text)
        text = text.lower()
        print(text)
    return text