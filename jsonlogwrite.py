#encoding:UTF-8

#@change: for above see http://www.python.org/dev/peps/pep-0263/
#@change: switch to using simplejson when available attempting to remove erros
try: import simplejson as json
except ImportError: import json

from time import localtime, time, strftime
import uuid
def Write(data, logfile):
        logfile = logfile + '.log'
        data['Timestamp'] = int(time())
        data['GUID'] = str(uuid.uuid4())
        data['date_time_stamp'] = strftime("%d %b %Y - %H:%M:%S")
        data['ActiveText'] = data['ActiveText'].encode('string_escape')
        #add more data to make it freindly to Drupal date module
        text = json.dumps(data, separators=(',',':')) #compact
        print (text)
        f = open(logfile, 'a', )
        f.write (text + "\n")
        f.close()