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

sql = 'select id,images from joke where images != "" '

rows = db.query_dict(sql)()

from lxml import etree

images = []
for r in rows:
    images.append(r)

update = 'update joke set images = %s where id = %s'

for r in images:
    if r['images'].index('http') == 0:
        continue
    attrs = etree.HTML(r['images'])
    src = "".join([i.get('src') if i.get('src') else '' for i in attrs.xpath('//img')])
    if not src:
        src = "".join([i.get('tsrc') if i.get('tsrc') else '' for i in attrs.xpath('//img')])
    if not src:
        src = "".join([i.get('_src') if i.get('_src') else '' for i in attrs.xpath('//img')])
    if not src:
        print 'error\n %s' % r['id'],attrs.xpath('//img'),r['images']
        continue
    db.update(update,src,r['id'])

