import pandas as pd
import cleaning_functions as cf

def get_meruvulikith_data():
    data = pd.read_csv('./meruvulikith_newdata/data-1.csv')
    return data

if __name__ == '__main__':
    new_data = get_meruvulikith_data()

    curr_dataset = pd.read_csv('new_train_data.csv')
    
    new_data["text"] = new_data["scraped_content"]
    new_data["title"] = new_data["Title"]
    new_data["date"] = new_data["Date"]

    new_data = new_data[["text", "title", "date"]]

    new_data = cf.clean(new_data)

    curr_dataset = pd.concat([curr_dataset, new_data], ignore_index=True)

    curr_dataset.to_csv('new_train_data.csv')