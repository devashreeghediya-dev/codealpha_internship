import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_data.csv")

plt.figure(figsize=(8,5))

plt.bar(df["Name"], df["Salary"])

plt.title("Employee Salary Comparison")
plt.xlabel("Employee")
plt.ylabel("Salary")

plt.tight_layout()

plt.savefig("sales_chart.png")

plt.show()