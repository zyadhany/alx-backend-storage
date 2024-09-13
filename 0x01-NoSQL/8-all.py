#!/usr/bin/env python3
""" 8-all """


def list_all(mongo_collection):
    """ list all documents in Python"""
    return mongo_collection.find()
