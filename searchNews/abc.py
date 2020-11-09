from elasticsearch import Elasticsearch
import os
import requests
import json
from prediction import predict_sentiment
from elasticsearch.helpers import scan

key = os.environ.get('API_KEY')
ip = os.environ.get('IP')

es = Elasticsearch(['http://'+ip])
print(es)

query = {'size': 1000, 'query': {'match_all' : {}}}
data = es.search(index='news-articles', body=query)

if data['hits']['hits'] == []:
    print('Elasticsearch is empty')

l = []
l2 = []

print(data['hits']['hits'][0])

for article in data['hits']['hits']:
    # print(article['_id'])
    # print(article['_source']['publishedAt'])
    if 'sentiment' in article['_source']:
    	l2.append(article['_source']['publishedAt'])
    else:
        print('not there', article['_source']['publishedAt'])
    l.append(article['_source']['publishedAt'])

# print(sorted(l))
# print(sorted(l2))
print(len(l), len(l2))

# query = {"query": {"range": {"publishedAt": {"from": '2020-10-19', "to": '2020-10-19'}}}}   
# data = es.search(index="news-articles", track_total_hits=10000, size=10000, body=query)
# print(len([d["_source"] for d in data['hits']['hits']]))  
# predict_sentiment(data, es)





# data = scan(es, index="news-articles", scroll ='5m', preserve_order=True, size=1000, timeout=None, clear_scroll=True, scroll_kwargs=None, query=query)
# print(len([d["_source"] for d in data]))
# for d in data:
#     print(d)
#     break

# kk = [d["_source"] for d in data]
# print(kk[1])
# 



# sid = data['_scroll_id']
# print(sid)

# scroll_size = data['hits']['total']['value']

# # Start scrolling

# while scroll_size > 0:

#     print ("Scrolling...")

#     page = es.scroll(scroll_id = sid, scroll = '2m')

# # Update the scroll ID

#     sid = page['_scroll_id']

#     # Get the number of results that we returned in the last scroll

#     scroll_size = len(page['hits']['hits'])

#     print ("scroll size: " + str(scroll_size))











