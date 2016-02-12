import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))

from funny.tools.mysql import getDB

db = getDB()

sql = 'select id,image where image != ""  limit 10'

rows = db.query_dict(sql)()

for r in rows:
    print r


