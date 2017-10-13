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
