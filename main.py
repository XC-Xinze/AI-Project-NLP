from datasets import load_dataset
import torch
import pandas as pd
ds = load_dataset("prithivMLmods/ChatGPT-Humane-Text-Prompts")
print(ds)
d_h_chtp = pd.DataFrame(ds)
output_file = "~/Project/huggingface_dataset.csv"
d_h_chtp.to_csv(output_file, index=False)