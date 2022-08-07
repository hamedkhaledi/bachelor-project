from flair.data import Sentence
from flair.models import SequenceTagger
from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.visual.training_curves import Plotter
import os
# define columns
columns = {0: 'text', 1: 'ner'}
data_folder = "./data/ner-NSURL-Persian-NER-2019/"
data_folder2 = "./data/ner-Persian-NER/"
res_text = "./result/ner-Persian-NER/res-nsurl.txt"
corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file='train.txt',
                              test_file='test.txt',
                              dev_file='valid.txt')
# load the model you trained
model = SequenceTagger.load(data_folder2 + 'model-resume/final-model.pt')

# create example sentence
sentence = Sentence(' من  نیویورک رو دوست دارم')

# predict tags and print
model.predict(sentence)

print(sentence.to_tagged_string())

result = model.evaluate(corpus.test, gold_label_type = "ner", mini_batch_size=4, out_path=f"predictions.txt")
print(result)
with open(res_text, "w") as file1:
    file1.write(str(result))
    
# os.system('cp ./data/ner-Persian-NER/model-resume/training.log ./result/ner-Persian-NER/training1.log') 
# plotter = Plotter()
# plotter.plot_training_curves(data_folder + "model/loss.tsv")