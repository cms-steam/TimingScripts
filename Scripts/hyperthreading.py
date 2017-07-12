import urllib2
import argparse
import json

parser = argparse.ArgumentParser(description='input run numbers and year')
parser.add_argument('runs', type = int, nargs='+')
parser.add_argument('year', type = int, nargs=1)

args = parser.parse_args()
print  'run list %s' %args.runs
print  'year %s' %args.year[0]

for run in args.runs:
    url = 'http://cmsdaqfff/prod/sc/php/is_ht_on.php?run=%s&setup=cdaq%d&multirun' %(run,args.year[0])

    
    line = json.load( urllib2.urlopen(url ))
    
    try:
        ans =  line['answer']['value']
        if ans == 0:
            print 'run %i not available' %run
        elif ans ==1:
            print 'run %i HT OFF' %run
        elif ans == 2:
            print 'run %i HT MIXED' %run
        elif ans == 3:
            print 'run %i HT ON' %run
        elif ans == 4:
            print 'run %i core count out of range' %run

        break
    except TypeError:
        print 'HT flag not available for run %i and year' %(run,year)
        ans = -1
        break



#  0 - not available
#  1 - HT off
#  2 - mixed
#  3 - HT on
#  4 - error (core count out of range)

   
        
