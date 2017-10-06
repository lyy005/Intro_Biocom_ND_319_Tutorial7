import pandas
import numpy

InFile=open("Lecture11.fasta","r")

A = numpy.zeros((100,4)) #tells python how big we want the table to be. 
B = pandas.DataFrame(A,columns=['seqNum','seqLength','Gcontent','Ccontent']) #labels each column

for line in InFile:
    Line=Line.strip()
    if '>' in Line:
        
    else:
        seqLen=float(len(Line))
        seqLen=B.iloc[i,1]
        
        nG=Line.count("G")
        nG=B.iloc[i,2]
        
        nC=Line.count("C")
        nC=B.iloc[i,3]