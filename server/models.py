from pydantic import BaseModel
from pydantic_mongo import AbstractRepository, PydanticObjectId
from typing import Optional
from time import time
import string
from random import choice

class UrlLookup(BaseModel):
    id: Optional[PydanticObjectId] = None
    timestamp: float = time()
    salt: str = ''.join( choice(string.ascii_letters+string.digits)  for _ in range(10)) 
    url: str

class URLRepository(AbstractRepository[UrlLookup]):
   class Meta:
      collection_name = 'urls'

