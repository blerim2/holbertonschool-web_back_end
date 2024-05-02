#!/usr/bin/env python3
'''
NoSQL
'''


def update_topics(mongo_collection, name, topics):
    '''
    function that changes all topics of a school document based on the name
    '''
    myquery = {"name": name}
    newvalues = {"$set": { "topics": topics}}
    mongo_collection.update_many(myquery, newvalues)