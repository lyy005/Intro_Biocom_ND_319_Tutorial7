#Part 1
import pandas
from plotnine import *

InFile=open("Lecture11.fasta","r") #Open fasta file as read-only

sequenceLength=[] #Set up variables to accept/store sequence data as it is calculated
percentGC=[]

for line in InFile: #Loop through each line in fasta file
    if '>' in line: #Check line for >, if present, skip to next line
        continue
    else:
        seqLen=float(len(line)) #Calculate length of sequence
        nG=line.count("G") #Count individual G and C contents
        nC=line.count("C")
        percGC=float(((nG+nC)/seqLen)*100) #Calculate % GC
    
        sequenceLength.append(seqLen) #Append length of individual sequences to list
        percentGC.append(percGC) #Append %GC of individual sequences to list

seqDF=pandas.DataFrame(list(zip(sequenceLength,percentGC)),columns=['sequenceLength','percentGC']) #combine lists into dataframe for easier plotting
a=ggplot(seqDF, aes(x="sequenceLength")) #Create plot of sequence lengths
a+geom_histogram()+theme_classic() #Plot as histogram

b=ggplot(seqDF, aes(x="percentGC")) #Create plot of %GC
b+geom_histogram()+theme_classic() #Plot as histogram

InFile.close() #Close file

#Part 3
import numpy

data=pandas.read_csv("data.txt", header=0, sep=",") #Open file as data frame

dataN=data[data.region=="north"] #Subset data frame & find mean for all populations
nMean=numpy.mean(dataN.observations)

dataE=data[data.region=="east"]
eMean=numpy.mean(dataE.observations)

dataW=data[data.region=="west"]
wMean=numpy.mean(dataW.observations)

dataS=data[data.region=="south"]
sMean=numpy.mean(dataS.observations)

means=pandas.DataFrame(columns=('region', 'mean')) #Combine means into new data frame
means.region='north','south','east','west'
means.iloc[0,1]=nMean
means.iloc[1,1]=sMean
means.iloc[2,1]=eMean
means.iloc[3,1]=wMean

c=ggplot(means, aes(x="region",y="mean")) #Plot means on bar graph
c+geom_col()+theme_classic()

d=ggplot(data, aes(x="region", y="observations")) #Plot all observations on scatter plot
d+geom_jitter()+theme_classic()

#Graphs tell different stories - only on the scatter plot does it become apparent that the observations
#in the south region are two discrete populations, rather than a continuous spread like the others.
#Additionally, the mean for the West region makes it look as though it has the smallest values, whereas
#the scatterplot shows that it has both the lowest and the highest values, over a very large spread.
#The mean barplot is really only an accurate respresentation for the North region.