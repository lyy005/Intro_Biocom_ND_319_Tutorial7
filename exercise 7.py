#exercise 7#
#Dan Bruzzese and Zoe Loh





# question 1




#question2






#question 3
#making the plot
from plotnine import *

import pandas
dat = pandas.read_csv("data.txt")

print dat.head(n=5)

#need graph for mean

p=(ggplot(data=dat)
   + aes( "region", "observations")
   + geom_bar(stat = "identity")
   + theme_classic()
)

print p

