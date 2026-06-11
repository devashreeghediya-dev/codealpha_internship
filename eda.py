import pandas as pd

data = {
    "Name": ["John", "Emma", "Alex", "Sophia", "David"],
    "Age": [25, 28, 30, 26, 35],
    "Salary": [30000, 35000, 40000, 37000, 50000]
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())