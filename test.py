## This is for test different parameters for testing model ##
import pandas as pd
import datasets
file_path1='./clear_wiki_dataset.csv'
#By observing the dataset, wiki_dataser has some human's name. I am tring to clean these contents...
wiki_dataset=pd.read_csv(file_path1)

print(wiki_dataset.info)