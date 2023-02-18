import pandas as pd
data = pd.read_csv("D:/project127/venv/PRO-129-Datasets-main")
data.head()
data = data.dropna()
data.head()