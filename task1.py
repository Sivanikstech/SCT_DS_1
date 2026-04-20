import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", skiprows=4, encoding='latin1', engine='python')



data = df[(df['Indicator Name'] == 'Population, total') & (df['Country Code'].str.len() == 3)]
data = data[['Country Name', '2022']].dropna()


top10 = data.sort_values(by='2022', ascending=False).head(10)


plt.figure()
plt.bar(top10['Country Name'], top10['2022'])

plt.title("Top 10 Countries by Population (2022)")
plt.xlabel("Country")
plt.ylabel("Population")

plt.xticks(rotation=45)

plt.savefig("output.png")
plt.show()