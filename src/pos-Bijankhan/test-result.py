from flair.data import Sentence
from flair.models import SequenceTagger
from flair.data import Corpus
from flair.datasets import ColumnCorpus
from pathlib import Path
import os
from flair.visual.training_curves import Plotter

# define columns
columns = {0: 'text', 1: 'pos'}
data_folder = "./data/pos-Bijankhan/"
res_text = "./result/pos-Bijankhan/res2.txt"
corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file='train.txt',
                              test_file='test.txt',
                              dev_file='valid.txt')


# 2. what label do we want to predict?
label_type = 'pos'

# 3. make the label dictionary from the corpus
label_dict = corpus.make_label_dictionary(label_type=label_type)

# load the model you trained
print(Path(data_folder + 'model2/final-model.pt').exists())
model = SequenceTagger.load(data_folder + 'model2/final-model.pt')
# create example sentence
sentence = Sentence(' من  نیویورک رو دوست دارم')

# predict tags and print
model.predict(sentence)

print(sentence.to_tagged_string())

result = model.evaluate(corpus.test, gold_label_type = "pos", mini_batch_size=4, out_path=f"predictions.txt")
print(result)
with open(res_text, "w") as file1:
    file1.write(str(result))
    
os.system('cp ./data/pos-Bijankhan/model2/training.log ./result/pos-Bijankhan/training1.log') 
plotter = Plotter()
plotter.plot_training_curves(data_folder + "model2/loss.tsv")