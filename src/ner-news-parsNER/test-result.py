from flair.data import Sentence
from flair.models import SequenceTagger
from flair.data import Corpus
from flair.datasets import ColumnCorpus

# define columns
columns = {0: 'text', 1: 'ner'}
data_folder = "./data/ner-news-parsNER/"
res_text = "./result/ner-news-parsNER/res1.txt"
corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file='train',
                              test_file='test')
# load the model you trained
model = SequenceTagger.load(data_folder + 'model1/final-model.pt')

# create example sentence
sentence = Sentence(' من  نیویورک رو دوست دارم')

# predict tags and print
model.predict(sentence)

print(sentence.to_tagged_string())

result = model.evaluate(corpus.test, gold_label_type = "ner", mini_batch_size=4, out_path=f"predictions.txt")
print(result)
with open(res_text, "w") as file1:
    file1.write(str(result))