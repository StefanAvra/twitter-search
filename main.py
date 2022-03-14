import os
import pandas as pd

since = '2006-01-01'
query = '"ich habe keine zeit"'
until = '2021-03-14'
max_results = 0

filename = "".join(
    [c for c in f'tweets-{query}-{since}-{until}' if c.isalnum() or c in ['-', '.']]).rstrip()
cmd_line = f'snscrape {"--max-results" + max_results if max_results else ""} --jsonl --progress --since {since} twitter-search \'{query} until:{until}\'> {filename}.json'
print(cmd_line)
os.system(cmd_line)

# tweets_df = pd.read_json(
#     f'{filename}.json', lines=True)[['content', 'date', 'user']]

# print(tweets_df.head())

# tweets_df.to_csv(f'{filename}.csv', sep=',', index=False)


# user.username
# user.displayname
# user.verified
# content
# date
#
