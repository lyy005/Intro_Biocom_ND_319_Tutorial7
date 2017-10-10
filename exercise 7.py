#exercise 7#
#Dan Bruzzese and Zoe Loh





# question 1




#question2






#########question 3################
from plotnine import *
import pandas as pd
dat = pd.read_csv("data.txt")

#barplot  for mean observations in a region
grouped= dat.groupby(["region"]).mean().reset_index() #mean observations by region
print grouped
grouped.columns = ['region', 'mean_observations']
p= (ggplot(data=grouped)
    + aes(x='region', y= 'mean_observations',fill= 'region')
    + geom_bar(stat = "identity")
    + theme_classic()
    )
print p




