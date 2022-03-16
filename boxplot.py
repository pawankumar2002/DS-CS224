import plotly.express as px
import pandas as pd
df = pd.read_csv('./data/cleaned_data.csv')

parameters = ["poverty",
              "malnutrition",
              "literacy",
              "drinking water",
              "electricity",
              "unemployment"]


for i in range(1, 7):
    print(i, parameters[i-1])

n = int(input('Select Parameter : '))

parameter = parameters[n-1]

fig = px.box(df, y=parameter)
fig.write_html("html/file4.html", auto_open=True)
