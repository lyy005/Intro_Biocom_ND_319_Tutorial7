import numpy
import pandas
from plotnine import *
data=pandas.read_csv("data.txt",sep=",",header=0)


#produces bar plot for means of populations
barplot=ggplot(data)+theme_classic()+xlab("region")+ylab("observations")
barplot+geom_bar(aes(x="factor(region)",y="observations"),stat="summary",fun_y=numpy.mean)


#produces scatter plot with jittering of observations
scatterplot=ggplot(data,aes(x="region",y="observations"))
scatterplot+geom_point()+coord_cartesian()+geom_jitter()

#The bar plot clearly shows that the mean is about the same for each population. The scatterplot also shows that but less clearly.
#The new information the scatter plot reaveals is the spread abd grouping of data which was hidden in the bar plot