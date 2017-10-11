import pandas
import matplotlib.pyplot as plt

df = pandas.read_excel('patentsPerYear.xlsx')

data= df[['Calendar Year','Utility Patent Application (Inventions)']]
x=data['Calendar Year']
y=data['Utility Patent Application (Inventions)']
plt.scatter(x,y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

plt.show()