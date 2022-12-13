#!/usr/bin/python3

import cgi
import pymysql

print("Content-type: text/html;charset=utf-8\n\n")

print('<html>')
print('<head>')
print('<link rel="stylesheet" href="./css/main.css">')
print('</head>')
print('<body>')
print('<div id = "box">')
print('<t1>일본어 수준별 텍스트 생성</t1>')
print('<br>')
print('<t1>日本語レベル別テキスト生成</t1>')
print('<br><br>')
print('<t2>토픽을 선택해 주세요</t2>')
print('<br>')
print('<t2>トピックを選択してください。</t2>')
print('<br><br>')

연결 = pymysql.connect(host="127.0.0.1", user="jlv", password="1@23q~", db="jlvdb", charset="utf8")
cur = 연결.cursor()

form = cgi.FieldStorage()
sql = "SELECT t.topic_id, t.topic_name FROM Topic as t Inner Join LevelTopic as lt On t.topic_id = lt.topic_id Where lt.level_id = '"+form["levelid"].value+"';"
cur.execute(sql)

rows = cur.fetchall()

print('<table>')
print('<form action="./input.py" method="post">')
print('<tr>')
count = 0
for row in rows:
    print('<td><button type="submit" name="topicid" value="'+row[0]+'">'+row[1]+'</button></td>')
    
    if count % 2 == 1 :
        print('</tr>')
        print('<tr>')
        
    count+=1

print('</tr>')
print('</form>')
print('</table>')

print('</div>')

print('</body>')
print('</html>')

연결.close()

print()


