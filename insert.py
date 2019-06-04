import json
import sys
malware_dict = {"string" : sys.argv[1]}
db = open('database.json', 'r')
malware_records = json.loads(db.read())
db.close()
f = open('database.json', 'w+')
malware_records.append(malware_dict)
f.write(json.dumps(malware_records))
f.close()
