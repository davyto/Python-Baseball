## Import data

import os as os
import glob as glob
import pandas as pd

# File management
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))

# Sort file names
game_files.sort() # sorts in place. sorted(list) would create a new list

# create a loop to import data
game_frames = [] # create empty list
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)

# concatenate dataframes
games = pd.concat(game_frames)

# replace values
games.loc[games['multi5'] =='??', 'multi5'] = ''

# extract feature and clean columns
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
identifiers = identifiers.fillna(method='ffill')
identifiers.columns = ['game_id', 'year'] # rename columns
games = pd.concat([games, identifiers], axis=1, sort=False)

# Fill NaN values
games = games.fillna(' ')

# Reduce memory usage by assigning data type to pandas
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

# print dataframe
games.head()




