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