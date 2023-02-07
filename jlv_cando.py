#!/usr/bin/python3

#import    cgi

#print("Content-type: text/html;charset=utf-8\n\n")

import MeCab 
import random
import math
import numpy as np
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


def sent(jlv_text, _ref):
	sent  = []
	sent.append(pos_tagging(jlv_text))
	sent.append(pos_tagging(_ref))
	return sent

def result_print(tfid_matrix):

	arr1  = tfid_matrix[0].split(",")
	arr2  = tfid_matrix[1].split(",")  

	# 조동사를 기준으로 대명사와의 매칭기준
	pnv = pos_pnv_m(arr1, arr2)

	# 조동사를 기준으로 명사와의 매칭기준
	nv = pos_nv_m(arr1, arr2)
 
	# 명사와 명사와의 매칭
	n = pos_n_m(arr1, arr2)
	# 그외 품사 매칭

	nn = wc_nn_m(arr1, arr2)

	return int((pnv + nv + n + nn) * 100)

# 조동사를 기준으로 대명사와의 매칭기준
def pos_pnv_m(arr1, arr2, w1 = 0.5):
	v = '助動詞'
	pron = '代名詞'

	# 조동사가 없으면 0
	if (v not in arr1 ) or (v not in arr2):
		return 0

	# 대명사가 없으면 w1
	if (pron not in arr1 ) or (pron not in arr2 ):
		return w1
	
	# 조동사의 위치
	v1 = arr1.index(v)
	v2 = arr2.index(v)

	# 대명사의 위치
	pron1 = arr1.index(pron)
	pron2 = arr2.index(pron)
 
	# 조동사 기준 대명사와의 매칭기준
	pos1 = abs(v1 - pron1)
	pos2 = abs(v2 - pron2)
 
	result = 0 
	if pos1 == pos2:
		result = 1
	elif pos1 > pos2:
		result = pos2 / pos1
	else :
		result = pos1 / pos2

	return w1 * result
 
# 조동사를 기준으로 명사와의 매칭기준
def pos_nv_m(arr1, arr2, w2 = 0.3):
	v = '助動詞'
	n = '名詞'

	# 조동사가 없으면 0
	if (v not in arr1 ) or (v not in arr2):
		return 0

	# 명사가 없으면 w2
	if (n not in arr1 ) or (n not in arr2 ):
		return w2

	# 조동사의 위치
	v1 = arr1.index(v)
	v2 = arr2.index(v)

	# 명사의 위치
	n1 = arr1.index(n)
	n2 = arr2.index(n)
 
	# 조동사 기준 명사와의 매칭기준
	pos1 = abs(v1 - n1)
	pos2 = abs(v2 - n2)

	result = 0 
	if pos1 == pos2:
		result = 1
	elif pos1 > pos2:
		result = pos2 / pos1
	else :
		result = pos1 / pos2

	return w2 * result

# 명사와 명사와의 매칭
def pos_n_m(arr1, arr2, w3 = 0.1):
	n = '名詞'

	if (n not in arr1 ) or (n not in arr2 ):
		return w3
	
	n1 = [i for i in range(len(arr1)) if arr1[i]==n]
	n2 = [i for i in range(len(arr2)) if arr2[i]==n]

	result = 0
	if n1 == n2:
		result = 1
	elif len(n1) > len(n2):
		result = myPoint(n2, n1, arr1, arr2)
	elif len(n2) > len(n1):
		result = myPoint(n1, n2, arr1, arr2)
	return w3 * result


# 명사를 제외한 그 외의 품사 매칭
def wc_nn_m(arr1, arr2, w4 = 0.1):
	n = '名詞'

	n1 = [i for i in range(len(arr1)) if arr1[i]!=n]
	n2 = [i for i in range(len(arr2)) if arr2[i]!=n]

	result = 0
	if n1 == n2:
		result = 1
	elif len(n1) > len(n2):
		result = myPoint(n2, n1, arr1, arr2)
	elif len(n2) > len(n1):
		result = myPoint(n1, n2, arr1, arr2)
	return w4 * result


