#Part 3
import pandas
import numpy
from plotnine import *

#load data
data=pandas.read_csv("data.txt")

#Barplot for the population means
means=ggplot('data')+theme_classic()+xlab("Populations")+ylab("Mean Number of Observations")
+means+geom_bar(aes(x="factor(region)",y="observations",fill="region"),stat="summary",fun_y=numpy.mean)+ggtitle("Population Means")

#bar plot means calculated for check
data.groupby(['region'])['observations'].mean()
#means are slightly different

#Scatterplot for the observations
scatter=ggplot('data',aes('observations','region'))
scatter+geom_jitter(aes(color='factor(region)'))+theme_classic()+ggtitle('All Observations')
#Scatter plot shows that although the average observations seem to be similar across the regions, the observation distributions are different.
