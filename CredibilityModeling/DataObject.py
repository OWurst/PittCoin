"""
    Simple data object for storing train/dev/test filenames all together as separate attributes.
    This is used to pass data between functions in the data manipulation process as well as
    to save the data split so that all models use the same split. This is the object returned
    by functions in DataManipulation.py.
"""
import pandas as pd
import csv

class DataObject:
    def __init__(self, savefilename=None, trainfile=None, devfile=None, testfile=None, train=None, dev=None, test=None):
        self.savefilename = savefilename
        
        self.train = train
        self.dev = dev
        self.test = test

        self.trainfile = trainfile
        if self.trainfile is not None:
            self.load_train()

        self.devfile = devfile
        if self.devfile is not None:
            self.load_dev()
        
        self.testfile = testfile
        if self.testfile is not None:
            self.load_test()

    def load_train(self):
        try:
            self.train = pd.read_csv(self.trainfile)
            print('Train data loaded from ' + self.trainfile)
        except:
            print('Error loading train data from ' + self.trainfile)
            quit()
    
    def load_dev(self):
        try:
            self.dev = pd.read_csv(self.devfile)
            print('Dev data loaded from ' + self.devfile)
        except:
            print('Error loading dev data from ' + self.devfile)
            quit()
    
    def load_test(self):
        try:
            self.test = pd.read_csv(self.testfile)
            print('Test data loaded from ' + self.testfile)
        except:
            print('Error loading test data from ' + self.testfile)
            quit()

    def get_train(self):
        return self.train
    
    def get_dev(self):
        return self.dev
    
    def get_test(self):
        return self.test

    def save(self):
        self.trainfile = self.savefilename + '_train.csv'
        self.devfile = self.savefilename + '_dev.csv'
        self.testfile = self.savefilename + '_test.csv'

        self.train.to_csv(self.trainfile, index=False)
        self.dev.to_csv(self.devfile, index=False)
        self.test.to_csv(self.testfile, index=False)

    def stats(self):
        # filenames
        print('Train file: ' + str(self.trainfile))
        print('Dev file: ' + str(self.devfile))
        print('Test file: ' + str(self.testfile))
        
        # sizes
        if self.train is not None:
            print('Train size: ' + str(len(self.train)))
        
        if self.dev is not None:
            print('Dev size: ' + str(len(self.dev)))
        
        if self.test is not None:
            print('Test size: ' + str(len(self.test)))
        
        # split member information
        if self.train is not None:
            print('Train info:')
            print(self.train.info())
        
        if self.dev is not None:
            print('Dev info:')
            print(self.dev.info())

        if self.test is not None:
            print('Test info:')
            print(self.test.info())