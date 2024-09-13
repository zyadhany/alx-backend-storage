#!/usr/bin/env python3
"""
12-log_stats.py
"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """

    students = mongo_collection.find()
    students = [student for student in students]

    for student in students:
        summ = 0
        count = 0
        for topic in student['topics']:
            summ += topic['score']
            count += 1

        average = 0
        if count > 0:
            average = summ / count

        student['averageScore'] = average

    students = sorted(students, key=lambda x: x['averageScore'], reverse=True)
    return students
