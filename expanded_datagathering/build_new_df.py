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

def get_old_data():
    old_data = pd.read_csv('./newdata/original_data/news_and_stocks.csv')

    old_data['date'] = old_data['Date']
    old_data = old_data[['text', 'title', 'date']]

    old_data = cf.clean(old_data)
    return old_data

if __name__ == '__main__':
    # keep this and comment out old datasets when adding new datasets
    try:
        curr_dataset = pd.read_csv('new_train_data.csv')
    except:
        curr_dataset = pd.DataFrame(columns=["date", "title", "text"])
    
    meruvulikith = get_meruvulikith_data()
    original_data = get_old_data()
    new_datasets = [meruvulikith, original_data]

    for dataset in new_datasets:
        curr_dataset = pd.concat([curr_dataset, dataset], ignore_index=True)
        
    print(curr_dataset.head())

    curr_dataset.to_csv('new_train_data.csv')