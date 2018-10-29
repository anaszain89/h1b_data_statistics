import re
from collections import Counter
import sys

##
def clean(line):
    line = re.sub(r'\(|\)|\\','',line)
    matches = re.findall('\".+?\"',line)
    for match in matches:
        line = re.sub(''.join(match),''.join(match).replace(';',''),line)
    return [s.strip() for s in line.split(";")]

##
def get_indices(header):
	try:
		idx1 = header.index('LCA_CASE_SOC_NAME')
		idx2 = header.index('LCA_CASE_WORKLOC1_STATE')
		idx3 = header.index('STATUS')
	except:
		idx1 = header.index('SOC_NAME')
		idx2 = header.index('WORKSITE_STATE')
		idx3 = header.index('CASE_STATUS')
	return idx1,idx2,idx3

##
def write_output(obj_counter,case,nfile):
	if case == 'state':
		filename = nfile
		op_header = ('TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE')
	elif case == 'occupations':
		filename = nfile
		op_header = ('TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE')
	
	sorted_list = sorted(obj_counter.items(), key=lambda item: (-item[1], item[0]), reverse = False)
	with open(filename,'w') as op_file:
		print('%s;%s;%s' %op_header,file=op_file)
		for item in sorted_list[:10]:
			print('%s;%i;%0.1f%%' %(item[0],item[1],item[1]*100/sum(obj_counter.values())),file=op_file)
	op_file.close()
 	

