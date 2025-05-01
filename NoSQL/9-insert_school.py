#!/usr/bin/env python3
"""Module for inserting a new document into a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection object.
        **kwargs: Arbitrary keyword arguments representing
        the fields and values for the new document.

    Returns:
        ObjectId: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(**kwargs)
    return result.inserted_id
