# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:32:42 2019

@author: Nagasudhir
"""

# import pandas library into variable named pd
import pandas as pd

# import an excel file as a pandas dataframe
df = pd.read_excel('schdc.xlsx', sheet_name = 'Sheet 1')

# find the dimension of dataframe df
dim = df.shape

# find columns of dataframe
colList = df.columns.tolist()

# find the index of dataframe
indexItems = df.index.tolist()

# get the size of index
indexSize = len(df.index)

# get the number of columns
numCols = len(colList)

# access the cell of position 100,2 in dataframe
val = df.iloc[100, 2]

# access the cells of column 2 in dataframe
col3 = df.iloc[:, 2]

# access the cells of column Time_Net Sch in dataframe
colTimeNetSch = df['Time_Net Sch']

# append blank column named blankCol
df['blankCol'] = ""

# duplicate this column and append as DupCol
df['DupCol2'] = df['Time_Net Sch']

# export dataframe as csv_export.csv in exports folder
df.to_csv('exports/csv_export.csv')
