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

import LoadFunctions as LF

def load_csv(filename):
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
    
    data_obj = DO.DataObject(savefilename=savefilename, train=train, dev=dev, test=test)

    return data_obj

def build_full_dataset():
    """
        This function loads multiple datasets and concatenates them into one full dataset.
    """

    data1 = LF.load_kamal007()
    data2 = LF.load_sumanthvrao()

    full_data = pd.concat([data1, data2], ignore_index=True)

    # put quotes around the text and titles to avoid errors when saving
    full_data['text'] = full_data['text'].apply(lambda x: '"' + x + '"')
    full_data['title'] = full_data['title'].apply(lambda x: '"' + x + '"')

    # convert all text and titles to lowercase strings
    full_data['text'] = full_data['text'].apply(lambda x: x.lower())
    full_data['title'] = full_data['title'].apply(lambda x: x.lower())

    # convert all text and titles to utf-8
    #full_data['text'] = full_data['text'].apply(lambda x: x.encode('utf-8'))
    #full_data['title'] = full_data['title'].apply(lambda x: x.encode('utf-8'))

    return full_data

if __name__ == '__main__':
    # set seed: sampling is random and I want reproducible results
    random.seed(0)

    # load data
    full_data = build_full_dataset()
    do = split_data(full_data, savefilename='full_data')

    do.save()

    print(do.stats())