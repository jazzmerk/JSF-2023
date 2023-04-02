import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import os
import pathlib


sample_directory= ("D:\Work\JSF 2023")#User types in the path where sample files are - doesn't have to be same as where Python code is
file_list = {}
file_count = 1
for file in os.listdir(sample_directory):# os.listdir automatically takes care of "backward" Windows path slashes
   
    if  file.endswith(".txt"):
        print( file_count," ", file)
        file_list [file_count]=file
        file_count=file_count+1
 print ("\n\n")
file_number=input("Enter the number of the file you want: ")

#Now user picks file
file_number=int(file_number)
chosen_file=(file_list[file_number])
print ("\n\n")
print("File Chosen is:   ","",chosen_file)

#User sets run and trigger data here###############################################################
max_num_of_runs=150
total_num_samples=10000
min_triggers_per_run=2000
#############################################################################################
my_data = [[000 for x in range(max_num_of_runs)] for y in range(total_num_samples)]  # col by row
filter_data = [[000 for x in range(max_num_of_runs)] for y in range(total_num_samples)] 
count =1
jcount=1

#User sets filter type and parameters here##############################################################
filter_type=signal.bessel
filter_order=2
critical_freq=2500
sampling_freq=1000000 
##################################################################################################
numerator,denominator=filter_type(filter_order,critical_freq,btype='Low',norm='mag',fs=sampling_freq) #This creates a digital filter.It returns the numerator and denominator polynomials of the filter function
print(numerator,denoominator)# to check if filter created correctly (optional)




with open(chosen_file, mode='r', encoding='utf-8' ) as f:

    graph_label = "Raw Signal"
    line = f.readline()
    while line:
        line = f.readline()
   
        if line =="\n":
            line = 0
        if line !="":
            test = int(line)
         
            if test < -1*min_triggers_per_run :   ## the end of a run is shown by a negative large number that also indicates number of triggers received
                if count > max_num_of_runs : # this is to eliminate the blank runs if we have several -2xxxs in a row, we got a trigger too soon and no data was taken
                    jcount=jcount+1
                    #print ("this is run # ", jcount, count, test)
                    test =0 ## reset both counters cause starting a new run
                    count=0
                             
            if test > -1*(min_triggers_per_run-1) :  ##  this is normal data stored in mydata array with first column the time index 1 to ~2100 time values, and the 2nd col is the run # usually about 50 - 100
                (my_data[count] [jcount])=test
                count=count+1  ## stored a good time value, so increment the counter
        if jcount >(max_num_of_runs):  # never more than 150 runs, if we are still going something wrong # why was this 148 instead of 150 in original code??
                break
        
         
my_data=np.array(my_data)  
filter_data = signal.lfilter(numerator, denominator,my_data,axis=0)#lfilter is what actually runs the signal through whatever filter was created previously



mpl.rcParams['figure.figsize'] = [12, 6]
fig, ax = plt.subplots(2)
plt.title(graph_label)
ax[0].plot(my_data[1:1000,1:10])# Increase to more points?? -JM
ax[1].plot(filter_data[1:1000,1:10])
plt.savefig ("Bessel.png")# plotting only the first 1000 ADC data points
                                                  # # there is a total of 2100 ADC voltage vs time points for 61 runs in the data file - only plotting a subset
plt.show()

     