# Exercise 7


#Question 1

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
histogram1+geom_histogram(binwidth=20,fill='blue',color='black')+theme_classic()

# histogram of percentGC
histogram2=ggplot(seqDF,aes(x="percentGC"))
histogram2+geom_histogram()+theme_classic()
# changing colors and bins
histogram2+geom_histogram(binwidth=15,fill='yellow',color='black')+theme_classic()

#Question 2


#Question 3

# open data file
q3north=0
q3south=0
q3west=0
q3east=0


for i in range(0,len(q3),1):
    if q3.region[i]=="north":
        q3north=q3north+q3.observations[i]
    elif q3.region[i]=="south":
        q3south=q3south+q3.observations[i]
    elif q3.region[i]=="east":
        q3east=q3east+q3.observations[i]
    elif q3.region[i]=="west":
        q3west=q3west+q3.observations[i]

q3north
q3south
q3west
q3east

avgnorth=(sum(q3.region=="north")/len(q3north))
sum(q3.region=="south")
sum(q3.region=="east")
sum(q3.region=="west")


import pandas
q3=pandas.read_csv("data.txt", sep=",", header=0)
average=q3.groupby('region')['observations'].mean()

regions=q3.groupby('region')['region']
seqDF=pandas.DataFrame(list(zip(average)),columns=['regions','observations'] set='\t')
df=average.to_frame(name=none)

#scatter plot with jitter applied
from plotnine import *
q3sp=ggplot(q3,aes(x="region",y="observations"))
q3sp+geom_jitter()+coord_cartesian()

