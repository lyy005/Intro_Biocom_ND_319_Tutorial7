import pandas as pd
import numpy as np
data=pd.read_csv("dataset.csv")
import matplotlib.pyplot as plt
plt.title('Percent of Planted Corn in USA that is GMO')
plt.ylabel('Percent')
plt.xlabel('Year')
plt.xlim([2000,2018])
plt.scatter(data.Year, data.Percent)
x=data.Year
y=data.Percent
z = np.polyfit(x,y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
