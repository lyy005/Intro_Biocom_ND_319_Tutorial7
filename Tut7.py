import os

os.chdir("Intro_Biocom_ND_319_Tutorial7/")

fasta = open("Lecture11.fasta", "r")

sequenceID=[]
sequenceLength=[]
percentGC=[]
meltingTemp = []

for Line in fasta:
    Line = Line.strip()
    if '>' in Line:
        sequenceID.append(Line[1:])
    else:
        seqLen=float(len(Line))
        
        if seqLen <= 14:
            Tm=2*(nG+nC)+2*seqLen 
        else: 
            Tm=-9999

        nG=Line.count("G")
        nC=Line.count("C")
        

    sequenceLength.append(seqLen)
    percentGC.append((nG+nC)/seqLen*100)
    meltingTemp.append(Tm)
    
from plotnine import *
from matplotlib import pyplot as plt

plt.hist(percentGC, bins = 11)
plt.title('Percent GC content distribution')
plt.xlabel('GC Content (%)')
plt.ylabel('count')

plt.show()
