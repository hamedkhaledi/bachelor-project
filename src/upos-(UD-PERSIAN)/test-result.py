import flair
from flair.data import Sentence
from flair.models import SequenceTagger
from flair.data import Corpus
from flair.datasets import ColumnCorpus

# define columns
columns = {0: 'text', 1: 'upos'}
data_folder = "./data/upos-(UD-PERSIAN)/"
res_text = "./result/upos-(UD-PERSIAN)/res(3).txt"
corpus = flair.datasets.UD_PERSIAN()
# load the model you trained
model = SequenceTagger.load(data_folder + 'model2/final-model.pt')

# create example sentence
sentence = Sentence(' من  نیویورک رو دوست دارم')

# predict tags and print
model.predict(sentence)

print(sentence.to_tagged_string())

result = model.evaluate(corpus.test, gold_label_type = "upos", mini_batch_size=4, out_path=f"predictions.txt")
print(result)
with open(res_text, "w") as file1:
    file1.write(str(result))