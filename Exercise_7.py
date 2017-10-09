# Question 1
# I am not a big fan of plotnine, so I used the matplotlib and seaborn, which I think are a little bit more popular. 
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_table('/Users/chenyingying/Documents/Intro_Biocom_ND_319_Tutorial7/Lecture11.fasta',header=None)
df=pd.DataFrame(columns=['ID','Length','%GC'])
df['ID']=range(1,101,1)
for i in range(0,100,1):
    temp=data.iloc[i*2+1,0]
    df.iloc[i,1]=len(temp)
    df.iloc[i,2]=100*(temp.count('C')+temp.count('G'))/len(temp)
fig=plt.figure(figsize=(8,8))
fig.suptitle('Histogram')
ax1 = fig.add_subplot(121)
ax1=plt.hist(df['Length'],edgecolor="black")
plt.title('Sequence Length')
ax2 = fig.add_subplot(122)
ax2=plt.hist(df['%GC'],edgecolor="black")
plt.title('%GC')
# Question 2
import pandas as pd
import seaborn as sns
data_2=pd.read_table('/Users/chenyingying/Documents/Intro_Biocom_ND_319_Tutorial7/LakeGPP.txt',sep='\t')
sns.lmplot(x="TP_mgm3", y="GPP_mmolm3d", data=data_2,size=8)
#Question 3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
data_3=pd.read_table('/Users/chenyingying/Documents/Intro_Biocom_ND_319_Tutorial7/data.txt',sep=',')
le=LabelEncoder()
le.fit(data_3['region'])
data_3['Index']=le.transform(data_3['region'])
# Barplot of mean 
fig=plt.figure(figsize=(8,8))
data_3.groupby('region')['observations'].mean().plot.bar()
plt.title('Barplot of mean')
# Scatter plot
f2=sns.pairplot(x_vars=["Index"], y_vars=["observations"], data=data_3, hue="region",size=8)
f2.set(xticks=[0,1,2,3])
f2.set(xticklabels=['east','north','south','west'])
f2.set(xlabel='region')
f2.set(title='Scatter plot')