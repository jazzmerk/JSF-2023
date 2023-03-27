import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

mydata = [[000 for x in range(150)] for y in range(200)]  # col by row
count = 0
jcount=1

b,a=signal.bessel(2,1,btype='Low',norm='Mag',fs=2500)  

with open("A Now with coil NO 120 in opamp 25mV at scope about d68mV across 68 ohms .txt", 
mode='r', encoding='utf-8' ) as f:

    graph_label = "A Now with coil NO 120 in opamp 25mV at scope about d68mV across 68 ohms .txt"
    line = f.readline()
    while line:
        line = f.readline()
   
        if line =="\n":
            line = 0
        if line !="":
            test = int(line)
         
            if test < -2000 :   ## the end of a run is shown by a negative large number that also indicates number of triggers received
                if count > 100 : # this is to eliminate the blank runs if we have several -2xxxs in a row, we got a trigger too soon and no data was taken
                    jcount=jcount+1
                    print ("this is run # ", jcount, count, test)
                    test =0 ## reset both counters cause starting a new run
                    count=0
                             
            if test > -1999 :  ##  this is normal data stored in mydata array with first column the time index 1 to ~2100 time values, and the 2nd col is the run # usually about 50 - 100
                (mydata[count] [jcount])=test
                count=count+1  ## stored a good time value, so increment the counter
        
        
        
my_data=np.array(mydata)


mpl.rcParams['figure.figsize'] = [12, 6]
fig, ax = plt.subplots()
plt.title(graph_label)

ax.plot(my_data[1:100,1:2])     # plotting only the first 100 ADC data points for the first 2 runs only - super imposed on each other.
                                                     # there is a total of 2100 ADC voltage vs time points for 61 runs in the data file - only plotting a subset

plt.show