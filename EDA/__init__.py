class EDA:
    def __init__(self, dataset_2017_filename, dataset_2018_filename):
        self.dataset_2017_filename = dataset_2017_filename
        self.dataset_2018_filename = dataset_2018_filename

        import pandas as pd
        # First load the dataset into pandas dataframe
        self.dataset_2017 = pd.read_csv(dataset_2017_filename, delimiter=',')
        self.dataset_2018 = pd.read_csv(dataset_2018_filename, delimiter=',')

    from .eda_def import generateTargetVars
    from .getCorrelation import getCorrelation
