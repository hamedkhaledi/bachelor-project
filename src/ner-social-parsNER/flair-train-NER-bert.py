from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import WordEmbeddings, FlairEmbeddings, StackedEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
from flair.data import Sentence
from flair.models import SequenceTagger
from flair.embeddings import TransformerWordEmbeddings
from torch.optim.lr_scheduler import OneCycleLR
from flair.visual.training_curves import Plotter
import os
import torch
import gc
torch.cuda.empty_cache()
gc.collect()

# define columns
columns = {0: 'text', 2: 'ner'}
data_folder = "./data/ner-social-parsNER/"
corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file='train.txt',
                              test_file='test.txt',
                              dev_file='valid.txt')

# 2. what label do we want to predict?
label_type = 'ner'

# 3. make the label dictionary from the corpus
label_dict = corpus.make_label_dictionary(label_type=label_type)
label_dict.add_unk = True
print(label_dict)
print(label_dict.add_unk)



# 4. initialize fine-tuneable transformer embeddings WITH document context
embeddings = TransformerWordEmbeddings(model='HooshvareLab/bert-base-parsbert-uncased',
                                       layers="-1",
                                       subtoken_pooling="first",
                                       fine_tune=True,
                                       use_context=True,
                                       local_files_only=True
                                       )

# 5. initialize bare-bones sequence tagger (no CRF, no RNN, no reprojection)
tagger = SequenceTagger(hidden_size=512,
                        embeddings=embeddings,
                        tag_dictionary=label_dict,
                        tag_type='ner',
                        use_crf=False,
                        use_rnn=False,
                        reproject_embeddings=False,
                        )

# 6. initialize trainer
trainer = ModelTrainer(tagger, corpus)

# 7. run fine-tuning
trainer.fine_tune(data_folder + 'model',
                  learning_rate=5.0e-6,
                  mini_batch_size=4,
                  mini_batch_chunk_size=1,  # remove this parameter to speed up computation if you have a big GPU7
                  embeddings_storage_mode='cpu',
                  max_epochs=100,
                  )

os.system('cp ./data/ner-social-parsNER/model/training.log ./result/ner-social-parsNER/training2.log') 
plotter = Plotter()
plotter.plot_training_curves(data_folder + "model/loss.tsv")