""""
    This file contains functions for data manipulation and preprocessing that will be 
    used in the credibility modeling process by all 3 credibility models. This includes
    functions for loading the data, preprocessing the data, and splitting the data into
    training/dev/test as well as saving the split so that the split used by all models
    will be consistent. It used DataObject.py to store and transfer data.
"""
import pandas as pd
import DataObject as DO
import random

def load_data(filename):
    try:
        data = pd.read_csv(filename)
        print('Data loaded from ' + filename)
        return data
    except:
        print('Error loading data from ' + filename)
        quit()

def split_data(data, savefilename=None, train_size=0.8, dev_size=0.1, test_size=0.1):
    if train_size + dev_size + test_size != 1.0:
        print('Error: Train, dev, test sizes do not add up to 1.0')
        quit()
    
    train = data.sample(frac=train_size)
    data = data.drop(train.index)
    
    dev = data.sample(frac=dev_size/(1-train_size))
    data = data.drop(dev.index)
    test = data
    
    data_obj = DO(savefilename=savefilename, train=train, dev=dev, test=test)

    return data_obj


if __name__ == '__main__':
    # set seed: sampling is random and I want reproducible results
    random.seed(0)