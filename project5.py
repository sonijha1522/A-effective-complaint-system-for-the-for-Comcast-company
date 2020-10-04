import matplotlib.pyplot as plt
import  pandas as pd
import numpy as np
import  numpy as np

df = pd.read_csv( 'project1.csv' )

print("date", df)

resolve_close = (df['Status'] =='Closed')
print("filter value +++++++++++++++++", resolve_close)
print("date who open===============",df.loc[resolve_close,'Received'])
df.head()

resolve_solve = (df['Status'] =='Solved')
print("filter value +++++++++++++++++", resolve_solve)
print("date who open===============",df.loc[resolve_solve,'Received'])
result1 = df.loc[resolve_close,'Received'].append(df.loc[resolve_solve,'Received'])
print(result1)
num_com = len(result1)
print("number of complain===",num_com )
total_num_com = len(df)
print("total number of complain===",total_num_com )

percentage_resolve_complain = (num_com/total_num_com)*100
print("percentage_resolve_complain", percentage_resolve_complain,"%")

#df = df.sort_values(["b", "c"], ascending = (False, True))
#print(df)

'''
Open_filt1 = (df['Status']=='Open')
print("filter value +++++++++++++++++", Open_filt1)
print(df[Open_filt1])
print("state who closed===============",df.loc[Open_filt1, 'State'])

Pending_filt2 = (df['Status']=='Pending')
print("filter pending value +++++++++++++++++", Pending_filt2)
print(df[Pending_filt2])
print("state who pending===============",df.loc[Pending_filt2, 'State'])
result1 = df.loc[Open_filt1, 'State'].append(df.loc[Pending_filt2, 'State'] )
print("df.loc[Open_filt1, 'State'] + df.loc[Pending_filt2, 'State']",result)
result_state_op_pen = result.unique()
print("result_state_open_pending >>>>>>>>>>>>>>>>>>>>>", result_state_op_pen)'''
