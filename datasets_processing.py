
import pandas as pd
import spacy
import ast 
from tqdm.notebook import tqdm 

nlp = spacy.load("en_core_web_sm")
file_path1='../Data/wiki_dataset.csv'
#By observing the dataset, wiki_dataser has some human's name. I am tring to clean these contents...
wiki_dataset=pd.read_csv(file_path1)

print("Start...")
df_all = wiki_dataset.copy()

def is_person_name_prompt(text):
    doc = nlp(text)
    total_words = len([token for token in doc if not token.is_punct])
    
    person_count = sum(1 for ent in doc.ents if ent.label_ == 'PERSON')
    
    
    if total_words < 4 and person_count > 0:
        return True
        
    return person_count > 0

def extract_instruction(text):
    try:
        dict_data = ast.literal_eval(text)
        return dict_data.get('instructions', '')  
    except:
        print(f"Error: {text}") 
        return ''

print("In instructions...")
df_all['clean_text'] = df_all['train'].apply(extract_instruction)

#Filter
df_all['should_filter'] = df_all['clean_text'].apply(is_person_name_prompt)

print("\nSaving...")
df_clean = df_all[df_all['should_filter'] == False]
df_clean[['clean_text']].to_csv('clear_wiki_dataset.csv', index=False)
