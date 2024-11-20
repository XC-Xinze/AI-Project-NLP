from datasets import load_dataset
import torch
import pandas as pd
ds1 = load_dataset("prithivMLmods/ChatGPT-Humane-Text-Prompts")
#for testing if dataset has been split
print(ds1)
ds2 = load_dataset("080-ai/20k_wikipedia_title_prompts")
print(ds2)
ds3 = load_dataset("fka/awesome-chatgpt-prompts")
print(ds3)

d_h_chtp = pd.DataFrame(ds1)
output_file1 = "~/Project/Data/gpt_dataset.csv"
d_h_chtp.to_csv(output_file1, index=False)

d_h_wiki = pd.DataFrame(ds2)
output_file2 = "~/Project/Data/wiki_dataset.csv"
d_h_wiki.to_csv(output_file2, index=False)

d_h_awesome = pd.DataFrame(ds3)
output_file3 = "~/Project/Data/awesome_dataset.csv"
d_h_awesome.to_csv(output_file3, index=False)
