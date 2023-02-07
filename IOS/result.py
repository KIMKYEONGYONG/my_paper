#!/usr/bin/python3

import sys
import cgi
import pymysql
import MeCab
from jlv_cando import *


def call(exa_sentence, voca):

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
		pass#!/usr/bin/python3

import sys
import cgi
import pymysql
import MeCab
from jlv_cando import *


def call(exa_sentence, voca):

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
		print("hell;")
	else:
		count = 0
		for row in rows:
			corpus_text.append(row[0])		
			count+=1
		genetic_main(exa_sentence, corpus_text)

call(sys.argv[1], sys.argv[2])