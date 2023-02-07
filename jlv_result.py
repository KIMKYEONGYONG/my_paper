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
print('<meta charset="utf-8" />')
print('<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />')
print('<meta name="description" content="" />')
print('<meta name="author" content="" />')
print('<title>JLVG-CANDO 수준별 일본어 텍스트 자동생성 시스템</title>')
print('<link rel="icon" type="image/x-icon" href="assets/favicon.ico" />')
print('<link href="css/styles.css" rel="stylesheet" />')
print('</head>')
print('<body>')
print('<nav class="navbar navbar-expand-lg navbar-dark bg-dark">')
print('<div class="container">')
print('<a class="navbar-brand" href="https://jbit.bufs.ac.kr/~rlaruddyd1/jlv/">Start JLVG-CANDO</a>')
print('<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>')
print('<div class="collapse navbar-collapse" id="navbarSupportedContent">')
print('<ul class="navbar-nav ms-auto mb-2 mb-lg-0">')
print('<li class="nav-item"><a class="nav-link active" aria-current="page" href="https://jbit.bufs.ac.kr/~rlaruddyd1/jlv/">Home</a></li>')
print('</ul>')
print('</div>')
print('</div>')
print('</nav>')
print('<div class="container">')
print('<div class="text-center mt-5">')
print('<h1>일본어 수준별 텍스트 생성('+level_name+', '+topic_name+')</h1>')
print('<h1>日本語レベル別テキスト生成('+level_name+', '+topic_name+')</h1>')
print('<br>')
print('<p class="lead">입력한 단어: '+search_text+'</p>')
print('<p class="lead">入力した単語: '+search_text+'</p>')
print('<br><br>')
 


sql = "SELECT sentence FROM ExaSe where sentence like binary '%"+search_text+"%'"
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
	print("<p class=\"lead\">검색 결과가 없습니다. 다른 단어로 검색해 주세요</p>")
	print("<p class=\"lead\">検索結果がありません。他の単語で検索してください。</p>")
else:
	print('<p class="lead">基準になる例文を選択してください。</p>')
	print('<p class="lead">기준이 되는 문장을 선택해 주세요</p>')
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
print('</div>')
print('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>')
print('<script src="js/scripts.js"></script>')

print('</body>')
print('</html>')

연결.close()
print()


