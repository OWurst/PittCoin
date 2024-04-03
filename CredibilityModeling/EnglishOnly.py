import pandas as pd
import os
import csv
from langdetect import detect

def load_csv(filename):
    try:
        data = pd.read_csv(filename)
        print('Data loaded from ' + filename)
        return data
    except:
        print('Error loading data from ' + filename)
        quit()

def isEnglish(string):
    try:
        if detect(string) == 'en':
            return True
        else:
            return False
    except:
        return False

def filter_english(df):
    print('Filtering out non-english articles...')
    print('Original size:', len(df))

    df = df[df['text'].apply(isEnglish)]
    df = df[df['title'].apply(isEnglish)]

    print('New size:', len(df))
    return df

if __name__ == '__main__':
    train = load_csv('Data/Kaggle-kamal007fakenewsprediction/train.csv')
    train = filter_english(train)
    print(train.head())

    # save english model to csv
    train.to_csv('Data/Kaggle-kamal007fakenewsprediction/trainenglish.csv', index=False)


