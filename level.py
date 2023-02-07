#!/usr/bin/python3

import cgi
import pymysql

print("Content-type: text/html;charset=utf-8\n\n")

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
print('<div class="container mybackgroundImage">')
print('<div class="text-center mt-5">')
print('<h1>일본어 수준별 텍스트 생성 시스템</h1>')
print('<h1>日本語レベル別テキスト生成</h1>')
print('<div class="text-center mt-5">')
print('<p class="lead">레벨을 선택해 주세요</p>')
print('<p class="lead">レベルを選択してください。</p>')

연결 = pymysql.connect(host="127.0.0.1", user="jlv", password="1@23q~", db="jlvdb", charset="utf8")
cur = 연결.cursor()
cur.execute("SELECT * FROM Level;")

rows = cur.fetchall()


print('<table>')
print('<tr>')
count = 0
print('<form action="./topic.py" method="post">')
for row in rows:
	print('<td><button type="submit" class="level_button" name="levelId" value="'+row[0]+'">'+row[1]+'</button></td>')
    
	if count % 2 == 1 :
		print('</tr>')
		print('<tr>')
        
	count+=1

print('</tr>')
print('</form>')
print('</div>')

print('</table>')
print('</div>')
'''
print('<div class="text-center mt-5 padding_right">')
print('<img class="fit-picture" src="./img/레벨 표.png">')
print('<p>일본어 A1~ A2 = 초급 , 일본어 B1-1 ~ B2-2 = 중급 </p>')
print('</div>')
'''
print('</div>')
print('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>')
print('<script src="js/scripts.js"></script>')
print('</body>')
print('</html>')

연결.close()

print()


