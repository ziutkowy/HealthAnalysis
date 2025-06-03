import pandas as pd


df = pd.read_csv("original_data/life_expectancy.csv")


column_to_keep = {
    "Reference area": "country",
    "TIME_PERIOD": "year",
    "SEX" : "sex_code",
    "Sex":"sex_label",
    "OBS_VALUE": "life_expectancy"
}

df_clean = df[list(column_to_keep.keys())].rename(columns=column_to_keep)
df_clean.drop_duplicates()
df_clean['year']=df_clean['year'].astype(int)
df_clean['life_expectancy']=df_clean['life_expectancy'].astype(float)
print(df_clean.head(5))
#
# df_clean.to_csv("clear_life_expectancy.csv")