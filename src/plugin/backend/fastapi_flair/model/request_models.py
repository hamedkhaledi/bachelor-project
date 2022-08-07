from typing import List

from pydantic import BaseModel


class InputElement(BaseModel):
    lang: str
    text: str


InputType = List[InputElement]


class RequestModel(BaseModel):
    id: int
    request: InputType
