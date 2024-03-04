import pandas as pd

df = pd.read_csv('data/weather_data_v2.csv')

# split date and time
df['Date'] = [datetime.split()[0] for datetime in df['Date/Time']]
df['Time'] = [datetime.split()[1] for datetime in df['Date/Time']]
df = df.drop('Date/Time', axis=1)

# move 'Date' and 'Time' to front
move = ['Date', 'Time']
order = move + [col for col in df if col not in move]
df = df[order]

# check results and export
print(df.head())
df.to_csv('result.csv', index=False)
