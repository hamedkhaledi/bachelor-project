from flair.data import Sentence
from flair.models import SequenceTagger
from flair.data import Corpus
from flair.datasets import ColumnCorpus
from pathlib import Path
import os
from flair.visual.training_curves import Plotter

# define columns
columns = {0: 'text', 1: 'ner'}
data_folder = "./data/ner-NSURL-Persian-NER-2019/"
res_text = "./result/ner-NSURL-Persian-NER-2019/res(13).txt"
corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file='train.txt',
                              test_file='test.txt',
                              dev_file='valid.txt')
print(corpus.get_label_distribution())
# load the model you trained
# print(Path(data_folder + 'model3/final-model.pt').exists())
# model = SequenceTagger.load(data_folder + 'model3/final-model.pt')
# # create example sentence
# sentence = Sentence(' من  نیویورک رو دوست دارم')

# # predict tags and print
# model.predict(sentence)

# print(sentence.to_tagged_string())

# result = model.evaluate(corpus.test, gold_label_type = "ner", mini_batch_size=4, out_path=f"predictions.txt")
# print(result)
# with open(res_text, "w") as file1:
#     file1.write(str(result))
    
# os.system('cp ./data/ner-NSURL-Persian-NER-2019/model3/training.log ./result/ner-NSURL-Persian-NER-2019/training13.log') 
# plotter = Plotter()
# plotter.plot_training_curves(data_folder + "model3/loss.tsv")