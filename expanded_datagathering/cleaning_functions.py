import pandas as pd

def clean(data):
    data = data.dropna()
    return data