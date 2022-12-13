#!/usr/bin/python3

import cgi
import pymysql

print("Content-type: text/html;charset=utf-8\n\n")

연결 = pymysql.connect(host="127.0.0.1", user="jlv", password="1@23q~", db="jlvdb", charset="utf8")
cur = 연결.cursor()

form = cgi.FieldStorage()

level_id = form["levelId"].value
topic_id = form["topicId"].value


sql = "SELECT l.level_name, t.topic_name FROM Topic as t, Level as l Where l.level_id = '"+level_id+"' and t.topic_id='"+topic_id+"';"
cur.execute(sql)

row = cur.fetchall()

print('<html>')
print('<head>')
print('<link rel="stylesheet" href="./css/main.css">')
print('</head>')
print('<body>')
print('<div id = "box">')
level_name = row[0][0]
topic_name = row[0][1]
print('<t1>일본어 수준별 텍스트 생성('+level_name+', '+topic_name+')</t1>')
print('<br>')
print('<t1>日本語レベル別テキスト生成('+level_name+', '+topic_name+')</t1>')
print('<br><br>')
print('<form action="./jlv_result.py" method="post">')
print('<input type="hidden" name="levelId" value="'+level_id+'">')
print('<input type="hidden" name="topicId" value="'+topic_id+'">')
print('<input type="hidden" name="levelName" value="'+level_name+'">')
print('<input type="hidden" name="topicName" value="'+topic_name+'">')
print('예문에 넣을 단어를 입력해주세요. <br>공백은 일본어 수준별 코퍼스의 단어에서 무작위로 선택됩니다. <br>')
print('例文に入力する単語を入力してください。<br>空白は日本語レベルコーパスからランダムで選ばれます。<br>')
print('<input type="text" class="input_text" name="inputText">')
print('<button type="submit" class="search_button">검색</button></td> <br>')
print('*동사와 형용사의 경우 語幹으로 입력해주세요. <br> 예시: 書く ➡ 書...<br>')
print('*語幹으로 검색되기 때문에 의도하지 않은 예문이 검색될 수 있습니다. <br>')
print('</form>')


print('</div>')

print('</body>')
print('</html>')

연결.close()

print()


