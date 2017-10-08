import pandas
from plotnine import *
football=pandas.read_csv("NFL-graph-for-class.csv", sep='\t',header=0)
football.shape
a=ggplot(football,aes(x="Year",y="Pats-Wins-Tot"))
b=ggplot(football,aes(x="Year",y="Lions-Wins-Tot"))
