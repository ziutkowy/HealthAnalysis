import pandas as pd


df = pd.read_csv("original_data/mortality.csv")

columns_to_keep = {
    "Reference area" : "country",
    "SEX" : "sex_code",
    "Sex" : "sex_label",
    "TIME_PERIOD" : "year",
    "OBS_VALUE": "deaths_per_100k"
}

df_clean = df[list(columns_to_keep.keys())].rename(columns=columns_to_keep)

df_clean.sort_values(by=["country", "year"])
df_clean.drop_duplicates()

df_clean["year"]= df_clean["year"].astype(int)
df_clean["deaths_per_100k"]=df_clean["deaths_per_100k"].astype(float)
print(df_clean.head(5))
# df_clean.to_csv("clear_mortality.csv")