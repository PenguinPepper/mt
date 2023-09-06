#!/usr/bin/python3
"""Initialize the models package"""

from models.storageunit.filestorage import Filestorage

storage = Filestorage()
storage.reloads()
