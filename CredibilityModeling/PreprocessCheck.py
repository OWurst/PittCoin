import pandas as pd
import os
import csv

def load_csv(filename):
    try:
        data = pd.read_csv(filename)
        print('Data loaded from ' + filename)
        return data
    except:
        print('Error loading data from ' + filename)
        quit()

if __name__ == '__main__':
    train = load_csv('full_data_train.csv')
    dev = load_csv('full_data_dev.csv')
    test = load_csv('full_data_test.csv')

    print(train.head())
    print(dev.head())
    print(test.head())