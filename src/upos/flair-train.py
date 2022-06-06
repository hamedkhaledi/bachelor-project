import flair.datasets
from flair.embeddings import WordEmbeddings, FlairEmbeddings, StackedEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer

corpus = flair.datasets.UD_PERSIAN()

data_folder = "./data/upos/"


# 2. what label do we want to predict?
label_type = 'upos'

# 3. make the label dictionary from the corpus
label_dict = corpus.make_label_dictionary(label_type=label_type)
print(label_dict)


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
                        use_crf=False)

# 6. initialize trainer
trainer = ModelTrainer(tagger, corpus)

trainer.train(data_folder + 'model2',
              mini_batch_size=16,
            #   mini_batch_chunk_size = 1,
              max_epochs=100,
              write_weights = True,
              embeddings_storage_mode='gpu',
              checkpoint=True,)