import pandas as pd
import cleaning_functions as cf

def get_meruvulikith_data():
    new_data = pd.read_csv('./newdata/meruvulikith_newdata/data-1.csv')
    
    new_data["text"] = new_data["scraped_content"]
    new_data["title"] = new_data["Title"]
    new_data["date"] = new_data["Date"]
    new_data = new_data[["text", "title", "date"]]

    new_data = cf.clean(new_data)
    print("meruvulikith data preprocessed")
    return new_data

def get_old_data():
    old_data1 = pd.read_csv('./newdata/original_data/news_and_stocks_with_domain.csv')

    old_data1['date'] = old_data1['published']
    old_data1 = old_data1[['text', 'title', 'date']]

    old_data1 = cf.clean(old_data1)
    print("Large Old Dataset Preprocessed")

    old_data2 = pd.read_csv('./newdata/original_data/news_and_stocks_small.csv')

    old_data2['date'] = old_data2['Date']
    old_data2 = old_data2[['text', 'title', 'date']]

    old_data2 = cf.clean(old_data2)
    print("Small Old Dataset Preprocessed")

    old_data = pd.concat([old_data1, old_data2], ignore_index=True)

    return old_data

def get_amulyas_data():
    new_data = pd.read_csv('./newdata/amulyas_newdata/amulyas.csv')
    
    new_data["date"] = new_data["published"].apply(lambda x: x.split("T")[0])
    new_data = new_data[["text", "title", "date"]]

    new_data = cf.clean(new_data)
    print("amulyas data preprocessed")
    return new_data

if __name__ == '__main__':
    # keep this and comment out old datasets when adding new datasets
    try:
        curr_dataset = pd.read_csv('new_train_data.csv')
    except:
        pass
    
    meruvulikith = get_meruvulikith_data()
    original_data = get_old_data()
    amulyas = get_amulyas_data()
    new_datasets = [
        meruvulikith, 
        original_data,
        amulyas
        ]

    try:
        new_datasets.append(curr_dataset)
        curr_dataset = pd.concat(new_datasets, ignore_index=True)
    except:
        curr_dataset = pd.concat(new_datasets, ignore_index=True)
    
    # remove duplicates in text
    curr_dataset = curr_dataset.drop_duplicates(subset='text')
    curr_dataset = curr_dataset.dropna()

    curr_dataset.to_csv('new_train_data.csv')
    print("\nSaved to 'new_train_data.csv'")