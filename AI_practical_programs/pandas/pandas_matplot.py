import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('SampleData.csv')

x = data['Date']
y = data['Cost']


plt.ylabel('COST')
plt.xticks(rotation = 45)
plt.xlabel('DATE')
plt.plot(x, y)
plt.show()