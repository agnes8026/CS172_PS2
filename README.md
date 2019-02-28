# CS172_PS2


I wrote a stemming program but for some reason I couldn't apply it to my (so-called) search engine, so I used elasticsearch to build the engine, do the document indexing and process the query.
stemming.py is what I have wrote, just to prove my bad work.


To run the engine, first run docIndex.py to do the document indexing and upload to my elasticsearch node.
queryProcess.py and tfidf.py are the programs that prep and run the queries in the query.txt. All queries are executed using TF-IDF, and the top 100 results s written to an output file. 


queryProcess will run queries against elasticsearch. Instead of using their built in query engine, the program will be retrieving information such as TF and DF scores from elasticsearch and implementing our own document ranking. tf-idf.py uses TF and DF scores from your elasticsearch index, as needed.
