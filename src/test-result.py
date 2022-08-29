from flair.data import Sentence
from flair.models import SequenceTagger
from flair.data import Corpus
from flair.datasets import ColumnCorpus
from pathlib import Path
import os
from flair.visual.training_curves import Plotter

# define columns
columns = {0: 'text', 1: 'ner'}
data_folder1 = "./data/ner-NSURL-Persian-NER-2019/model2/final-model.pt"
data_folder2 = "./data/pos-Bijankhan/model2/final-model.pt"
data_folder3 = "./data/upos-UD-PERSIAN/model2/final-model.pt"
exm = "مریم میرزاخانی ریاضیدان شد."
# load the model you trained
model1 = SequenceTagger.load(data_folder1)
model2 = SequenceTagger.load(data_folder2)
model3 = SequenceTagger.load(data_folder3)
# create example sentence
sentence = Sentence(exm)

# predict tags and print
model1.predict(sentence)
print(sentence.to_tagged_string())

model2.predict(sentence)
print(sentence.to_tagged_string())

model3.predict(sentence)
print(sentence.to_tagged_string())