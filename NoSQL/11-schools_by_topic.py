#!/usr/bin/env python3
'''
NoSQL
'''


def schools_by_topic(mongo_collection, topic):
    '''
    function that returns the list of school having a specific topic
    '''
    value = {"topics": topic}
    return mongo_collection.find(value)