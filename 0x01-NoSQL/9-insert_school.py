#!/usr/bin/env python3
""" 8-all """

from pymongo import MongoClient


def insert_school(mongo_collection: MongoClient, **kwargs):
    """ insert a document in Python"""
    obj = mongo_collection.insert_one(kwargs)
    return obj.inserted_id
