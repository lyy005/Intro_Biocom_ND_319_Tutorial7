#Question 3
#load the dataset
import pandas
import numpy
Data = pandas.read_csv("data.txt", sep=',')
#print (Data)

#making bar graph with region as x and ave as y
import plotnine
from plotnine import *
d=ggplot(Data)+theme_classic()+xlab("region")+ylab("Average")
d+geom_bar(aes(x="factor(region)",y="observations"),stat="summary",fun_y=numpy.mean)

#scatter plot of all observations
a=ggplot(Data,aes(x="region",y="observations"))
a+geom_jitter()+coord_cartesian()
