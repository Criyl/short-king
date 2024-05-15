from pymongo import MongoClient
from server.models import URLRepository
import os

client = MongoClient(os.environ['MONGO_URI'])
database = client[os.environ['MONGO_DATABASE']]

url_repository = URLRepository(database=database)