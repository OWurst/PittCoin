"""
One model for credibility modeling is to use BERT. This script is used to fine tune BERT for the credibility modeling task.
"""

import DataManipulation as DM
import pandas as pd

if __name__ == '__main__':
    data_obj = DM.load_train_dev('full_data')

    train = data_obj.get_train()
    dev = data_obj.get_dev()