import pandas as pd
import os
import shutil
import chardet
import tqdm

"""
    This file creates csv files for each year in the philippe remy dataset.
    The files are saved in the newdata/philippe_data/directory. The files initially
    are text files and will need to be preprocessed accordingly. Cleaning will
    not be done in this file.
"""

initial_path = './bloomberg_2010-2013'

def limit_years():
    directories = os.listdir('./bloomberg_2010-2013')
    
    for directory in directories:
        # if the first four characters are less than 2010, delete the directory
        if int(directory[:4]) < 2010:
            shutil.rmtree(f'./bloomberg_2010-2013/{directory}')

def make_year_file(year):
    # list all directories that start with the year
    directories = os.listdir(initial_path)
    year_directories = [directory for directory in directories if directory.startswith(year)]

    year_df_list = []

    print("Reading files for year: ", year)

    # use tqdm to show progress bar
    for directory in tqdm.tqdm(year_directories):
        # list all files in the directory
        files = os.listdir(f'{initial_path}/{directory}')
        for file in files:
            rawdata = open(f'{initial_path}/{directory}/{file}', 'rb').read()
            result = chardet.detect(rawdata)
            char_enc = result['encoding']

            # read the file
            with open(f'{initial_path}/{directory}/{file}', 'r', encoding=char_enc) as f:
                # title is on line 1
                title = f.readline().strip()
                title = title[3:]

                # date is on line 3
                f.readline()
                date = f.readline().strip()
                date = date[3:]

                # date starts as full timestamp, we only want date
                date = date.split('T')[0]

                #skip over url
                f.readline()

                # read the rest of the file
                content = f.read()

                # make a dataframe with the title, date, and content
                temp_df = pd.DataFrame({'title': [title], 'date': [date], 'content': [content]})
                year_df_list.append(temp_df)

    # concatenate all the dataframes
    print("Building dataframe for year: ", year)
    year_df = pd.concat(year_df_list, ignore_index=True)
    year_df.to_csv(f'./bloomberg{year}.csv', index=False)
    print(year_df.head())

if __name__ == '__main__':
    limit_years()

    make_year_file('2010')
    make_year_file('2011')
    make_year_file('2012')
    make_year_file('2013')