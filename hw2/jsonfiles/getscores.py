import linecache;
from elasticsearch import Elasticsearch;
import json
def ranking(qid1, qid1_title, ratings):
    _search = {
        "requests": [
            {
                "id": str(qid1),
                "request":{
                    "query":{
                        "bool": {
                            "must_not":{
                                "match":{
                                    "_id":qid1
                                }
                            },
                            "should": [
                            {
                                "match": {
                                    "title": {
                                        "query": qid1_title,
                                        "boost": 3.0,
                                        "analyzer": "my_analyzer"
                                    }
                                    }
                                },
                                {
                                    "match": {
                                    "body": {
                                        "query": qid1_title,
                                        "boost": 0.5,
                                        "analyzer": "my_analyzer"
                                }}},
                                {
                                    "match": {
                                    "body": {
                                        "query": qid1_title,
                                        "boost": 0.5,
                                        "analyzer": "my_analyzer"
                                }}}
                                ]}}
                },
                "ratings":ratings
                }
        ],
        "metric":{
            "dcg":{
                "k":10,
                "normalize":True
            }
        }
    }
    return _search

es=Elasticsearch()
if es.indices.exists(index="java_lm") == False:
    print("WHERE IS THE INDEX")
else:
    print("!")
    ndcg_list=[]
    String1=""
    lang="java"
    filen = open("../../%s_cosidf.txt"%lang,"r")
    filem = open("./%s_lm_ratings.JSON"%lang,"w")
    num=2
    qid1s=[]
    
    ratings=[]
    #try:
    String1=filen.readline()
    for i in range(1000):
        linecache.clearcache()
        String1 = linecache.getline("../../%s_cosidf.txt"%lang,num+i*30)
        qid1s.append(String1.split('\t')[0])

        ratings=[]
        for j in range(30):
            String1=filen.readline()
            #print(String1)
            ratings.append({"_index":"java_lm"  ,"_id":String1.split('\t')[1],"rating":int(String1[len(String1)-2])})
            filem.write(json.dumps(ratings[j]))
            filem.write("\n")
        #Save ratings as a JSON

        qid1_title=es.get(index="java_lm", doc_type='_doc',id=qid1s[i])['_source']['title']
        #Load_ratings_for(qid1[i]) # Computed by Algorithm 2
        _search = ranking(qid1s[i], qid1_title, ratings) # Figure 2
        ndcg_list.append(es.rank_eval(index="java_lm",body=_search)['metric_score'])
    # except e:
    #     print(e)
    #     filem.close()
    #     filen.close()
    # finally:
    m=0.0
    for n in ndcg_list:
        m+=float(n)
    print(m/len(ndcg_list))
    filem.close()
    filen.close()
    # Compute and return the NDCG@10 score from ndcg list