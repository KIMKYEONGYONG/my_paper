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
level_name = row[0][0]
topic_name = row[0][1]
print('<h1>일본어 수준별 텍스트 생성('+level_name+', '+topic_name+')</h1>')
print('<h1>日本語レベル別テキスト生成('+level_name+', '+topic_name+')</h1>')
print('<br>')
print('<form action="./jlv_result.py" method="post">')
print('<input type="hidden" name="levelId" value="'+level_id+'">')
print('<input type="hidden" name="topicId" value="'+topic_id+'">')
print('<input type="hidden" name="levelName" value="'+level_name+'">')
print('<input type="hidden" name="topicName" value="'+topic_name+'">')
print('<p class="lead">예문에 넣을 단어를 입력해주세요. <br>공백은 일본어 수준별 코퍼스의 단어에서 무작위로 선택됩니다. </p>')
print('<p class="lead">例文に入力する単語を入力してください。<br>空白は日本語レベルコーパスからランダムで選ばれます。</p>')
print('<input type="text" class="input_text" name="inputText">')
print('<button type="submit" class="search_button">검색</button></td> <br>')
print('<p class="lead">*동사와 형용사의 경우 語幹으로 입력해주세요. <br> 예시: 書く ➡ 書...<br>')
print('*語幹으로 검색되기 때문에 의도하지 않은 예문이 검색될 수 있습니다. <p>')
print('</form>')


print('</div>')
print('</div>')
print('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>')
print('<script src="js/scripts.js"></script>')

print('</body>')
print('</html>')

연결.close()

print()


