import pandas as pd
import matplotlib.pyplot as plt

from data import games

# Select all plays
plays = games[games['type'] == 'play']

# Select all strike outs
strike_outs = plays[plays['event'].str.contains('K')]

# Group by Year and Game
strike_outs = strike_outs.groupby(['year', 'game_id']).size()

# Reset Index
strike_outs = strike_outs.reset_index(name='strike_outs')

# Apply an Operation to Multiple Columns
strike_outs = strike_outs.loc[:, ['year', 'strike_outs']].apply(pd.to_numeric)

# Plot df
strike_outs.plot(x='year', y='strike_outs', kind='scatter').legend(['Strike Outs'])
plt.show()