def myPoint(n_1, n_2, arr_1, arr_2):
		point = 0
		for i in n_1:
			if i in n_2 and arr_1[i] == arr_2[i]:
				point += 1
		return point / len(n_2)

def genetic_main(jlv_text, corpus_text):
	
	# 처음 유전 알고리즘을 수행할 후보 n개 배열 
	random_size = 4
	corpus_random_text = []
	현재후보 = []
	if(len(corpus_text) >= random_size):
		while(len(corpus_random_text) < random_size):
			# 후보가 1개만 선택되게끔 중복체크
			my_ran = random.randrange(0,len(corpus_text)-1)
			if corpus_text[my_ran] not in corpus_random_text:
				corpus_random_text.append(corpus_text[my_ran])
				현재후보.append(my_ran)
	else:
		corpus_random_text = corpus_text

	# 적합도 계산을 위한 비교군 생성
	corpus_sent = [sent(jlv_text, corpus_random_text[i]) for i in range(len(corpus_random_text))]
	
	현재적합도 = 0
	이전적합도 = 0
	현재적합도평균 = 0.0
	적합도 = []
	# 적합도 확인
	for i in range(len(corpus_sent)):
		result = result_print(corpus_sent[i])
		적합도.append(result)
		현재적합도 += int(result)

	# 선택 연산
	roulte_result = select_Roulette(적합도, 현재적합도, 현재후보)

	최적후보 = 현재후보
	최적적합도 = 현재적합도
	traning_count = 500000
	_count  = 0
	for _ in range(traning_count):
		이전적합도 = 현재적합도
		
		# 교차 연산
		cross_result = my_crossover(roulte_result)
		# 돌연변이 연산
		mutation_result = myMutation(cross_result)
		# 현재후보 / 2진수를 다시 10진수로
		현재후보 = [ int(j , 2) for j in mutation_result ]
		# 연산 중 검색대상 코퍼스의 길이보다 큰 숫자가 있을 경우
		for j in range(len(현재후보)):
			if 현재후보[j] >= len(corpus_text):
				현재후보[j] = np.random.randint(0, len(corpus_text)) 
		result_sum = 0
		적합도 = []


		# 적합도 계산을 위한 비교군 생성
		temp_text = [corpus_text[j] for j in 현재후보]
		corpus_sent = [sent(jlv_text, temp_text[j]) for j in range(len(temp_text))]
		for j in range(len(corpus_sent)):
			result = result_print(corpus_sent[j])
			적합도.append(result)
			result_sum += int(result)
		현재적합도 = result_sum

		if 현재적합도 > 최적적합도:
			최적후보 = 현재후보
			최적적합도 = 현재적합도
			_count = 0

		if 현재적합도 < 이전적합도:
			_count += 1

		if _count > math.sqrt(traning_count):
			break

		roulte_result = select_Roulette(적합도, 현재적합도, 현재후보)

	result_text = [corpus_text[i] for i in 최적후보]
	corpus_sent = [sent(jlv_text, result_text[i]) for i in range(len(result_text))]	
	적합도 = []
	for i in range(len(corpus_sent)):
		result = result_print(corpus_sent[i])
		적합도.append(result)
	
	적합도_sorted_index = np.argsort(적합도)[::-1]
	
	print("<tr class='jlv_th'>")
	print("<td class='jlv_td'> 텍스트 생성 결과 </td>")
	print("<td class='jlv_td'> 유사도 </td>")
	print("</tr>")
	print("<tr class='jlv_th'>")
	for i in 적합도_sorted_index:
		print("<td class='jlv_td'>", result_text[i],  "</td>")
		print("<td class='jlv_td'>", str(적합도[i]), " %</td>")
		print("</tr><tr class='jlv_th'>")
	print("</tr>")



