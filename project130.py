import pandas as pd
import csv
df = pd.read_csv("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")

print(df.shape)
del df("Luminosity")
df = df[["radius"].notna()]