from flair.visual.training_curves import Plotter
data_folder = "./data/ner-NSURL-Persian-NER-2019/"
plotter = Plotter()
plotter.plot_training_curves(data_folder + "model/loss.tsv")