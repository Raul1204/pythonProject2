import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.io
import seaborn as sns
import plotly.express as px
from matplotlib import pyplot as plt, colors
import statsmodels.formula.api as smf

df = pd.read_csv('spain2.csv')
df["fecha"]= df["fecha"].str.replace("/", "-")
df.reset_index(inplace=True)

print("\nThe lenght of the data is:", len(df))
# to show the dimensions of the pandas dataset
print("\nThe shape of the data:", df.shape)

#df = df["fallecimientos"].dropna()

print("Replace missing values with '0':\n     Now there are:",df.isnull().sum().sum(),"missing values")

# to show the first 6 lines of the pandas dataset
print("\nThe first 6 observations are:\n",df.head(6))


print("\nObservations with more than 300 fatalities")
select3=df.loc[df['fallecimientos'] >= 300.0]
print(select3)

df5 = pd.read_csv('spain2.csv')
validloop = False
while validloop is not True:
    d = int(input("select a day (In number from 1 to 31): "))
    if d>0 and d<32:
        validloop = True
        d=str(d)
        if len(d)<2:
            d = str("0"+d)
    else:
        print("Make sure to enter a valid day (In number from 1 to 31)")


validloop = False
while validloop is not True:
    m = int(input("Select a month (In number from 1 to 12): "))
    if m>0 and m<13:
        validloop = True
        m=str(m)
        if len(m)<2:
            m = str("0"+m)
    else:
        print("Make sure to enter a valid month (In number from 1 to 12)")

validloop = False
while validloop is not True:
    y = int(input("select a year: "))
    if y>=2020 and y<=2022:
        validloop = True
        y = str(y)
    else:
        print("Make sure to enter a value between 2020 and 2022")

x = str(d+"-"+m+"-"+y)

select4 = df.loc[df['fecha']== x]
print("The data for the selected date is:\n",select4)
for i in df.columns:
    print(select4[i])

#First plot on fatalities vs cases
plt.plot(df["casos_total"], df["fallecimientos"], 'r-', linewidth=0.1)
plt.plot(df["casos_total"], df["fallecimientos"], 'o', ms=3)
plt.xlabel("total cases")
plt.ylabel("Fatalities")
plt.title("Total Cases VS Fatalities")
plt.legend(loc="upper left")
plt.show()


plt.plot(df["fecha"], df["total_test"], label = "Total Test")
plt.plot(df["fecha"], df["casos_total"], label="Total Cases")
plt.ylabel("Total Test")
plt.xlabel("Total Cases")
plt.title("Total Test VS Total Cases")
plt.legend(loc="upper left")
plt.show()


plt.plot(df["fecha"], df["hospitalizados"], label = "Hospitaliced")
plt.plot(df["fecha"], df["ingresos_uci"], label="ICUs")
plt.xlabel("Date")
plt.ylabel("Number of people")
plt.title("Amount of Hospitalized Patients")
plt.legend(loc="upper left")
plt.show()

df3 = pd.read_csv('dataworld.csv')
df2 = df3.sort_values(by=["Confirmed_2020", "Countries"]).tail(10)
plt.bar(df2["Countries"], df2["Confirmed_2021"], label="2021")
plt.bar(df2["Countries"], df2["Confirmed_2022"], label = "2022")
plt.bar(df2["Countries"], df2["Confirmed_2020"], label="2020")
plt.xlabel("Country")
plt.ylabel("Confirmed cases")
plt.title("Cases by country")
plt.legend(loc="upper left")
plt.show()

df4 = pd.read_csv('nacional_covid19.csv')
results = smf.ols('casos_total ~ fallecimientos', data=df4).fit()
print(results.summary())

mlrformula = 'fallecimientos ~ casos_total + altas  + ingresos_uci + hospitalizados'
mlrmodel = smf.ols(mlrformula, data=df4)
mlrresults = mlrmodel.fit()
print(f'{mlrresults.rsquared=}')
print(mlrresults.summary())