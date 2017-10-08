import pandas
from plotnine import *
football=pandas.read_csv("NFL-graph-for-class.txt", sep='\t',header=0)
football.shape
(ggplot(football) + aes('Pats-Win-Tot','Lions-Win-Tot') + geom_point() + geom_smooth(method='lm'))