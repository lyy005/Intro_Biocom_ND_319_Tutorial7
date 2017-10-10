import numpy
import pandas
from plotnine import *


#Question 1
InFile=open("Lecture11.fasta","r")

#create lists for storing information about sequences
sequenceID=[]
sequenceLength=[]
percentGC=[]
meltingTemp=[]

#loop through each line in fasta file to process sequences
for Line in InFile:
    Line=Line.strip() #removes white space, tab, space, newline characters
    if '>' in Line:
        sequenceID.append(Line[1:])
        #print(Line[1:])
    else:
        seqLen=float(len(Line))
        nG=Line.count("G")
        nC=Line.count("C")
        
    #append values to lists
        sequenceLength.append(seqLen)
        percentGC.append((nG+nC)/seqLen*100)
    
#combine lists into dataframe 
seqDF = pandas.DataFrame(list(zip(sequenceID,sequenceLength,percentGC)),columns=['sequenceID','sequenceLength','percentGC'])
#min(seqDF.sequenceLength)

#close file
InFile.close()

#plots histogram of sequence length
b=ggplot(seqDF,aes(x="sequenceLength"))
b+geom_histogram(binwidth=5)+theme_classic()

#plots histogram of sequence length
b=ggplot(seqDF,aes(x="percentGC"))
b+geom_histogram(binwidth=5)+theme_classic()






