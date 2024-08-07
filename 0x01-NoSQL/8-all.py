#!/usr/bin/env python3


def list_all(mongo_collection) -> list:
    """
    List all documents in a MongoDB collection.

    :param mongo_collection: The pymongo collection object.
    :return: A list of all document is in the
    collection or an empty list if the collection is empty.
    """

    documents: list = []

    for document in mongo_collection.find():
        documents.append(document)

    return documents
