#!/usr/bin/env python3
"""This module provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def get_logs_stats(mongo_collection, option=None):
    """
    This function gets statistics about Nginx logs stored in MongoDB.
    """
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print("\tmethod {}: {}".format(option, value))
        return

    result = mongo_collection.count_documents(items)
    print("{} logs".format(result))
    print("Methods:")
    for method in METHODS:
        get_logs_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print("{} status check".format(status_check))


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    get_logs_stats(nginx_collection)