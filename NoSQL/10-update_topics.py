#!/usr/bin/env python3
"""Module for updating the topics of a school document
in a MongoDB collection."""


def update_topics(mongol_collection, name, topics):
    """
    Updates the topics of a school document based on the school's name.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection object.
        name (str): The name of the school to update.
        topics (list): The list of topics to set for the school.

    Returns:
        pymongo.results.UpdateResult: The result of the update operation.
    """
    mongol_collection.update_many({"name": name}, {"$set": {"topics": topics}})
