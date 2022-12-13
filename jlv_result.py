#!/usr/bin/python3

import cgi
import pymysql

print("Content-type: text/html;charset=utf-8\n\n")


form = cgi.FieldStorage()
level_name = form["levelName"].value
topic_name = form["topicName"].value
level_id = form["levelId"].value
topic_id = form["topicId"].value

연결 = pymysql.connect(host="127.0.0.1", user="jlv", password="1@23q~", db="jlvdb", charset="utf8")
cur = 연결.cursor()


if "inputText" in form:
	input_text = form["inputText"].value
	search_text = input_text
else:
	sql = "SELECT * FROM Voca Order by RAND() Limit 1;"
	cur.execute(sql)
	row = cur.fetchone()
	#input_text = row[2]
	search_text = row[3]

print('<html>')
print('<head>')
print('<link rel="stylesheet" href="./css/main.css">')
print('</head>')
print('<body>')
print('<div id = "box">')
print('<t1>일본어 수준별 텍스트 생성('+level_name+', '+topic_name+')</t1>')
print('<br>')
print('<t1>日本語レベル別テキスト生成('+level_name+', '+topic_name+')</t1>')
print('<br><br>')
print('<t2>입력한 단어: '+search_text+'</t2>')
print('<br>')
print('<t2>入力した単語: '+search_text+'</t2>')
print('<br><br>')
 


sql = "SELECT sentence FROM ExaSe where sentence like '%"+search_text+"%'"
if level_id == "L999" and topic_id == "T999":
	sql += " ;"
elif level_id == "L999":
	sql += " and topic_id = '"+topic_id+"';"
elif topic_id == "T999":
	sql += " and level_id = '"+level_id+"';"
else:
	sql += " and level_id = '"+level_id+"' and topic_id = '"+topic_id+"';"

cur.execute(sql)
rows = cur.fetchall()
if not rows:
	print("검색 결과가 없습니다. 다른 단어로 검색해 주세요 <br>")
	print("検索結果がありません。他の単語で検索してください。<br>")
else:
	print('<t2>基準になる例文を選択してください。</t2>')
	print('<br>')
	print('<t2>기준이 되는 문장을 선택해 주세요</t2>')
	print('<br><br>')
	print('<table>')
	print('<form action="./result.py" method="post">')
	print('<input type="hidden" name="levelName" value="'+level_name+'">')
	print('<input type="hidden" name="topicName" value="'+topic_name+'">')
	print('<input type="hidden" name="voca" value="'+search_text+'">')

	count = 0
	for row in rows:
		print('<tr>')
		print('<td><button type="submit" class="exa_button" name="exa_sentence" value="'+row[0]+'">'+row[0]+'</button></td>')
		print('</tr>')
			
		count+=1

	print('</tr>')
	print('</form>')
	print('</table>')

print('</div>')

print('</body>')
print('</html>')

연결.close()
print()


