from pymongo import MongoClient
import os

client = MongoClient(os.environ['MONGO_URI'], tls=False, tlsAllowInvalidCertificates=True)
database = client[os.environ['MONGO_DATABASE']]