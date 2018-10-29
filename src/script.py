
from function_library import *


cnt_jobs = Counter()
cnt_state = Counter()

with open(sys.argv[1], 'r') as f: 
    header = f.readline().split(';')
    idx1,idx2,idx3 = get_indices(header)
    
    for line in f:
        data = [s.strip() for s in line.split(";")]
        if len(data) != len(header):
            data = clean(line)
        if data[idx3] == 'CERTIFIED':
            cnt_jobs[data[idx1].strip('"')] += 1
            cnt_state[data[idx2].strip('"')] += 1

write_output(cnt_jobs,'occupations',sys.argv[2])
write_output(cnt_state,'state',sys.argv[3])
