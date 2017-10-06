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
print sequenceLength
print percentGC
        