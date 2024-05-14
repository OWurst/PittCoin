import pandas as pd
import os
import shutil

"""
    This file creates csv files for each year in the philippe remy dataset.
    The files are saved in the newdata/philippe_data/directory. The files initially
    are text files and will need to be preprocessed accordingly. Cleaning will
    not be done in this file.
"""

def limit_years():
    directories = os.listdir('./bloomberg_2010-2013')
    
    for directory in directories:
        # if the first four characters are less than 2010, delete the directory
        if int(directory[:4]) < 2010:
            shutil.rmtree(f'./bloomberg_2010-2013/{directory}')

if __name__ == '__main__':
    limit_years()