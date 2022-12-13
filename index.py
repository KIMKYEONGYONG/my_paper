#!/usr/bin/python3

import    cgi
import    pymysql

#print("Content-type: text/plain;charset=utf-8\n\n")
print("Content-type: text/html;charset=utf-8\n\n")

연결 = pymysql.connect(host="127.0.0.1", user="jlv", password="1@23q~", db="jlvdb", charset="utf8")

cur  = 연결.cursor()
cur.execute("SELECT * FROM Level;")


rows = cur.fetchall()

print('<table>')

for 행 in rows :
	print('<tr>')
	print('<td>', 행, '</td>')
	print('</tr>')

print('</table>')

연결.close()

print()