#!/usr/bin/python3

import cgi
import pymysql
import MeCab
print("Content-type: text/html;charset=utf-8\n\n")


form = cgi.FieldStorage()
level_name = form["levelName"].value
topic_name = form["topicName"].value
exa_sentence = form["exa_sentence"].value
voca = form["voca"].value

print('<html>')
print('<head>')
print('<link rel="stylesheet" href="./css/main.css">')
print('</head>')
print('<body id="body_result">')
print('<div id = "box_result">')
print('<t1>일본어 수준별 텍스트 생성('+level_name+', '+topic_name+')</t1>')
print('<br>')
print('<t1>日本語レベル別テキスト生成('+level_name+', '+topic_name+')</t1>')
print('<br><br>')
print('<t2>선택한 문장 : '+ exa_sentence +'</t2>')
print('<br><br>')

mecab = MeCab.Tagger()
par = mecab.parseToNode(exa_sentence)
par = par.next
while par:
	#print(par.surface, par.feature.split(',')[0], "<BR>")
	par = par.next


연결 = pymysql.connect(host="127.0.0.1", user="jlv", password="1@23q~", db="jlvdb", charset="utf8")
cur = 연결.cursor()

sql = "SELECT * FROM Corpus where corpus_text like '%"+voca+"%'"
cur.execute(sql)
rows = cur.fetchall()
if not rows:
	print("검색 결과가 없습니다. 다른 단어로 검색해 주세요 <br>")
	print("検索結果がありません。他の単語で検索してください。<br>")
else:
	print('<br>')
	print('<br><br>')
	print("선택한 문장과 유사한 문장은 아래와 같습니다. <br>")
	print("選択した文章と似ている文章は下記の通りです。<br><br>")
	print('<table>')

	count = 0
	for row in rows:
		print('<tr>')
		print('<td>'+row[0]+'</td>')
		print('</tr>')
		print('<tr><td><br></td></tr>')
			
		count+=1

	print('</tr>')
	print('</table>')

print('</div>')

print('</body>')
print('</html>')

연결.close()
print()


