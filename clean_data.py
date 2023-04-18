import pandas as pd

# Read the data into a pandas DataFrame
df = pd.read_csv('players.csv')

# Select only the desired columns
df = df.loc[:, ['name', 'current_club_name', 'country_of_citizenship', 'country_of_birth', 'date_of_birth', 'position', 'sub_position', 'foot', 'height_in_cm', 'market_value_in_eur','current_club_domestic_competition_id']]
# Write the new DataFrame to a CSV file
df.to_csv('cleaned_search_result.csv', index=False)

#on garde uniquement les clubs des grands championnat 
df2 = pd.read_csv('cleaned_search_result.csv')

# Define a list of Big league club IDs
Big_league_club_ids = ['FR1','L1','ES1','IT1','GB1']

# Filter the DataFrame to only show players who belong to a club in the Big leagues et ont une valeur de plus de 20mil
df2 = df2[df2['current_club_domestic_competition_id'].isin(Big_league_club_ids) ]
df2 = df2[df2['market_value_in_eur'] > 20000000]
df2.to_csv('final_players.csv', index=False)

#transformer en JSON
