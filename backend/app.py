import pandas as pd
import json

path = '../files/input/messy_test_file.xlsx'

df = pd.read_excel(path, sheet_name=None)

csv_string = df['Sheet1'].to_csv(index=False, header=True)

print(csv_string.re)

