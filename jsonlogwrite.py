#encoding:UTF-8

#@change: for above see http://www.python.org/dev/peps/pep-0263/
#@change: switch to using simplejson when available attempting to remove erros
try: import simplejson as json
except ImportError: import json

from time import localtime, time
def Write(data, logfile):
        logfile = logfile + '.json'
        data['Timestamp'] = int(time())
        #text = json.dumps(data) #normal
        #text = json.dumps(data, sort_keys=True, indent=2) #nicely formated
        text = json.dumps(data, separators=(',',':')) #compact
        f = open(logfile, 'a', )
        f.write (text + "\n")
        f.close()