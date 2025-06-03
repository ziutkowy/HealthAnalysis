import pandas as pd


df = pd.read_csv("original_data/Pm_25.csv", skiprows=4)
df.dropna(axis = 1, how ='all', inplace=True)

df_clean = df.melt(id_vars=['Country Name', 'Country Code'],
                   var_name='Year', value_name='PM2.5_micrograms_per_cubic_meter')
df_clean['Year'] =pd.to_numeric(df_clean['Year'], errors= 'coerce')


df_clean.reset_index(drop=True, inplace=True)
df_clean = df_clean[df_clean['Year'] >= 2000]

df_clean['Year'] = df_clean['Year'].astype(int)
df_clean['PM2.5_micrograms_per_cubic_meter'] = df_clean['PM2.5_micrograms_per_cubic_meter'].astype(float)

print(df.head())


# df_clean.to_csv("clear_pm_25.csv")