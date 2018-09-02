#%%
import pandas as pd
import numpy as np

file = pd.read_excel('/Users/t-matsuzawa/budget_viz/national_budget/data/DL201811001.xls', sheet_name = '一般会計 予定経費要求書（科目別内訳）')
file = file.iloc[:,[0,1,9,10,11]]
file.columns = ["jurisdiction", "organization", "item", "subject", "amount"]
file[["jurisdiction", "organization", "item"]] = file[["jurisdiction", "organization", "item"]].fillna(method="ffill")
file = file.dropna()
file[["amount"]] = file[["amount"]].astype('float64')
print(file.head())

#file.to_csv('/Users/t-matsuzawa/budget_viz/national_budget/data/budget2018.csv', index=False)
file.to_json('/Users/t-matsuzawa/budget_viz/national_budget/data/budget2018.json', orient='records')