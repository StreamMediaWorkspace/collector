# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch

class es(object):
    es = Elasticsearch()
    es.indices.create(index='news', ignore=400)
    data = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'}
    result = es.create(index='news', doc_type='politics', id=1, body=data)
    print(result)
