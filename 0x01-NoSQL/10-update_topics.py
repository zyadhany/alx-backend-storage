#!/usr/bin/env python3
"""
10-update_topics.py
"""

from pymongo import MongoClient


def update_topics(mongo_collection: MongoClient, name, topics):
    """ changes all topics of a school document based on the name """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
