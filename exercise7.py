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
#print(percentGC)

#So we need the data in a datafram to be used by ggplot aparantly. So here I put it in a dataframe
data=pandas.DataFrame({"Sequence Length": sequenceLength, "Percent GC": percentGC})

length=ggplot(data,aes(x="Sequence Length"))
length+geom_histogram()+theme_classic()

gc=ggplot(data,aes(x="Percent GC"))
gc+geom_histogram()+theme_classic()