#!/usr/bin/env python3
"""Module for retrieving school documents by topic from
a MongoDB collection."""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieves all school documents that have a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection object.
        topic (str): The topic to search for in the 'topics' field.

    Returns:
        pymongo.cursor.Cursor: A cursor to the documents that match the topic.
    """
    return mongo_collection.find({"topics": topic})
