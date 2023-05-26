#!/usr/bin/env python3

from pymongo import MongoClient, errors

"""
related forum thread
======================
https://community.ui.com/questions/Is-there-a-way-to-set-the-default-time-zone-used-for-new-sites-in-the-controller/6ac47bb0-7143-41a4-8b8d-ed9b3f8ec06e

pymongo
=========
https://pymongo.readthedocs.io/en/stable/api/pymongo/mongo_client.html
https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find
https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find_one

"""

def create_mongo_client(host, port):
    client = MongoClient(host, port)
    try:
        client.admin.command('ping')
    except errors.ConnectionFailure:
        print("MongoDB server not available")
        return None
    return client

def get_sites(client):
    db = client['ace']
    sites = db['site']
    sites_cursor = sites.find({
        "desc": {'$ne': None},
        "name": {'$ne': "default"}
    }).sort("desc", 1)
    max_len = 0
    sites_data = []
    for site in sites_cursor:
        max_len = max(max_len, len(site["desc"]) + 2)
        sites_data.append(site)
    return sites_data, max_len

def print_sites(sites_data, max_len):
    db = client['ace']
    settings = db['setting']
    for site in sites_data:
        s = str(site["_id"])
        n = str(site["name"])
        desc = str(site["desc"])
        tz = settings.find_one({
            "site_id": s,
            "timezone": {'$ne': None}
        })
        if tz is not None:
            tz = tz.get('timezone')
        else:
            tz = '(none)'
        print('{:<10} {:<} {:<}'.format(n, desc.ljust(max_len), tz))

client = create_mongo_client('localhost', 27117)
if client:
    sites_data, max_len = get_sites(client)
    print_sites(sites_data, max_len)
