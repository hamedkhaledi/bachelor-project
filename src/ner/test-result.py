from flair.data import Sentence
from flair.models import SequenceTagger
data_folder = "./data/ner/"
# load the model you trained
model = SequenceTagger.load(data_folder + 'model2/final-model.pt')

# create example sentence
sentence = Sentence(' من  نیویورک رو دوست دارم')

# predict tags and print
model.predict(sentence)

print(sentence.to_tagged_string())

Code cell <WdFkUWE2ljNo>
#%% [code]
result = model.evaluate(corpus.test, gold_label_type = "ner", mini_batch_size=4, out_path=f"predictions.txt")
print(result)