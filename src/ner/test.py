from flair.data import Corpus
from flair.datasets import ColumnCorpus

columns = {0: 'text', 1: 'ner'}
data_folder = "./data/ner/"
corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file='train.txt',
                              test_file='valid.txt',
                              dev_file='valid.txt')

# 2. what label do we want to predict?
label_type = 'ner'

# 3. make the label dictionary from the corpus
label_dict = corpus.make_label_dictionary(label_type=label_type)
label_dict.add_unk = True
label_dict.remove_item('در')
print(label_dict)
print(label_dict.add_unk)