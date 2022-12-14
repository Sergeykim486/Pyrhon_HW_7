import json, csv

def openjsonfile(fname):
    f = open(fname, 'r')
    file = json.loads(f.read())
    f.close()
    res = file
    return res

def opencsvfile(fname):
    f = open(fname, 'r')
    res = []
    freader = csv.reader(f, delimiter = ',')
    for row in freader:
        res.append({'id': row[0], 'f_name': row[1], 'l_name': row[2], 'phone': row[3]})
    return res
