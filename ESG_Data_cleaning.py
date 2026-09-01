from google.colab import files

uploaded = files.upload()
import pandas as pd
df=pd.read_excel("esg_cleaned.xlsx")
df.head()
import pandas as pd

excel_file = "esg_cleaned.xlsx"

pd.ExcelFile(excel_file).sheet_names
df = pd.read_excel(excel_file, sheet_name="esg_Cleaned.xlsx")
df.shape
df.head()
df.isnull().sum()
df['GrowthRate'] = df['GrowthRate'].fillna(df['GrowthRate'].mean())
df.isnull().sum()
df.shape
df.head()
df.info()
df.describe()
df['Industry'].value_counts()
df['Region'].value_counts()
df['Year'].min(), df['Year'].max()

1.Average ESG score by industry

df.groupby('Industry')['ESG_Overall'].mean().sort_values(ascending=False)

2.Total carbon emissions by industry

df.groupby('Industry')['CarbonEmissions'].sum().sort_values(ascending=False)

3. Total carbon emissions by year

df.groupby('Year')['CarbonEmissions'].sum().sort_values(ascending=False)

4. Average ESG score by region

df.groupby('Region')['ESG_Overall'].mean().sort_values(ascending=False)

ESG score vs Profit Margin

df[['ESG_Overall','ProfitMargin']].corr()

ESG score vs Revenue

df[['ESG_Overall','Revenue']].corr()

Carbon Emissions vs Revenue

df[['CarbonEmissions','Revenue']].corr()

Environmental score vs Carbon Emissions

df[['ESG_Environmental','CarbonEmissions']].corr()

ESG score by industry. This helps us identify which industries have the strongest and weakest average ESG performance

import matplotlib.pyplot as plt

industry_esg = df.groupby('Industry')['ESG_Overall'].mean().sort_values()

industry_esg.plot(kind='barh', figsize=(10,6))

plt.title('Average ESG Score by Industry')
plt.xlabel('Average ESG Score')
plt.ylabel('Industry')
plt.show()

Carbon emissions trend.

year_emissions = df.groupby('Year')['CarbonEmissions'].sum()

year_emissions.plot(kind='line', figsize=(10,6))

plt.title('Total Carbon Emissions by Year')
plt.xlabel('Year')
plt.ylabel('Total Carbon Emissions')
plt.show()

ESG vs Profit Margin

plt.figure(figsize=(10,6))

plt.scatter(df['ESG_Overall'], df['ProfitMargin'])

plt.title('ESG Score vs Profit Margin')
plt.xlabel('ESG Overall Score')
plt.ylabel('Profit Margin')
plt.show()

df.to_excel("ESG_Final_Cleaned.xlsx", index=False)
from google.colab import files
files.download("ESG_Final_Cleaned.xlsx")