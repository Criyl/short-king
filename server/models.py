from pydantic import BaseModel
from pydantic_mongo import AbstractRepository, PydanticObjectId
from typing import Optional
from time import time

class UrlLookup(BaseModel):
    id: Optional[PydanticObjectId] = None
    timestamp: float = time()
    url: str

class URLRepository(AbstractRepository[UrlLookup]):
   class Meta:
      collection_name = 'urls'

