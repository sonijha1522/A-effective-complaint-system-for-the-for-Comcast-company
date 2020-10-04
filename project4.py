import matplotlib.pyplot as plt
import  pandas as pd
import numpy as np
import  numpy as np
from textwrap import wrap
df = pd.read_csv( 'project1.csv' )

data = df[:len(df)][['State','Status']]
print("data", data)
freq_state_status = df[:len(df)][['State','Status']]._values
print("freq_state_status", freq_state_status)
state = data.iloc[:,0]
Status = data.iloc[:,1]
name_States = df.State.unique()
print("state wise.......................",name_States )
num_States = np.count_nonzero(name_States)
print("num_States.......................", num_States)


close_filt1 = (df['Status']=='Closed')
print("filter value +++++++++++++++++", close_filt1)
print(df[close_filt1])
print("state who closed===============",df.loc[close_filt1, 'State'])

solved_filt2 = (df['Status']=='Solved')
print("filter value +++++++++++++++++", solved_filt2)
print(df[solved_filt2])
print("state who Solved===============",df.loc[solved_filt2, 'State'])
result = df.loc[close_filt1, 'State'].append(df.loc[solved_filt2, 'State'] )
print("resolved complained======",result)
result_state_cl_sol = result.unique()
print("result_state_cl_sol>>>>>>>>>>>>>>>>>>>>>", result_state_cl_sol)

freq_state_cl_sol1 = result.value_counts()
print("freq_state_cl_sol--------------------resolve", freq_state_cl_sol1)

X = freq_state_cl_sol1.values
print("x=======", X)
print("length of x=====================", len(X))


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
print("result_state_open_pending >>>>>>>>>>>>>>>>>>>>>", result_state_op_pen)



freq_state_op_pen = result1.value_counts()
print("freq_state_open_pending--------------------", freq_state_op_pen)



y = freq_state_op_pen.values
print("y++++++++++++++", y)
print("length of y=====================", len(y))
temp_array = []
sum_val_y = 0
for counter1 in range (0,len(y)):
    sum_val_y = sum_val_y + y[counter1]

print("sum_val_y = ", sum_val_y)
for counter in range (0, len(y)):
    percentage_unresolve = (y[counter]/sum_val_y)*100
    print("percentage_unresolve",percentage_unresolve, "%")


'''
status_freq = Status.value_counts()
print("freq open=======================", status_freq)
state_freq = state.value_counts()
maximum_state_com = max(state_freq)
print(" maximum complaint state>>>>>>>>>>>>>", maximum_state_com)
print("state_freq", state_freq)
index = np.arange(len(data))
print(index,state, Status)
plt.plot(state_freq)
plt.xlabel("Statewise")
plt.ylabel("Number of complaint type")
plt.show()

#plt.pie(freq_state_cl_sol1, labels= result_state_cl_sol) # pie chart of resolve complaint
#plt.title("Pie chart of resolve complaint")

#plt.show()


X1 = freq_state_cl_sol1.index.unique()  #  RESOLVE COMPLAINS
print("X...........", X1)
print(len(X))
y1= freq_state_cl_sol1.values
print("y...........", y1)



N = 43
xvalues = np.arange(N)

plt.bar(xvalues,X1 ,color='b', label ='Closed')
plt.bar(xvalues,y1 , color='r', bottom =X1, label = 'Solved')
plt.xticks(xvalues, (name_States) )

plt.xlabel('States')
plt.ylabel('no. of complain')
plt.title('Stacked Bar Graphs')
plt.legend()
plt.show()
'''

X2 = [208,201,159,135,110 ,96,92,75,63,58,56,50,50 ,49  ,49  ,36,29,23,
  17,16,15,14,14,12,11,9,8, 8,8 ,6  ,6 , 4, 3 ,3 ]  #  RESOLVE COMPLAINS
print("X2...........", X2)

y2= freq_state_op_pen.values
print("y2...........", y2)     #UNRESOLVE COMPLAINS



N = 34
xvalues = np.arange(N)

plt.bar(xvalues,X2 ,color='b', label ='RESOLVE COMPLAINS')
plt.bar(xvalues,y2 , color='r', bottom =X2, label = 'UNRESOLVE COMPLAINS')
plt.xticks(xvalues, (name_States) )

plt.xlabel('States')
plt.ylabel('no. of complain')
plt.title('Stacked Bar Graphs')
plt.legend()
plt.show()


















'''

#close_com = pd.DataFrame({'state':[state_freq],'complaint_type': ['Solved', 'Closed'],'freqency':[973,734]})
#print("close and solve", close_com)



#.figure(figsize=(10,7))


graphMath = plt.bar(x = index, height=state, width=0.35)
graphReading = plt.bar(x = index, height=Status, width=0.35, bottom=Status)
plt.xlabel("Status")
plt.ylabel("state")
plt.show()

new_status = df.index
new_state =df.index
df.head()
print("new_status", new_status)
print("new_state", new_state)

frequency_table = new_state.value_counts()
print("frequency_table===\n", frequency_table)










mykeys = frequency_table.index
print("mykeys=",mykeys )
myvalues = frequency_table.values
close_com = pd.DataFrame({'complaint_type': ['Solved', 'Closed'],'freqency':[973,734]})
print("close and solve", close_com)
open_com = pd.DataFrame({'complaint_type': ['Open', 'Pending'],'freqency':[363,154]})
print("open and pen", open_com)

final_com = pd.DataFrame({'complaint_type': ['Solved', 'Closed','Open', 'Pending'],'freqency':[973,734, 363,154]})
print("final dataframe", final_com)

plt.plot(mykeys)
plt.legend(frequency_table)
plt.show()'''