'''
Name : Bhasha Dushara
Date : 27th july 2018
'''

import re
from collections import Counter

def apache_log_reader(logfile):
    myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    try :
        with open(logfile) as f:
            log = f.read()
            my_iplist = re.findall(myregex,log)
            ipcount = Counter(my_iplist)
            for k, v in ipcount.items():
                print("IP ADDRESS : {}".format(str(k)),end='\n')
                print("COUNTING : {}".format(str(v)))

    except IOError as e:
        print("ERROR : {}".format(e))


if __name__ == '__main__':
    apache_log_reader("access_log")