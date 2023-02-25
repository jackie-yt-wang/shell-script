import pandas as pd
import os 
import glob
InputPath = os.environ.get('INPUT_FOLDER')
OutputPath = os.environ.get('OUT_FOLDER')
OutputFileName ='all_years.csv'
FilePathNames = glob.glob(InputPath+'/*.csv')
DF = pd.DataFrame()

TempDFCount=[]
for file in FilePathNames:
    TempDF = pd.read_csv(file)
    TempDFCount.append(TempDF.shape[0])
    DF = pd.concat([DF,TempDF]) 


print('are the count equal?',str(sum(TempDFCount)),str(DF.shape[0]))
DF.to_csv(OutputPath+'/'+OutputFileName,index=False)



