import numpy
import pandas
from plotnine import *
Ex7=open("Lecture11.fasta", "r")
sequenceID=[]
sequenceLength=[]
percentGC=[]
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
b=ggplot(line,aes(x="sequenceLength"))
b+geom_histogram()+theme_classic
c=ggplot(line,aes(x="percentGC"))
c+geom_histogram()+theme_xkcd