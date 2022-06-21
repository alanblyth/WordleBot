# %%
import pandas as pd

def has_unique_letters(word):
    char_list = list(word)
    unique_char_set = set(char_list)
    if len(unique_char_set) == 5:
        return True
    else:
        return False
all_words = pd.read_csv('words.txt', sep=" ", header=None).rename(columns={0: 'word'})

all_words['unique_chars'] = all_words['word'].apply(has_unique_letters)
# %%
