import time
from typing import List

from flair.data import Sentence
from flair.models import SequenceTagger

from fastapi_flair.model.request_models import InputElement
from fastapi_flair.model.response_models import EntityResponseModel


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


columns = {0: 'text', 1: 'ner'}
data_folder = "../data/"
# load the model you trained
model = SequenceTagger.load(data_folder + 'model-ner/final-model.pt')

input_elem1 = InputElement(
    lang="fa",
    text="آخرین مقام برجسته ژاپنی که پس از انقلاب 57 تاکنون به ایران سفر کرده است شینتارو آبه است.")
input_json: List[InputElement] = []
sentences = []
for i in range(100):
    input_json.append(input_elem1)
start_time = time.time()

for element in input_json:
    text = element.text
    sentences.append(Sentence(text))
print("--- %s seconds ---" % (time.time() - start_time))
model.predict(sentences, mini_batch_size=32)
result = []

for sentence in sentences:
    result.append(sentence_to_json(sentence))
print("--- %s seconds ---" % (time.time() - start_time))
# 27 seconds for 100 elements
