import pandas as pd
df = pd.read_csv('original_data/cancer.csv')



columns_to_keep = {
    "Reference area" : "country",
    "TIME_PERIOD" : "year",
    "SEX" : "sex_code",
    "Sex" : "sex_label",
    "CANCER_SITE" : "cancer_code",
    "Cancer site": "cancer_site",
    "OBS_VALUE": "cases_per_100k"
}

df_clean = df[list(columns_to_keep.keys())].rename(columns=columns_to_keep)

df_clean.drop_duplicates()
df_clean.sort_values(by=["country", "year"])

df_clean["year"]= df_clean["year"].astype(int)
df_clean["cases_per_100k"]=df_clean["cases_per_100k"].astype(float)


print(df_clean.head(5))

# df_clean.to_csv("clear_cancer.csv")