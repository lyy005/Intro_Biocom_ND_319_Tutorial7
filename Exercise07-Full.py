#Part 1
import numpy
import pandas
from plotnine import *

#load data
Ex7=open("Lecture11.fasta", "r")

sequenceID=[]
sequenceLength=[]
percentGC=[]

#Determine G:C content
for line in Ex7:
    line=line.strip()
    if '>' in line:
        sequenceID.append(line[1:])
    else:
        seqLen=float(len(line))
        G=line.count("G")
        C=line.count("C")
    sequenceLength.append(seqLen)
    percentGC.append((G+C)/seqLen*100)

#Generate histogram of G:C content    
b=ggplot(line,aes(x="seqID"))
b+geom_histogram()+theme_classic

#Part 2
import pandas
from plotnine import *
football=pandas.read_csv("NFL-graph-for-class.txt", sep='\t',header=0)
football.shape
(ggplot(football) + aes('Pats-Win-Tot','Lions-Win-Tot') + geom_point() + geom_smooth(method='lm'))

#Part 3
import pandas
import numpy
from plotnine import *

#load data
data=pandas.read_csv("data.txt")

#Barplot for the population means
means=ggplot('data')+theme_classic()+xlab("Populations")+ylab("Mean Number of Observations")
+means+geom_bar(aes(x="factor(region)",y="observations",fill="region"),stat="summary",fun_y=numpy.mean)+ggtitle("Population Means")

#Barplot means calculated for check(not necessary)
data.groupby(['region'])['observations'].mean()
#means are slightly different

#Scatterplot for the observations
scatter=ggplot(data,aes('observations','region'))
scatter+geom_jitter(aes(color='factor(region)'))+theme_classic()+ggtitle('All Observations')
#could have used scatter+geom_jitter()+coord_cartesian() instead
#Scatterplot shows that although the average observations seem to be similar across the regions, the observation distributions are different.

#Why?
#Barplot shows the means for the regional observations whilst the scatterplot shows the values for the all of the observations from each region.
