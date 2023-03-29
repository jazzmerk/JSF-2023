import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

mydata = [[000 for x in range(2100)] for y in range(2101)]  # col by row
count =1
jcount=1

#b,a=signal.bessel(2,1,btype='Low',norm='Mag',fs=2500)  

with open("1 run.txt", mode='r', encoding='utf-8' ) as f:

    graph_label = "Test Bessel filter"
    line = f.readline()
    while line:
        line = f.readline()
   
        if line =="\n":
            line = 0
        if line !="":
            test = int(line)
            print("this is sample # ", count, test)
            (mydata[count][jcount])=test 
            count=count+1  ## stored a good time value, so increment the counter
          
        
my_data=np.array(mydata)


mpl.rcParams['figure.figsize'] = [12, 6]
fig, ax = plt.subplots()
plt.title(graph_label)

ax.plot(my_data[1:1000,1:2])     # plotting only the first 1000 ADC data points for the first run only 
                                                     # there is a total of 2100 ADC voltage vs time points for 61 runs in the data file - only plotting a subset
plt.savefig("first 10 runs only.png")
plt.show()