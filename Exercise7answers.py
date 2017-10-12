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

#open file and import pandas
import pandas
q3=pandas.read_csv("data.txt", sep=",", header=0)

#group by the region and find the mean of each region
average=q3.groupby('region')['observations'].mean()
#print to dataframe
df=average.to_frame()
#add the region rows - can find the order if you print the previous variable
df['region']=["east", "north", "south", "west"]

#making a bar graph with the avg of the corresponding regions
from plotnine import *
q3bp=ggplot(df)+theme_classic()+xlab("region")+ylab("observations")
q3bp+geom_bar(aes(x="region",y="observations"),stat="summary",)

#scatter plot with jitter applied
from plotnine import *
q3sp=ggplot(q3,aes(x="region",y="observations"))
q3sp+geom_jitter()+coord_cartesian()


