import urllib2
import json

def htflag(run,year): 

# returns HT flag if available else -1
    
    print  'run number %s' %run

    url = 'http://cmsdaqfff/prod/sc/php/is_ht_on.php?run=%s&setup=cdaq%s&multirun' %(run,year)
    print url

    line = json.load( urllib2.urlopen(url ))
    try:
        answer =  line['answer']['value']
        return (answer)
    except TypeError:
        print 'HT flag not available for run %i and year' %(run,year)
        return (-1) 
    

        
