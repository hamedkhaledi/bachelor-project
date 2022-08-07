from typing import List, Dict

from flair.data import Sentence
from flair.models import SequenceTagger
from model.request_models import InputElement
from model.response_models import EntityResponseModel, ResponseModel


def sentence_to_json(sentence: Sentence, tag: str = 'ner') -> List[EntityResponseModel]:
    result = []
    values = sentence.to_dict(tag)['entities']
    for value in values:
        entity_response = EntityResponseModel(
            entity_group=value['labels'][0].value,
            word=value['text'],
            start=int(value['start_pos']),
            end=int(value['end_pos']),
            score=float(value['labels'][0].score))
        result.append(entity_response)
    return result


class Responses:
    responses: Dict[int, ResponseModel] = {}

    @staticmethod
    def check_id(request_id: int) -> bool:
        if Responses.responses.get(request_id):
            return True
        return False

    @staticmethod
    def get_response(request_id: int) -> ResponseModel:
        if Responses.responses.get(request_id):
            return Responses.responses[request_id]


class NerResponse:
    def __init__(self):
        data_folder = "./data/"
        # load the model you trained
        self.model = SequenceTagger.load(data_folder + 'model-ner/final-model.pt')

    def predict_json(self, input_json: List[InputElement], request_id: int) -> ResponseModel:
        Responses.responses[request_id] = ResponseModel(progression="started")
        sentences = []
        for element in input_json:
            text = element.text
            lang = element.lang
            sentences.append(Sentence(text))
        Responses.responses[request_id] = ResponseModel(progression="in going")
        self.model.predict(sentences, mini_batch_size=4, verbose=True, embedding_storage_mode="gpu")
        result = []
        Responses.responses[request_id] = ResponseModel(progression="extracting")
        for sentence in sentences:
            result.append(sentence_to_json(sentence))
        Responses.responses[request_id] = ResponseModel(progression="done", result=result)
        print(request_id, " done ")
        return ResponseModel(progression="done", result=result)

    def predict(self, text):
        # create example sentence

        sentence: Sentence = Sentence(text)
        result = ""
        # predict tags and print
        self.model.predict(sentence)
        return sentence_to_json(sentence, 'ner')


class PosResponse:
    def __init__(self):
        data_folder = "./data/"
        # load the model you trained
        self.model = SequenceTagger.load(data_folder + 'model-pos/final-model.pt')

    def predict_json(self, input_json: List[InputElement], request_id: int) -> ResponseModel:
        Responses.responses[request_id] = ResponseModel(progression="started")
        sentences = []
        for element in input_json:
            text = element.text
            lang = element.lang
            sentences.append(Sentence(text))
        Responses.responses[request_id] = ResponseModel(progression="in going")
        self.model.predict(sentences, mini_batch_size=4, verbose=True, embedding_storage_mode="gpu")
        result = []
        Responses.responses[request_id] = ResponseModel(progression="extracting")
        for sentence in sentences:
            result.append(sentence_to_json(sentence, tag='pos'))
        Responses.responses[request_id] = ResponseModel(progression="done", result=result)
        print(request_id, " done ")
        return ResponseModel(progression="done", result=result)

    def predict(self, text):
        # create example sentence

        sentence: Sentence = Sentence(text)
        result = ""
        # predict tags and print
        self.model.predict(sentence)
        return sentence_to_json(sentence, 'pos')
