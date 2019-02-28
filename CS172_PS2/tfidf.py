from __future__ import division
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import math
from operator import itemgetter
import string
import dill

es = Elasticsearch()


s = Search().using(es).query("match_all")
s.aggs.bucket("avg_size", "avg", field="doc_len")
s.aggs.bucket("vocabSize", "cardinality", field="text")
res = s.execute()
D = 84678
avgDocLen = 20969809/84660 #res.aggregations.avg_size.value
V = res.aggregations.vocabSize.value
print(V)

def TF_IDF(qNo, termVector, docFreq):
    docScore = []
    for docid in termVector:
        tf = 0
        for key in termVector[docid]:
            tfwd = termVector[docid][key][0]
            docLen = termVector[docid][key][1]
            tf += ((tfwd / (tfwd + 0.5 + (1.5 * (docLen / avgDocLen)))) * (math.log10(D/list(filter(lambda x:x[0]==key, docFreq))[0][1])))
        docScore.append([docid, tf])
    docScore.sort(key=itemgetter(1), reverse=True)
    with open('/Users/50175/Desktop/CS172_PS2/data/Results_File.txt', 'a+') as queryResults:
        rank = 1
        for ds in docScore:
            queryResults.write('%s Q0 %s %d %lf Exp\n' % (qNo, ds[0], rank, ds[1]))
            # if rank == 1000:
            #     break
            rank += 1

def queryNums():
    f = open('query_list.txt', 'r')
    queries = []
    for line in f:
        queries.append(line.split()[0].translate(None, string.punctuation))
    return queries

qNums = queryNums()
i = 0
f = open('Pickles/totalTF.p', 'rb')
cTF = dill.load(f)
f.close()
for qNo in qNums:
    i += 1
    # if i == 1:
    f = open('Pickles/docFreq%s.p' % i, 'rb')
    docFreq = dill.load(f)
    f.close()
    f = open('Pickles/termVector%s.p' % i, 'rb')
    termVector = dill.load(f)
    f.close()
    TF_IDF(qNo, termVector, docFreq)
print("Done!")