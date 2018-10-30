
from h1b_statistic_lib import *

# initiate empty counter instance 
# see h1b_statisic_lib for definitions

job_type_counter = count_instances()
states_counter = count_instances()

with open(sys.argv[1], 'r') as f: 
	# only one line is read at a time
	
    header = f.readline().split(';')
    #get indices to parse delimiters correctly
    idx1,idx2,idx3 = get_indices(header)
    
    for line in f:
        data = [s.strip() for s in line.split(";")]
        # if invalid number of columns noted pre-process file
        if len(data) != len(header):
            data = clean(line) 
        if data[idx3] == 'CERTIFIED':
            job_type_counter[data[idx1].strip('"')] += 1
            states_counter[data[idx2].strip('"')] += 1

#We need the top 10 values
num_vals = 10
#total number of 'CERTIFIED' instances
total_counts = sum(job_type_counter.values()) 

write_output(job_type_counter.sort_by_val(num_vals),total_counts,sys.argv[2])
write_output(states_counter.sort_by_val(num_vals),total_counts,sys.argv[3])
