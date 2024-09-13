#!/usr/bin/env python3
"""
12-log_stats.py
"""

from pymongo import MongoClient


def log_stats():
    """ provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    total = logs.count_documents({})
    get = logs.count_documents({"method": "GET"})
    post = logs.count_documents({"method": "POST"})
    put = logs.count_documents({"method": "PUT"})
    patch = logs.count_documents({"method": "PATCH"})
    delete = logs.count_documents({"method": "DELETE"})
    path = logs.count_documents({"method": "GET", "path": "/status"})

    print(f"{total} logs")
    print("Methods:")

    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")


if __name__ == "__main__":
    log_stats()
