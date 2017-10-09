# open fasta file
InFile=open("Lecture11.fasta","r")

#create lists for storing information about sequences
sequenceID=[]
sequenceLength=[]
percentGC=[]

#loop through each line of fasta file to process sequences
for Line in InFile:
    # remove newline character from file line
    Line=Line.strip()
    # if a sequence record
    if '>' in Line:
        # add the sequence ID (except the ">" character) to the sequenceID list
        sequenceID.append(Line[1:])
    # if a sequence line
    else:
        # get the number of characters in the sequence and convert to a float to avoid integer division
        seqLen=float(len(Line))
        # count the number of G's and C's
        nG=Line.count("G")
        nC=Line.count("C")
        
        # append values to the lists
        sequenceLength.append(seqLen)
        percentGC.append((nG+nC)/seqLen*100)

import pandas
# combine lists into dataframe
seqDF = pandas.DataFrame(list(zip(sequenceID,sequenceLength,percentGC)),columns=['sequenceID','sequenceLength','percentGC'])

from plotnine import *
# histogram of sequence length
histogram1=ggplot(seqDF,aes(x="sequenceLength"))
histogram1+geom_histogram()+theme_classic()


