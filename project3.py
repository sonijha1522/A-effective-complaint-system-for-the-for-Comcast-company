import matplotlib.pyplot as plt
import  pandas as pd
import numpy as np
df = pd.read_csv( 'project1.csv', index_col= [ 'Status' ] )
new_status = df.index
new_state =df.index
df.head()
print(new_status)

frequency_table = new_status.value_counts()
print("frequency_table===\n", frequency_table)

mykeys = frequency_table.index
print("mykeys=",mykeys )
mykeys1 = frequency_table.index[0]
#print("solve=",mykeys1 )
mykeys2 = frequency_table.index[1]
#print("close=",mykeys2)

myvalues1 = frequency_table.values[0]
#print("myvalues=",myvalues1 )
myvalues2 = frequency_table.values[1]
#print("myvalues=",myvalues2 )
close_com = pd.DataFrame({'complaint_type': [mykeys1, mykeys2],'freqency':[myvalues1,myvalues2]})
print("close and solve", close_com)
open_com = pd.DataFrame({'complaint_type': ['Open', 'Pending'],'freqency':[363,154]})
print("open and pen", open_com)

statewise = pd.DataFrame({'complaint_type': ['Solved',' Closed', 'Open', 'Pending'],'freqency':[973,734, 363,154]})
print("The value of state wise",statewise)