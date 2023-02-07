#!/usr/bin/python3

import cgi
import pymysql
import MeCab
from jlv_cando import *
print("Content-type: text/html;charset=utf-8\n\n")


form = cgi.FieldStorage()
level_name = form["levelName"].value
topic_name = form["topicName"].value
exa_sentence = form["exa_sentence"].value
voca = form["voca"].value

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
print('<p class="lead">선택한 문장 : '+ exa_sentence +'</p>')
print('<br><br>')

mecab = MeCab.Tagger()
par = mecab.parseToNode(exa_sentence)
par = par.next
while par:
	#print(par.surface, par.feature.split(',')[0], "<BR>")
	par = par.next


연결 = pymysql.connect(host="127.0.0.1", user="jlv", password="1@23q~", db="jlvdb", charset="utf8")
cur = 연결.cursor()

sql = "SELECT * FROM Corpus where corpus_text like binary '%"+voca+"%'"
cur.execute(sql)
rows = cur.fetchall()

corpus_text = []

if not rows:
	print("<p class=\"lead\">검색 결과가 없습니다. 다른 단어로 검색해 주세요</p>")
	print("<p class=\"lead\">検索結果がありません。他の単語で検索してください。</p>")
else:
	print("<p class=\"lead\">선택한 문장과 유사한 문장은 아래와 같습니다. </p>")
	print("<p class=\"lead\">選択した文章と似ている文章は下記の通りです。</p><br><br>")
	print('<table class="jlv_table">')

	count = 0
	for row in rows:
		corpus_text.append(row[0])		
		count+=1
	genetic_main(exa_sentence, corpus_text)
	print('</table>')

print('</div>')
print('</div>')
print('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>')
print('<script src="js/scripts.js"></script>')

print('</body>')
print('</html>')

연결.close()
print()


