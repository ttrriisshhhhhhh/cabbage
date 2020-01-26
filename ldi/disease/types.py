import pandas


class Disease:
    """ Holds available list of diseases for classification in 
        cabbage leaves
    """

    def __init__(self):
        import os
        __types__ = "ldi/disease/class_disease_list.csv"
        self.classes = self.read_data(__types__)

    def read_data(self, file):
        return pandas.read_csv(file)

    def __add__(self, name):
        raise NotImplementedError
        self.classes.append(name)

    def __remove__(self, name):
        raise NotImplementedError
        self.classes.remove(name)

    def __list__(self):
        return self.classes
