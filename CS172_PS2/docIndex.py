import time
from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup
import os
import re

es = Elasticsearch()
path = "/Users/50175/Desktop/CS172_PS2/ap89_collection/"
start_time = time.time()
i = 0
for filename in os.listdir(path):
    if(filename != 'readme'):
        file = open(path+filename)
        page = file.read()
        #docNo = []
        validPage = "<root>" + page + "</root>"
        soup = BeautifulSoup(validPage, 'xml')
        docs = soup.find_all('DOC')
        for doc in docs:

            i+=1
            texts = doc.find_all('TEXT')
            text = ""
            for txt in texts:
                text += txt.get_text()
            count = 0
            for line in text.splitlines():
                word = re.sub('\s+', ' ', line).strip().split(' ')
                count += len(word)
            jsonDoc = {
                    'text': text
            }
            #docNo.append(doc.DOCNO.get_text().strip())
            res = es.index(index="index1", doc_type='document', id=doc.DOCNO.get_text().strip(), body=jsonDoc)
#            print("Indexed %d document" % i)