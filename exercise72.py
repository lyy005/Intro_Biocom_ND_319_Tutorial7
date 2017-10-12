import numpy
import pandas
from plotnine import *
ice=pandas.read_csv("icecream.txt",sep=",",header=0)


scatter=ggplot(ice,aes(x="Temperature C",y="How much I want ice cream"))
scatter+geom_point()+coord_cartesian() + stat_smooth(method="lm")