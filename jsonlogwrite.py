#encoding:UTF-8

try:
    import simplejson as json
except ImportError:
    import json


def Write(data, logfile):
    logfile = logfile + '.log'
    data['Window Text'] = data['Window Text'].encode('string_escape')
    data['Application Name'] = data['Application Name'].encode('string_escape')
    data['Application Window Name'] = data['Application Window Name'].encode('string_escape')
    text = json.dumps(data, sort_keys=True, indent='    ') #pretty
    # text = json.dumps(data, separators=(',', ':')) #compact
    print (text)
    f = open(logfile, 'a', )
    f.write(text + "\n")
    f.close()