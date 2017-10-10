#exercise 7#
#Dan Bruzzese and Zoe Loh





# question 1




#question2






#question 3
#making the plot
from plotnine import *

import pandas
dat = pandas.read_csv("data.txt")

#barplot  for mean observations in a region
dat_grp= dat['observations'].groupby(dat['region']) #group observations by region
dat_mean= dat_grp.mean() # mean of the dat grp into a list

df = pandas.DataFrame({'col':dat_mean})  #turn list into a dataframe
print (df)
print df[0:4]
#only has one row....



