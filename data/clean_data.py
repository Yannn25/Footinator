import pandas as pd
import datetime


# Read the data into a pandas DataFrame
df = pd.read_csv('players.csv')

# Select only the desired columns
df = df.loc[:, ['name', 'current_club_name', 'country_of_citizenship', 'country_of_birth', 'date_of_birth', 'position', 'sub_position', 'foot', 'height_in_cm', 'market_value_in_eur','current_club_domestic_competition_id']]
# Write the new DataFrame to a CSV file
df.to_csv('cleaned_search_result.csv', index=False)

#There we only keep the Big European Championship 
df2 = pd.read_csv('cleaned_search_result.csv')
today = datetime.date.today()
df2['date_of_birth'] = pd.to_datetime(df2['date_of_birth'])  # Convertir la colonne en format de date
df2['age'] = df2['date_of_birth'].apply(lambda x: today.year - x.year)
df2 = df2.drop('date_of_birth', axis=1)
# Define a list of Big league club IDs
Big_league_club_ids = ['FR1','L1','ES1','IT1','GB1']

# Filter the DataFrame to only show players who belong to a club in the Big leagues and who have a value over 20 millions
df2 = df2[df2['current_club_domestic_competition_id'].isin(Big_league_club_ids) ]
df2 = df2[df2['market_value_in_eur'] > 60000000]
df2.to_csv('final_players.csv', index=False)


