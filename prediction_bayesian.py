from sklearn.linear_model import BayesianRidge
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

df = pd.read_csv('./data/sustainable_goals.csv')


regressor = BayesianRidge()

state = df.loc[df['state'] == "Bihar"]

years = ['2018', '2019', '2020']

x = list()
y = list()

for year in years:
    x.append(int(year[-2]+year[-1]))
    val = int(state[year])
    if(val > 100):
        y.append(100)
    else:
        y.append(val)

x = np.array(x).reshape(-1, 1)

regressor.fit(x, y)

y_predicted = regressor.predict(x)
accuracy = round(r2_score(y, y_predicted)*100, 2)

plt.title(f'Bayesian Regressor: Accuracy= {accuracy} %')
plt.xlabel('Year')
plt.ylabel('Composite score')
plt.scatter(x, y, color='red', label='actual')
plt.scatter(x, y_predicted, color='blue', label='predicted')
plt.legend()
plt.show()
