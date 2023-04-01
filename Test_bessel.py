import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import os
import pathlib


sample_directory= ("D:\Work\JSF 2023")
file_list = [[0 for x in range (100)]for y in range(100)]
file_count =1
for file in os.listdir(sample_directory):
   
    if file.endswith(".txt"):
        file_list =([file_count],file)
        print( file_count," ", file)
        file_count=file_count+1
       

print ("\n\n")
file_number=input("Enter the number of the file you want: ")

file_number=int(file_number)

chosen_file=(file_list[file_number:file_number])
print ("\n\n")
print("File Chosen is ",chosen_file)




# max_num_of_runs=150
# total_num_samples=10000
# min_triggers_per_run=2000

# my_data = [[000 for x in range(max_num_of_runs)] for y in range(total_num_samples)]  # col by row
# filter_data = [[000 for x in range(max_num_of_runs)] for y in range(total_num_samples)] 
# count =1
# jcount=1

# filter_type=signal.bessel
# filter_order=2
# critical_freq=2500
# sampling_freq=1000000 #sampling frequency
# numerator,denominator=filter_type(filter_order,critical_freq,btype='Low',norm='mag',fs=sampling_freq) #This creates a digital filter.It returns the numerator and denominator polynomials of filter function
# #print(numerator,denoominator)# to check if filter created correctly




# with open("A Now with coil NO 120 in opamp 25mV at scope about d68mV across 68 ohms .txt", mode='r', encoding='utf-8' ) as f:

    # graph_label = "Raw Signal"
    # line = f.readline()
    # while line:
        # line = f.readline()
   
        # if line =="\n":
            # line = 0
        # if line !="":
            # test = int(line)
         
            # if test < -1*min_triggers_per_run :   ## the end of a run is shown by a negative large number that also indicates number of triggers received
                # if count > max_num_of_runs : # this is to eliminate the blank runs if we have several -2xxxs in a row, we got a trigger too soon and no data was taken
                    # jcount=jcount+1
                    # #print ("this is run # ", jcount, count, test)
                    # test =0 ## reset both counters cause starting a new run
                    # count=0
                             
            # if test > -1*(min_triggers_per_run-1) :  ##  this is normal data stored in mydata array with first column the time index 1 to ~2100 time values, and the 2nd col is the run # usually about 50 - 100
                # (my_data[count] [jcount])=test
                # count=count+1  ## stored a good time value, so increment the counter
        # if jcount >(max_num_of_runs):  # never more than 150 runs, if we are still going something wrong
                # break
        
         
# my_data=np.array(my_data)  
# filter_data = signal.lfilter(numerator, denominator,my_data,axis=0)#lfilter actually runs signal through whatever filter is created



# mpl.rcParams['figure.figsize'] = [12, 6]
# fig, ax = plt.subplots(2)
# plt.title(graph_label)
# ax[0].plot(my_data[1:1000,1:10])
# ax[1].plot(filter_data[1:1000,1:10])
# plt.savefig ("Bessel.png")# plotting only the first 1000 ADC data points
                                                  # # there is a total of 2100 ADC voltage vs time points for 61 runs in the data file - only plotting a subset
plt.show()

     