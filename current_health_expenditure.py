import pandas as pd

df = pd.read_csv("original_data/current_health_expenditure.csv", skiprows=4)

df.dropna(axis = 1, how ='all', inplace=True)

df_clean = df.melt(id_vars=['Country Name', 'Country Code']
                   , var_name='Year', value_name='Expenditure (US$ billion)')

df_clean['Year'] =pd.to_numeric(df_clean['Year'], errors= 'coerce')

df_clean.reset_index(drop=True, inplace=True)
df_clean.sort_values(by=['Country Name', 'Year'])
df_clean = df_clean[df_clean['Year'] >= 2000]
print(df.head(5))

# df_clean.to_csv("clear_current_health_expenditure.csv")