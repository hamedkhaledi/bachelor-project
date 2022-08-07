from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import WordEmbeddings, FlairEmbeddings, StackedEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
from flair.data import Sentence
from flair.models import SequenceTagger
from flair.visual.training_curves import Plotter

import torch
import gc
torch.cuda.empty_cache()
gc.collect()

# define columns
columns = {0: 'text', 1: 'ner'}
data_folder = "./data/ner-NSURL-Persian-NER-2019/"
corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file='train.txt',
                              test_file='test.txt',
                              dev_file='valid.txt')

# 2. what label do we want to predict?
label_type = 'ner'

# 3. make the label dictionary from the corpus
label_dict = corpus.make_label_dictionary(label_type=label_type)
label_dict.add_unk = True
label_dict.remove_item('در')
print(label_dict)
print(label_dict.add_unk)


# 4. initialize embedding stack with Flair and GloVe
embedding_types = [
    WordEmbeddings('fa'),
    FlairEmbeddings('fa-forward'),
    FlairEmbeddings('fa-backward')
]
embeddings = StackedEmbeddings(embeddings=embedding_types)

# 5. initialize sequence tagger
tagger = SequenceTagger(hidden_size=1024,
                        embeddings=embeddings,
                        tag_dictionary=label_dict,
                        tag_type=label_type,
                        use_crf=True)

# 6. initialize trainer
trainer = ModelTrainer(tagger, corpus)

torch.cuda.empty_cache()
gc.collect()


# 7. start training
trainer.train(data_folder + 'model2',
              mini_batch_size=4,
            #   mini_batch_chunk_size = 1,
              max_epochs=100,
              write_weights = True,
              embeddings_storage_mode='none',
              checkpoint=True,)


