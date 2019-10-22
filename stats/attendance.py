import pandas as pd
import matplotlib.pyplot as plt

from data import games

# Select attendance
attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'), ['year', 'multi3']]

# Rename attendance columns
attendance.columns = ['year', 'attendance']

# Convert to numeric
attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])

# Plot dataframe
attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')
plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y=dataframe['column'].mean(), label='Mean', linestyle = '--', color='green')

plt.show()




