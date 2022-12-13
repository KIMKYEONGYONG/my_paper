#!/usr/bin/python3

import cgi
import pymysql

print("Content-type: text/html;charset=utf-8\n\n")


form = cgi.FieldStorage()

연결 = pymysql.connect(host="127.0.0.1", user="jlv", password="1@23q~", db="jlvdb", charset="utf8")
cur = 연결.cursor()

level_id = form["levelId"].value
sql = "SELECT level_name FROM Level Where level_id = '"+level_id+"';"
cur.execute(sql)

row = cur.fetchone()
level_name = row[0]


print('<html>')
print('<head>')
print('<link rel="stylesheet" href="./css/main.css">')
print('</head>')
print('<body>')
print('<div id = "box">')
print('<t1>일본어 수준별 텍스트 생성('+level_name+')</t1>')
print('<br>')
print('<t1>日本語レベル別テキスト生成('+level_name+')</t1>')
print('<br><br>')
print('<t2>토픽을 선택해 주세요</t2>')
print('<br>')
print('<t2>トピックを選択してください。</t2>')
print('<br><br>')

sql = "SELECT t.topic_id, t.topic_name FROM Topic as t Inner Join LevelTopic as lt On t.topic_id = lt.topic_id Where lt.level_id = '"+level_id+"';"
cur.execute(sql)

rows = cur.fetchall()

print('<table>')
print('<form action="./input.py" method="post">')
print('<input type="hidden" name="levelId" value="'+level_id+'">')
print('<tr>')
count = 0
for row in rows:
    print('<td><button type="submit" class="topic_button" name="topicId" value="'+row[0]+'">'+row[1]+'</button></td>')
    
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


