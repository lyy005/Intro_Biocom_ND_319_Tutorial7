#exercise 7#
#Dan Bruzzese and Zoe Loh





# question 1
import pandas
File=open("Lecture11.fasta","r")
plotData = pandas.DataFrame(columns = ["Sequence Length" , "GC content"])

for line in File:
    line = line.strip()
    if ">" in line:
        continue
    else:
        #First the length of the sequence and the percent gc count is calculated
        Length = (len(line)-1)
        #Because it is integer division we must force python do divide as if it was real numbers by using float()
        GCcount = (float((line.count("G"))+line.count("C"))/len(line))
        #The values are inserted into a dataframe for plotting
        row = pandas.DataFrame({"Sequence Length": Length, "GC content": GCcount}, index=[0])
        plotData = plotData.append(row)
#GC histogram plot
a=ggplot(plotData,aes(x="GC content"))
a+geom_histogram()+theme_classic()        

#sequence length histogram plot
b=ggplot(plotData,aes(x="Sequence Length"))
b+geom_histogram()+theme_classic()

#question2

import pandas
from plotnine import *
data=pandas.read_csv("heartrate.txt",sep=",",header=0)

#Here I make the scatter plot showing how running speed and heart rate are related
plot=ggplot(data,aes(x="Heart rate",y="Running speed"))
plot+geom_point()+coord_cartesian()+stat_smooth(method="lm")


#########question 3################
from plotnine import *
import pandas as pd
dat = pd.read_csv("data.txt")

#barplot  for mean observations in a region
grouped= dat.groupby(["region"]).mean().reset_index() #mean observations by region
print grouped
grouped.columns = ['region', 'mean_observations']
p= (ggplot(data=grouped)
    + aes(x='region', y= 'mean_observations',fill= 'region')
    + geom_bar(stat = "identity")
    + theme_classic()
    )
print p

#scatterplot
d= (ggplot(data=dat)
    + aes(y='observations', x='region', fill= 'region')
    + geom_point(alpha= .01)
    + theme_classic()
    )
print d
 # why= the bar chart shows us the mean of observations from each region
#while the scatter plot shows us the value of all  observations from each region
