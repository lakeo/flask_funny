import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))

import SimpleDB
def getDB():
    return SimpleDB.MySQLdb(
                host='localhost',
                port = 3306,
                user='joke',
                passwd='joke',
                db ='joke',
                use_unicode=True,
                charset='utf8')

db = getDB()

sql = 'select id,images from joke where images != ""  limit 10'

rows = db.query_dict(sql)()

for r in rows:
    print r