# 선택 연산
def select_Roulette(적합도, 현재적합도, texts):
	

	# 후보의 적합도만큼의 수를 배열에 넣어서 룰렛의 데이터로 활용
	# parents = [texts[rand(0, len(texts))] for i in range(2)]
	roulette_array = []
	for i in range(len(적합도)):
		for j in range(적합도[i]):
			roulette_array.append(i)
	
	# 위의 룰렛데이터가 정렬되어 있으므로 셔플
	random.shuffle(roulette_array)
	
	# 룰렛데이터 중 랜덤으로 선택하여 문장 번호를 랜덤으로 4개 선택한다 ( 중복 가능)
	result = [texts[roulette_array[int(random.uniform(0, len(roulette_array)))]] for i in range(4)]
	
	# 같은 숫자 교차하는 경우 방지하기 위함
	# result[0] == result[1] -> result[1]  + 1 , result[2] == result[3] -> result[3]  + 1
	if result[0] == result[1]:
		result[1] += 2
	if result[2] == result[3]:
		result[3] += 3
	return result

# 교차연산
def my_crossover(roulette):
	binary_roulette = []
	for i in roulette:
		binary_roulette.append(format(i, 'b'))
	 
	# index 0 lenght != index 1 lenght /  index 2 lenght != index 3 lenght 일 경우 앞에 0을 채운다.
	if len(binary_roulette[0]) != len(binary_roulette[1]):
		if len(binary_roulette[0]) > len(binary_roulette[1]) :
			binary_roulette[1] = binary_roulette[1].zfill(len(binary_roulette[0]))
		else:
			binary_roulette[0] = binary_roulette[0].zfill(len(binary_roulette[1]))
	if len(binary_roulette[2]) != len(binary_roulette[3]):
		if len(binary_roulette[2]) > len(binary_roulette[3]) :
			binary_roulette[3] = binary_roulette[3].zfill(len(binary_roulette[2]))
		else:
			binary_roulette[2] = binary_roulette[2].zfill(len(binary_roulette[3]))
	
	# 교차결과 배열
	cross_result = []

	# 교차지점 
	if len(binary_roulette[0]) > 1 :
		crossover_point1 = np.random.randint(1, len(binary_roulette[0]))
		# 부모 유전자 교차
		cross_result.append(binary_roulette[0][:crossover_point1]+binary_roulette[1][crossover_point1:])
		cross_result.append(binary_roulette[1][:crossover_point1]+binary_roulette[0][crossover_point1:])
	else:
		cross_result.append(binary_roulette[1])
		cross_result.append(binary_roulette[0])
	if len(binary_roulette[2]) > 1 :
		crossover_point2 = np.random.randint(1, len(binary_roulette[2]))
		cross_result.append(binary_roulette[2][:crossover_point2]+binary_roulette[3][crossover_point2:])
		cross_result.append(binary_roulette[3][:crossover_point2]+binary_roulette[2][crossover_point2:])
	else:
		cross_result.append(binary_roulette[3])
		cross_result.append(binary_roulette[2])

	return cross_result

# 돌연변이연산
def myMutation(cross_result):
    
	mutation_result= []

	# 0.25의 확률로 발생한다.
	my_rand = np.random.randint(0, 4)
	if my_rand == 1:
		# 돌연변이 연산을 시킬 후보
		cross_rand = np.random.randint(0, len(cross_result))
		# 돌연변이 연산 시킬 위치
		point_rand = np.random.randint(0, len(cross_result[cross_rand]))
		if cross_result[cross_rand][point_rand] == '0':
			temp = list(cross_result[cross_rand])
			temp[point_rand] = '1'
			cross_result[cross_rand] = ''.join(temp)
		else:
			temp = list(cross_result[cross_rand])
			temp[point_rand] = '0'
			cross_result[cross_rand] = ''.join(temp)
		mutation_result = cross_result
	else :
		mutation_result = cross_result

	return mutation_result

