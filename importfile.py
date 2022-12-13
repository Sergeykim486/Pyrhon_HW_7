import json, csv

def openjsonfile(fname):
    f = open(fname, 'r')
    file = json.loads(f.read())
    f.close()
    res = file['response']['item']
    return res

# def opencsvfile(fname):
#     f = open(fname, 'r')
#     res = []
#     reader = csv.reader(f, delimiter=',')
#     for item in reader:
#         res.append({'id': item[0], 'f_name': item[1], 'l_name': item[2], 'phone': item[3]})
#     return res

def savecsvfile(fname):
    f = open(fname, 'w')
    res = []
    reader = csv.reader(f, delimiter=',')
    for item in reader:
        res.append({'id': item[0], 'f_name': item[1], 'l_name': item[2], 'phone': item[3]})
    return res

f = openjsonfile('Phones.json')
for i in f:
    for j in i:
        print(str(i[j]), end= ' ')
    print()