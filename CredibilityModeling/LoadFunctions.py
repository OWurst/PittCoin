"""
This file contains the functions that are used to load the data from the files.
Data comes from multiple sources, and putting all of this together requires building
multiple dataframes in different ways and concatenating them together. This file is
used to load the data from the files and return the dataframes. 
"""
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

def clean_df(df):
    df = df.dropna()

    # put quotes around the text and titles to avoid errors when saving
    df['text'] = df['text'].apply(lambda x: '"' + x + '"')
    df['title'] = df['title'].apply(lambda x: '"' + x + '"')

    # convert all text and titles to lowercase strings
    # df['text'] = df['text'].apply(lambda x: x.lower())
    # df['title'] = df['title'].apply(lambda x: x.lower())

    # remove all newline characters
    df['text'] = df['text'].apply(lambda x: x.replace('\n', ' '))
    df['title'] = df['title'].apply(lambda x: x.replace('\n', ' '))

    return df


def csv_to_dict(filename):
    """
    Reads a csv file and returns a dictionary with the data.
    """
    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        mydict = {int(rows[0]):int(rows[1]) for rows in reader}
    return mydict

def flip_labels(df):
    """
    Flips the labels of the dataframe (for some datasets, 
    1 means fake and 0 means real, we want 1 to mean trustworthy).
    """
    df['label'] = 1 - df['label']
    return df

def clean_unicode(text):
    text_utf8 = text.replace('\u2018', "'").replace('\u2019', "'")
    text_utf8 = text_utf8.replace('\u203a', '>').replace('\u2039', '<')
    text_utf8 = text_utf8.replace('\u201c', "'").replace('\u201d', "'")
    text_utf8 = text_utf8.replace('\u2014', '-').replace('\u2015', '-')

    # replace newlines, new paragraphs, and tabs with spaces
    text_utf8 = text_utf8.replace('\u2028', ' ').replace('\u2029', ' ')
    text_utf8 = text_utf8.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

    # replace weird 00a0 character with space
    text_utf8 = text_utf8.replace('\u00a0', ' ')

    # replace weird 00b7 character with period
    text_utf8 = text_utf8.replace('\u00b7', '.')

    # replace weird 00e2 character with space
    text_utf8 = text_utf8.replace('\u00e2', ' ')

    # replace weird 00e2 character with space
    text_utf8 = text_utf8.replace('\u00e2', ' ')

    text_utf8 = text_utf8.replace('\u2013', '-')

    # remove oe character
    text_utf8 = text_utf8.replace('\u0153', 'oe')

    # make euro symbol into the word 'euro'
    text_utf8 = text_utf8.replace('\u20ac', 'euro')

    # make pound symbol into the word 'pound'
    text_utf8 = text_utf8.replace('\u00a3', 'pound')

    # make yen symbol into the word 'yen'
    text_utf8 = text_utf8.replace('\u00a5', 'yen')

    # make unicode space into a regular space
    text_utf8 = text_utf8.replace('\u2002', ' ').replace('\u2003', ' ')
    text_utf8 = text_utf8.replace('\u2004', ' ').replace('\u2005', ' ')
    text_utf8 = text_utf8.replace('\u2006', ' ').replace('\u2007', ' ')
    text_utf8 = text_utf8.replace('\u2008', ' ').replace('\u2009', ' ')
    text_utf8 = text_utf8.replace('\u200a', ' ').replace('\u200b', ' ')
    text_utf8 = text_utf8.replace('\u200c', ' ').replace('\u200d', ' ')
    text_utf8 = text_utf8.replace('\u200e', ' ').replace('\u200f', ' ')

    # make tm symbol into the word 'trademark'
    text_utf8 = text_utf8.replace('\u2122', 'trademark')

    # make copyright symbol into the word 'copyright'
    text_utf8 = text_utf8.replace('\u00a9', 'copyright')

    # make registered symbol into the word 'registered'
    text_utf8 = text_utf8.replace('\u00ae', 'registered')

    # make bullet symbol into *
    text_utf8 = text_utf8.replace('\u2022', '*')

    # make ellipsis symbol into ...
    text_utf8 = text_utf8.replace('\u2026', '...')

    # make em dash symbol into --
    text_utf8 = text_utf8.replace('\u2014', '--')

    # convert to utf-8
    text_utf8 = text_utf8.encode('utf-8').decode('utf-8')

    return text_utf8

def fix_utf8(df):
    df['text'] = df['text'].apply(clean_unicode)
    df['title'] = df['title'].apply(clean_unicode)
    return df

def load_kamal007():
    """
    Data from this set is split into three csv files: train, submit, and test.
    * train.csv is a labeled dataframe
    * test.csv is an unlabeled dataframe
    * submit.csv is a mapping of indexes to labels for test.csv
    I will be creating a dataframe with title, text, and label columns with all of
    the data from train.csv and test.csv because I will be creating splits myself.
    """
    # set up train dataframe (load, flip labels, drop unused columns)
    train = load_csv('Data/Kaggle-kamal007fakenewsprediction/trainenglish.csv')
    train = train.drop(['id', 'author'], axis=1)
    train = flip_labels(train)

    train = clean_df(train)

    train = fix_utf8(train)

    return train

def load_sumanthvrao():
    """
    Data from this set is split into two folders, one for fake news and one for real news.
    Each folder contains multiple text files with the title on the first line and text of 
    the news article on the following lines. I will be creating a dataframe with title, 
    text, and label columns with all of the data from the text files.
    """
    # set up fake dataframe
    fake = []
    fake_dir = 'Data/Kaggle-sumanthvraofakenewsdataset/fake/'
    for filename in os.listdir(fake_dir):
        with open(fake_dir + filename, 'r') as file:
            title = file.readline().strip()
            text = file.read().strip()
            fake.append([title, text, 0])
    fake = pd.DataFrame(fake, columns=['title', 'text', 'label'])

    # set up real dataframe
    real = []
    real_dir = 'Data/Kaggle-sumanthvraofakenewsdataset/real/'
    for filename in os.listdir(real_dir):
        with open(real_dir + filename, 'r') as file:
            title = file.readline().strip()
            text = file.read().strip()
            real.append([title, text, 1])
    real = pd.DataFrame(real, columns=['title', 'text', 'label'])

    # concatenate fake and real dataframes
    full_data = pd.concat([fake, real], ignore_index=True)

    full_data = clean_df(full_data)

    return full_data

# main method is just for testing
if __name__ == '__main__':
    # load data
    data1 = load_kamal007()
    print(data1.head())

    data2 = load_sumanthvrao()
    print(data2.head())

    # save each as csv
    data1.to_csv('data1.csv', index=False)
    data2.to_csv('data2.csv', index=False)