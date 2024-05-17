from pydantic import BaseModel
from pydantic_mongo import AbstractRepository, PydanticObjectId
from server.mongo import database
from typing import Optional
from time import time
import string
from random import choice

class UrlLookup(BaseModel):
    id: Optional[PydanticObjectId] = None
    timestamp: float = time()
    salt: str
    url: str

class URLRepository(AbstractRepository[UrlLookup]):
   class Meta:
      collection_name = 'urls'

url_repository = URLRepository(database=database)

def generate_salt(size: int) -> str:
    generated = ''.join( choice(string.ascii_letters+string.digits)  for _ in range(size))
    if url_repository.find_one_by({"salt": generated}):
        return generate_salt(size)
    return generated

def generate_url(url: str) -> UrlLookup:
        url_item = UrlLookup(url=url, salt=generate_salt(5))
        url_repository.save(url_item)
        return url_item