import pandas as pd
import scrape_functions as sf

"""
    Much of the data we will need will need to be scraped from the web. This script drives the scraping process
    and calls the scraping functions to build the dataframes we need. The scraping functions take in a url and return
    the text of the article. The dataframes are then saved to the newdata folder. This
    script does not handle the preprocessing of the data, only the scraping, preprocesing will be 
    handled all at once in build_new_df.py which builds the final dataframe for training.
"""

def build_graban_df():
    graban_df = pd.read_csv('./newdata/stephgraban_newdata/wsj2014_2020_unscraped.csv')
    
    graban_df["title"] = graban_df["headlines"]

    # apply scrape to all urls
    graban_df["text"] = graban_df["url"].apply(sf.scrape_wsj)

    graban_df = graban_df[["text", "title", "date"]]
    graban_df = graban_df.dropna()
    print("Graban data scraped")

    # save the new data
    graban_df.to_csv('./newdata/stephgraban_newdata/wsj2014_2020_scraped.csv', index=False)
    print("Graban data saved to ./newdata/stephgraban_newdata/wsj2014_2020_scraped.csv")

if __name__ == '__main__':
    menu = {
        "1": build_graban_df,
    }

    print("Welcome to the data gathering script for the scraping dfs.")
    print("Pick the function you would like to run based on what df you would like to build.")
    while True:
        print("\n\nChoose a function to run:")
        for key, value in menu.items():
            print(f"{key}: {value.__name__}")
        print("q: quit")
        choice = input("Enter your choice: ")

        if choice == 'q':
            break

        if choice in menu:
            menu[choice]()
        else:
            print("Invalid choice. Try again.")