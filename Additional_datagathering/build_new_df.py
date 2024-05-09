import pandas as pd
import cleaning_functions as cf

def get_meruvulikith_data():
    new_data = pd.read_csv('./newdata/meruvulikith_newdata/data-1.csv')
    
    new_data["text"] = new_data["scraped_content"]
    new_data["title"] = new_data["Title"]
    new_data["date"] = new_data["Date"]

    new_data = new_data[["text", "title", "date"]]

    new_data = cf.clean(new_data)
    return new_data

if __name__ == '__main__':
    try:
        curr_dataset = pd.read_csv('new_train_data.csv')
    except:
        curr_dataset = pd.DataFrame(columns=["date", "title", "text"])
    
    meruvulikith = get_meruvulikith_data()
    new_datasets = [meruvulikith]

    for dataset in new_datasets:
        new_dataset = pd.concat([curr_dataset, dataset], ignore_index=True)

    new_dataset.to_csv('new_train_data.csv')
    