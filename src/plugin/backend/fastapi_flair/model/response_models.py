from typing import List, Optional

from pydantic import BaseModel


class EntityResponseModel(BaseModel):
    entity_group: str
    word: str
    start: int
    end: int
    score: float


class BaseResponse(BaseModel):
    id: int
    status: str


class ResponseModel(BaseModel):
    progression: str
    result: Optional[List[List[EntityResponseModel]]]
