import pandas as pd

file1 = "C:/quantium-starter-repo/data/daily_sales_data_0.csv"
file2 = "C:/quantium-starter-repo/data/daily_sales_data_1.csv"
file3 = "C:/quantium-starter-repo/data/daily_sales_data_2.csv"

#df1= pd.read_csv(file1)
#df2 =pd.read_csv(file2)
#df3= pd.read_csv(file3)

#output = pd.merge(df1,df2, how='inner')
#print(output)


files = [file1,file2,file3]
df = pd.DataFrame()
for file in files:
    data = pd.read_csv(file)
    #df = pd.merge([data,df], how='inner')
    df = pd.concat([df,data],axis = 0)
df.to_csv('merged_files.csv', index=True)
