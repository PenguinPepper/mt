#!/usr/bin/python3
"""Initialize the models package"""

from os import getenv
from dotenv import load_dotenv


load_dotenv()
storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.storageunit.dbstorage import DBstorage
    storage = DBstorage()
else:
    from models.storageunit.filestorage import Filestorage
    storage = Filestorage()
storage.reload()
