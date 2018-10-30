import re
import sys

##
class count_instances(dict):
    '''Instance counter implemented as a Dict subclass.
    Elements are stored as dictionary keys and their counts
    are stored as dictionary values.
    NOTE:  An alternative to this can be using the Counter object in Collections,
    which may provide a more wider range of functionality than this fuction
    
    '''

    def __init__(*args, **kwds):
        '''Initial an empty object for counting instances.
        '''
        self, *args = args
        super(count_instances, self).__init__()
        self.update(*args, **kwds)

    def __missing__(self, key):
        '''This ensures that a missing key does not raise KeyError
        '''
        return 0

    def sort_by_val(self, n=None):
        '''Function to sort through the counted instances using the values first
        and then in case of ties, alphabetically
        '''
        if n is None: n=len(self.items())
        return sorted(self.items(), key=lambda item: (-item[1], item[0]), reverse = False)[:n]
##
def clean(line):
    '''This function is used to process through a line from the file if parsing
    does not work properly '''

    # We first search for and ignore any special characters which may effect REGEX
    line = re.sub(r'(?i)[^a-z0-9;" +-]','',line)
    # Find portions of string within " ", look for ';' and replace them
    matches = re.findall('\".+?\"',line)
    for match in matches:
        line = re.sub(''.join(match),''.join(match).replace(';',''),line)
    return [s.strip() for s in line.split(";")]

##
def get_indices(header):
    '''This function is used to get valid indices from the header of each file
    Files prior to 2014 have the first format while the laters ones have the second
    one. '''
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
def write_output(sorted_list,total,nfile):
    '''This function is used to generate the top10**.txt files as requested'''
    
    if nfile.find('state') != -1:
        op_header = ('TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE')
    elif nfile.find('occupation') != -1:
        op_header = ('TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE')
    
    with open(nfile,'w') as op_file:
        print('%s;%s;%s' %op_header,file=op_file)
        for item in sorted_list:
            print('%s;%i;%0.1f%%' %(item[0],item[1],item[1]*100/total),file=op_file)
    op_file.close()

