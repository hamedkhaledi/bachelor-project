from typing import Dict

from model.request_models import InputType


class Requests:
    def __init__(self):
        self.requests: Dict[int, InputType] = {}
        self.id = 0

    def add_request(self, input_json: InputType):
        self.requests[self.id] = input_json
        self.id += 1
        return self.id

