#!/usr/bin/env python3
''' Python Module to list all documents in a colection
'''

def list_all(mongo_collection):
    '''Lists all documents in a collection.
    '''
    return [doc for doc in mongo_collection.find()]
