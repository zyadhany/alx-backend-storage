#!/usr/bin/env python3
"""
10-update_topics.py
"""

from pymongo import MongoClient


def update_topics(mongo_collection: MongoClient, name, topics):
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
