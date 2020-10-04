import matplotlib.pyplot as plt
import  pandas as pd
import numpy as np
data = pd.read_csv( 'project1.csv', parse_dates=[ 'Date' ], index_col= [ 'Date' ] )
data.head()
Date_new = data.index
#print("Date_new", Date_new)



'''
Daily_resampled_data = data.Received.resample('W').count()
print("monthly_resampled_data", Daily_resampled_data)
plt.xlabel("Number of complaint weekly basis")
plt.ylabel("Number of frequency")
plt.title("Number of complaints at monthly and daily granularity levels")
plt.bar(Daily_resampled_data, rwidth=.80, color= 'green', height= )

plt.show()
'''

weekly_resampled_data = data.Received.resample('M').count()

print("monthly_resampled_data", weekly_resampled_data)

frequency_table = data['Received'].value_counts()
print("frequency_table===\n", frequency_table)
mykeys = frequency_table.index
print("mykey = ",mykeys )
myvalues = frequency_table.values
print("values of frequency = ",myvalues )
frequency = pd.DataFrame({'Received': mykeys,'frequency': myvalues })
print("frequncy ",frequency )
max_com_type = max(frequency['frequency'])
print("maximum value of complaint type=",max_com_type )


x = np.arange(len(mykeys))
y= np.arange(len(myvalues))
plt.xlabel("Customer Care Call")
plt.ylabel("Internet")
plt.plot(x,y)

plt.show()
#cst_call_count = frequency_table
#print("data['Received'].values[0] = " , data['Received'].get('Customer Care Call'))

#new_df = pd.DataFrame({'Date':Date_new, 'custmer_c_call': data['Received'].values[0],'Internet': data['Received'].values[1]})
#new_df.head()

'''
 #data['frequency'].value_counts())

#print(new_df.shape)
#print(new_df.describe())
#print(new_date.index)
#new_date['Month'] = new_date.index.month
#print(new_date.loc['2015-06-25'])
#print("new_date['2015-04-18']", new_date['2015-04'])

#daily_resample1 = new_df.resample('D', on='Date').count()
#print("-------dily sample1---------",daily_resample1)
#plt.plot(weekly_resample1)
#plt.show()
#weekly_resample2 = new_df.Internet.resample('M').count()
#print("weekly_resample",weekly_resample2)
x = np.arange(len(Date_new))                 # the label locations

fig, ax = plt.subplots()            #this wrapper is useful to create custom layouts
width = 0.50  # the width of the bars
#these bars are connected to cases and deaths accordingly
#print("new_df['custmer_c_call'].values========", new_df['custmer_c_call'].count())


bar1 = ax.bar(x - width/2, new_df['custmer_c_call'].values, width, label='custmer_c_call',color='b')
bar2 = ax.bar(x + width/2, new_df['Internet'].values, width, label='Internet', color='g')
ax.set_ylabel('FREQUENCY')      #axis setting of Y label
ax.set_xlabel('DATE')       #axis setting of X label
ax.set_xticks(x)            #axis setting of X ticks
ax.set_xticklabels(daily_resample1)   #axis setting of X tick labels
ax.legend()
plt.show()



custmer_cust_call = new_df['custmer_c_call'].values
Internet1 = new_df['Internet'].values
legend = ['custmer_c_call', 'Internet']
plt.hist([custmer_cust_call, Internet1], color=['orange', 'green'])
plt.xlabel("Time")
plt.ylabel("Frequency")

plt.legend(legend)

plt.show()


#plt.bar(weekly_resample1,6 , label="Customer Care Call ", color='b')
#plt.bar(weekly_resample2,5, label="Internet", color='g')
#plt.legend()
#plt.show()



start, end = '2015-01', '2015-06'
# Plot daily and weekly resampled time series together
fig, ax = plt.subplots()
ax.plot(opsd_daily.loc[start:end, 'Solar'],
marker='.', linestyle='-', linewidth=0.5, label='Daily')
ax.plot(opsd_weekly_mean.loc[start:end, 'Solar'],
marker='o', markersize=8, linestyle='-', label='Weekly Mean Resample')
ax.set_ylabel('Solar Production (GWh)')
ax.legend();




Date = data['2015-01-01':'2016-01-01']
Date1 = Date.data.Received.resample('W')
(Date1)
df['A'].value_counts() 
df = pd.DataFrame({
    'Date': ['a', 'a', 'a', 'a', 'a', 'a', 'a',
              'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    'day': ['Mon', 'Tues', 'Fri', 'Thurs', 'Sat', 'Sun', 'Weds',
            'Fri', 'Sun', 'Thurs', 'Sat', 'Weds', 'Mon', 'Tues'],
    'amount': [1, 2, 4, 2, 1, 1, 2, 4, 5, 3, 4, 2, 1, 3]})
dfx = df.groupby(['group'])


#plt.plot(['weekly_resampled_data'],['frequency'] , label="Customer Care Call ", color='b')
#plt.bar(['frequency'], label="Internet", color='g')
plt.legend()
plt.show()


print(frequency.describe())
(frequency['Received'].count())

for Received, Received_df in frequency:
    print(Received)
    print(Received_df)
    weekly_resampled_data1 = data.Received.resample ( 'W' ).count ()

    print ( weekly_resampled_data1 )

print(frequency.max())
print(frequency.count())
plt.plot(weekly_resampled_data1)
#plt.show()


plt.bar(['weekly_resampled_data'],Y , label="Customer Care Call ", color='b')
plt.bar(['weekly_resampled_data'],Y, label="Internet", color='g')
plt.legend()
plt.show()



plt.hist(weekly_resampled_data, edgecolor="k")

plt.bar([weekly_resampled_data],bins = 5, label="Example one")

plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('Epic Graph\nAnother Line! Whoa')



weekly_resampled_data2 = data.Received_df.resample ( 'W' ).count ()
    plt.bar( [ 'Received' ], weekly_resampled_data1, label="Customer Care Call ", color='b' )
    plt.hist( [ 'Received_df'], weekly_resampled_data2, label="Internet", color='g' )

plt.show()'''

