import os
import sys
import json

db = open('database.json', 'r')
malware_records = json.loads(db.read())
replacement = """"""

logs = open("cleanup.log","w")
for dname, dirs, files in os.walk(sys.argv[1]):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath) as f:
            s = f.read()
        length_of_original = len(s)
        for record in malware_records:
            s = s.replace(record['string'], replacement)
        if len(s) != length_of_original :
            logs.write("Cleaning " + fname + " in " + dname)
        with open(fpath, "w") as f:
            f.write(s)
