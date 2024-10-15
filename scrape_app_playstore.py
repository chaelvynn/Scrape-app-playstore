# -*- coding: utf-8 -*-
"""scrape app playstore.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DNtWj87UhIhMgdGJgdqBfb0nhP0KKCzW
"""

!pip install google-play-scraper

from google_play_scraper import app

import pandas as pd

import numpy as np

from google_play_scraper import app

result = app(
    'com.dbs.id.pt.digitalbank',
    lang='id',
    country='id'
)

# Akses jumlah unduhan
jumlah_unduhan = result['installs']
print(jumlah_unduhan)

from google_play_scraper import Sort, reviews_all

result = reviews_all(
    'com.dbs.id.pt.digitalbank',
    sleep_milliseconds=0,
    lang='id',
    country='id',
    sort=Sort.NEWEST
)

df_busu = pd.DataFrame(np.array(result),columns=['review'])

df_busu = df_busu.join(pd.DataFrame(df_busu.pop('review').tolist()))

df_busu.head()

len(df_busu.index)

df_busu[['userName', 'score','at', 'content']].head()

new_df = df_busu[['userName', 'score','at', 'content']]
sorted_df = new_df.sort_values(by=['score', 'at'], ascending=[False, False])
sorted_df.head()

my_df = sorted_df[['userName', 'score','at', 'content']]

my_df.head()

my_df.to_csv("scrapped_data.csv", index = False)

import pandas as pd
import matplotlib.pyplot as plt

download_count = '1,000,000+ Downloads'

score_counts = df_busu['score'].value_counts().sort_index()

# Create a bar chart for score distribution
plt.figure(figsize=(10, 6))
plt.bar(score_counts.index, score_counts.values, color='skyblue')
plt.xlabel('Score')
plt.ylabel('Number of Reviews')
plt.title('Distribution of Reviews by Rating')

# Annotate with the number of downloads
plt.text(1, max(score_counts.values) * 0.95, download_count, fontsize=12, color='black', ha='left')

plt.xticks(score_counts.index)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()