import pandas
InFile=open("Lecture11.fasta","r")
sequenceLength=[]
percentGC = []
for line in InFile:
    line = line.strip()
    if ">" in line:
        next
    else: 
        sequenceLength.append(len(line)-1)
        percentGC.append(1.0*(line.count("G")+line.count("C"))/len(line))
print(percentGC)