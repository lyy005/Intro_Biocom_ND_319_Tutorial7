Ex7=open("Lecture11.fasta", "r")
sequenceID=[]
sequenceLength=[]
for line in Ex7:
    line=line.strip()
    if '>' in line:
        sequenceID.append(line[1:])
    else:
        seqLen=len(line)
        G=line.count("G")
        C=line.count("C")
    sequenceLength.append(seqLen)
        