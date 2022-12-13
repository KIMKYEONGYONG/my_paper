#!/usr/bin/python3

import    cgi

print("Content-type: text/plain;charset=utf-8\n\n")

import MeCab 
mecab = MeCab.Tagger() 

def pos_tagging(text):
	result = mecab.parseToNode(text)
	result = result.next
	result_list = ""
	while result:
		result_list += result.feature.split(",")[0] + ","
		# print (result.surface, result.feature.split(",")[0])
		result = result.next

	result_list = result_list[:-9]
	return result_list

#rint(pos_tagging("私はキムです。"))
#print(pos_tagging("机があります。"))


jlv_text = "私はキムです。"
def sent(_ref):
	sent  = []
	sent.append(pos_tagging(jlv_text))
	sent.append(pos_tagging(_ref))
	return sent
#sent5 = sent("私はキムです。", "私はワンです。")

from sklearn.feature_extraction.text import TfidfVectorizer
def tfid_matrix(text):
	tfid = TfidfVectorizer()
	tfid_matrix = tfid.fit_transform(text)
	idf = tfid.idf_
	print(dict(zip(tfid.get_feature_names_out(), idf)))
	return tfid_matrix

from sklearn.metrics.pairwise import cosine_similarity

def result_print(tfid_matrix):
	result = cosine_similarity(tfid_matrix[0:1], tfid_matrix[1:2]) [0][0] * 100
	#print(result)
	return int(result)

# 선택 연산
import random
def select_Roulette(적합도, 현재적합도):
	
	# 배열에 넣어서 하는 방법 TODO. 더 좋은 방법 생각해보기
	# 후보의 적합도만큼의 수를 배열에 넣어서 룰렛의 데이터로 활용
	input_roulette = []
	for i in range(len(적합도)):
		for j in range(적합도[i]):
			#print(j)
			input_roulette.append(i)

	result = []
	while(len(result) < len(적합도)):
		# 후보가 1개만 선택되게끔 중복체크
		# TODO. 원래는 선택연산으로 중복이 가능하다. 지금 단계에서는 그 고려를 생략 
		my_ran = random.randrange(0,현재적합도-1)
		#print(input_roulette[my_ran])
		#print(result)
		if input_roulette[my_ran] not in result:
			result.append(input_roulette[my_ran])
	
	#print(result)
	return result

# 교차연산
def my_cross(roulette):

	# TODO 본래는 이진화된 상태로 교차연산이 진행되지만, 임시로 품사 배열로 교차연산 진행한다

	pass


def genetic_main():
	
	'''
	sent1, sent2, sent3, sent4
	'''
	# 현재 후보 , 본래는 생성한 문장을 append 할 예정
	#corpus_text = ["私の趣味はテニスです。","私は映画を見ることが好きです。","私は学校に行きます。","私はワンではありません。"]
	
	corpus_text = ["私は韓国人です。","私は学校に行きます。","私の家族は3人です。","私はご飯を食べます。"]


	# 적합도 계산을 위한 비교군 생성
	corpus_sent = []
	for i in range(len(corpus_text)):
		print(corpus_text[i])
		corpus_sent.append(sent(corpus_text[i]))
	
	# 벡터화 
	corpus_sent_tfid_matrix = []
	for i in range(len(corpus_sent)):
		print(corpus_sent[i])
		corpus_sent_tfid_matrix.append(tfid_matrix(corpus_sent[i]))
	

	현재적합도 = 0
	이전적합도 = 0
	현재적합도평균 = 0.0
	적합도 = []

	# 적합도 확인
	for i in range(len(corpus_sent_tfid_matrix)):
		result = result_print(corpus_sent_tfid_matrix[i])
		적합도.append(result)
		현재적합도 += int(result)

	print(적합도)
	
	select_Roulette(적합도, 현재적합도)
			
	'''
	int 현재적합도 = 0
	int 이전적합도 = 0
	float 현재적합도평균 = 0.0f
	적합도= []
	for i in len(sent_vector):
		result = targetFunction(sent_vector[0]);
		적합도.append(result);
		현재적합도 += result;
	}
	'''

genetic_main()









'''
def text_to_binary(text):
	# ' '.join(format(ord(x), 'b') for x in str
	return ' '.join(format(x,'08b') for x in bytearray(text,'utf-8'))  

def binaryToText(bin_data):
	#return "".join([chr(int(binary, 2)) for binary in bin_data.split(" ")]).decode('utf-8', 'ignore')
	return bin_data.encode('utf-8').decode('utf-8')

print(text_to_binary(jlv_text))
#bin_data ='10001111100101110010111010111110011'
print(binaryToText(text_to_binary(jlv_text)))
'''