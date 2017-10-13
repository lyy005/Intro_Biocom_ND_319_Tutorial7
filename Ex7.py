cd Desktop/Intro_Biocom_ND_319_Tutorial7/


import pandas as pd

InFile=open("Lecture11.fasta","r")

#create lists for storing information about sequences
sequenceID=[]
sequenceLength=[]
percentGC=[]
meltingTemp=[]

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
        
        # if the sequence is 14 or fewer bases calculate melting temperature
        if seqLen<=14:
            Tm=2*(nG+nC)+2*seqLen
        else:
            Tm=-9999
        
        # append values to the lists
        sequenceLength.append(seqLen)
        percentGC.append((nG+nC)/seqLen*100)
        meltingTemp.append(Tm)

# combine lists into dataframe
seqDF = pandas.DataFrame(list(zip(sequenceID,sequenceLength,percentGC,meltingTemp)),columns=['sequenceID','sequenceLength','percentGC','meltingTemp'])

# close file
InFile.close()


import plotnine

#ex 1.1, histogram of sequence length
plot1=plotnine.ggplot(seqDF, plotnine.aes('sequenceLength'))
plot1 + plotnine.geom_histogram(binwidth=5)

#ex 1.2, histogram of GC content
plot2=plotnine.ggplot(seqDF, plotnine.aes('percentGC'))
plot2 + plotnine.geom_histogram(binwidth=5)

#ex 2, data of speed and stopping distance of cars.csv
cars=pd.read_csv("cars.csv")

plot3=plotnine.ggplot(cars, plotnine.aes('speed','dist'))
plot3 + plotnine.geom_point() + plotnine.geom_smooth()

