from __future__ import annotations

from typing import Union, Dict
import torch
from fastapi import FastAPI, HTTPException, Request
from starlette.status import HTTP_201_CREATED

from src.database_handler import Database
from src.requests import Requests
from model.request_models import InputType, InputElement
from model.response_models import BaseResponse, ResponseModel
from src.response import NerResponse, Responses, PosResponse
from fastapi import BackgroundTasks

print(torch.__version__)
app = FastAPI()
ner_response = NerResponse()
pos_response = PosResponse()
requests: Requests = Requests()
database: Database = Database()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ner/{item_id}", response_model=ResponseModel)
async def read_item(item_id, request: Request) -> ResponseModel:
    if database.check_client(client_id=request.headers.get('Client-Id'),
                             client_password=request.headers.get('Client-Password')):
        if not Responses.check_id(int(item_id)):
            raise HTTPException(status_code=404, detail="Item not found")
        return Responses.get_response(int(item_id))
    else:
        raise HTTPException(status_code=403, detail="you are not allowed")


@app.post("/ner", response_model=BaseResponse, status_code=HTTP_201_CREATED)
async def ner(input_json: InputType, background_tasks: BackgroundTasks, request: Request) -> BaseResponse:
    if database.check_client(client_id=request.headers.get('Client-Id'),
                             client_password=request.headers.get('Client-Password')):
        request_id = requests.add_request(input_json)
        background_tasks.add_task(ner_response.predict_json, input_json, request_id)
        return BaseResponse(status="input received successfully", id=request_id)
    else:
        raise HTTPException(status_code=403, detail="you are not allowed")
    # return ner_response.predict_json(input_json)


@app.post("/ner", response_model=BaseResponse, status_code=HTTP_201_CREATED)
async def ner(input_json: InputType, background_tasks: BackgroundTasks, request: Request) -> BaseResponse:
    if database.check_client(client_id=request.headers.get('Client-Id'),
                             client_password=request.headers.get('Client-Password')):
        request_id = requests.add_request(input_json)
        background_tasks.add_task(ner_response.predict_json, input_json, request_id)
        return BaseResponse(status="input received successfully", id=request_id)
    else:
        raise HTTPException(status_code=403, detail="you are not allowed")


@app.post("/nerTest", response_model=ResponseModel, status_code=HTTP_201_CREATED)
async def ner(input_json: InputType, request: Request) -> ResponseModel:
    if database.check_client(client_id=request.headers.get('Client-Id'),
                             client_password=request.headers.get('Client-Password')):
        print(input_json)
        result = ner_response.predict_json(input_json, 1)
        print(result)
        return result
    else:
        raise HTTPException(status_code=403, detail="you are not allowed")


@app.post("/posTest", response_model=ResponseModel, status_code=HTTP_201_CREATED)
async def pos(input_json: InputType, request: Request) -> ResponseModel:
    if database.check_client(client_id=request.headers.get('Client-Id'),
                             client_password=request.headers.get('Client-Password')):
        print(input_json)
        result = pos_response.predict_json(input_json, 1)
        print(result)
        return result
    else:
        raise HTTPException(status_code=403, detail="you are not allowed")
