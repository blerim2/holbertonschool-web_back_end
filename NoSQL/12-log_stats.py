#!/usr/bin/env python3
'''
NoSQL
'''
from pymongo import MongoClient


method = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def nginx_logs_stats(mongo_collection):
    """
    script that provides some stats about Nginx logs stored in MongoDB
    """
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    for x in method:
        method_count = mongo_collection.count_documents({"method": x})
        print(f"\tmethod {x.upper()}: {method_count}")
    status_check = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    nginx_logs_stats(nginx_collection)