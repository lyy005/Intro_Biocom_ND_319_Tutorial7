import pandas

#Question 1
InFile=open("Lecture11.fasta","r")

#create lists for storing information about sequences
sequenceID=[]
sequenceLength=[]
percentGC=[]
meltingTemp=[]

#loop through each line in fasta file to process sequences
for Line in InFile:
    Line=Line.strip()
    if '>' in Line:
        sequenceID.append(Line[1:])
    else:
        seqLen=float(len(Line))
        nG=Line.count("G")
        nC=Line.count("C")
        
    #append values to lists
        sequenceLength.append(seqLen)
        percentGC.append((nG+nC)/seqLen*100)
        print(percentGC)
    
#combine lists into dataframe 
seqDF = pandas.DataFrame(list(zip(sequenceID,sequenceLength,percentGC)),columns=['sequenceID','sequenceLength','percentGC'])

#close file
InFile.close()
