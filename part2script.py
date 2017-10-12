import numpy
import pandas
import plotnine
from plotnine import *

Part2=pandas.read_csv("part2datacopy.txt", sep=",")
#print(Part2)

#plotting data in scatterplot with trendline
a=ggplot(Part2,aes(x="oil changes per year",y="cost of repairs($)"))+theme_classic()+geom_point()
a+xlab("oil changes per year")+ylab("cost of repairs($)")+stat_smooth(method="lm")
