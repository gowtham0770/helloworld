
import pandas as pd


xlsx=pd.ExcelFile("/Users/gowtham/TestDB/Book1.xlsx")

"""df=('df1','df2','df3')

classes=('classa','classb','classc')

zipper=zip(df,classes)

z=(list(zipper))

print(z[0][0])

for i in range(0,3):
    for j in range(0,2):
        print("i=",i)
        print("j=",j)
        
        if(j==0):
            
            k=j+1
            temp=z[i][j]
            temp=pd.read_excel(xlsx,z[i][k]);
        else:
             temp=z[i][j]
             temp=pd.read_excel(xlsx,z[i][j]);
             
for i in range(0,3):
    print(df[i])
#        if(j==2):
#           {
             
             
#             }
           
#         if(j!=2):
#           
#          temp=z[i][j+1]
#          temp= pd.read_excel(xlsx,z[i][j+1])}

    
"""

df1=pd.read_excel(xlsx,'classa')
    
i=df1.set_index("Network Bits") 
print (i)

#df1=df.loc["/8":"/30","Network Bits":"Subnet Mask"]"""
   

