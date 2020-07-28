import pandas as pd
import random
import numpy as np

#Read original and reference excel
data = pd.read_excel(".\\tryA.xlsx")
ref_data = pd.read_excel(".\\tryB.xlsx")

#Make dataframe after data reading from excel

df = pd.DataFrame(np.random.randint(0,100, size=(16,6)), 
columns = ['SL No', 'Division Name', 'Total books', 'Scanned', 'Verified', 'Completed'])

df1 = pd.DataFrame(np.random.randint(0,100, size=(16,6)), 
columns = ['SL No', 'Division Name', 'Total books', 'Scanned', 'Verified', 'Completed'])
print(df)

divsion_name_list = [
'Nenei Nidines',
'Pugatan',
'Siari Botocos Kingdom',
'Niai Siarwan',
'Imarmai',
'Western Giaalmarbo',
'Vialyso',
'Ninor Ratedle',
'Southngacar',
'Bubar Saintmi',
'Subritish Isles',
'Slandmacsouth',
'Hunistacen',
'Guaran Miu',
'Rifolkla',
'Manbel Doriof',
]
for i in range(0, 16):
    df.loc[i,'SL No'] = i+1
    df1.loc[i,'SL No'] = i+1
    
df['Division Name'] = divsion_name_list
df1['Division Name'] = divsion_name_list
print(df)

#Insert random value in columns in descending order in original dataframe A
a = 100
b = 300
for i in range(5,1,-1):
    df.iloc[:, i] = np.random.randint(a,b, size=16)
    a = b+1
    b+=200

#Insert random value in columns in descending order in reference dataframe B
a = 100
b = 300
for i in range(5,1,-1):
    df1.iloc[:, i] = np.random.randint(a,b, size=16)
    a = b+1
    b+=200

print(df)
print(df1)
#The above step is performed as a demo to prevent manual entering of values in 4 columns each in both excel.

#Create new excel sheet after inserting data 
df.to_excel('fileA.xlsx')
df1.to_excel('fileB.xlsx')

#Make the dataframe out of it 
data = pd.read_excel(".\\fileA.xlsx")
ref_data = pd.read_excel(".\\fileB.xlsx")
df = pd.DataFrame(data)
df1 = pd.DataFrame(ref_data)

#Create dictionary for each column

dict_books = dict(zip(df1['Division Name'], df1['Total books']))
dict_scanned = dict(zip(df1['Division Name'], df1['Scanned']))
dict_verified = dict(zip(df1['Division Name'], df1['Verified']))
dict_completed = dict(zip(df1['Division Name'], df1['Completed']))

#Perform the required operation.

#Copying the values from reference datframe as a new column in original dataframe
df['Total books_new'] = df['Division Name'].apply(lambda x : dict_books[x])
df['Scanned books_new'] = df['Division Name'].apply(lambda x : dict_scanned[x])
df['Verified books_new'] = df['Division Name'].apply(lambda x : dict_verified[x])
df['Completed books_new'] = df['Division Name'].apply(lambda x : dict_completed[x])


#Comparing the values from ref and original dataframe and inserting values with highest value from both after comparison.
print(df.iloc[:, [3, 7]])
row_list = []
for i in range(0, 16):
    j = 0
    row_list = df.iloc[i, 3:7].values
    if (row_list[::-1] == row_list[:]).all():
        continue
    else:
        while(j < 4):
            if (df.iloc[i, 3 + j]  < df.iloc[i, 7+j]):
                if j > 0:
                    if (df.iloc[i, 7+j] < df.iloc[i, 3 + j - 1]):
                        df.iloc[i, 3 + j] = df.iloc[i, 7 + j]
                        df.loc[i, 'Remarks'] = 'Copied cell value'
                else:
                    df.iloc[i, 3 + j] = df.iloc[i, 7 + j]
                    df.loc[i, 'Remarks'] = 'Copied cell value'
            j+=1

print(df)

#Export the data in new excel
df.to_excel('final_value.xlsx')

#Remove the unnecessary columns after that from output excel.