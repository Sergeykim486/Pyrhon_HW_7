import json, csv

def openjsonfile(fname, data):
    f = open(fname, 'w')
    f.write(json.dumps(data, indent=2))
    f.close

def savecsvfile(fname, data):
    f = open(fname, 'w')
    writer = csv.writer(f, delimiter = ",", lineterminator="\r")
    for item in data:
        writer.writerow([item['id'], item['f_name'], item['l_name'], item['phone']])
    f.close()