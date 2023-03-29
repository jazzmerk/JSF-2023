import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

my_data = [[000 for x in range(2100)] for y in range(2101)]  # col by row
filter_data=[[000 for x in range(2100)] for y in range(2101)]
count =1
jcount=1

b,a=signal.bessel(2,1,btype='LOw',norm='Mag',fs=2500)
print (b,a)

output=0 

with open("1 run.txt", mode='r', encoding='utf-8' ) as f:

    graph_label = "Raw Signal"
    line = f.readline()
    while line:
        line = f.readline()
   
        if line =="\n":
            line = 0
        if line !="":
            test = int(line)
            #print("this is sample # ", count, test)
            (my_data[count][jcount])=test 
            count=count+1  ## stored a good time value, so increment the counter
            
my_data=np.array(my_data)  
filter_data = signal.lfilter(b, a,my_data)
#print("this is filtered sample # ", count, output)


mpl.rcParams['figure.figsize'] = [12, 6]
fig, ax = plt.subplots(2)
plt.title(graph_label)
ax[0].plot(my_data[1:1000,1:2])
ax[1].plot(filter_data[1:1000,1:2])
plt.savefig ("Bessel.png")# plotting only the first 1000 ADC data points for the first run only 
                                                  # there is a total of 2100 ADC voltage vs time points for 61 runs in the data file - only plotting a subset
plt.show()

     