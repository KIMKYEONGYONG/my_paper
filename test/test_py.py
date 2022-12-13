#!/usr/bin/python3

import cgi
print("Content-type: text/html;charset=utf-8\n\n")
print("<head><meta charset='utf-8'> </head>")

result_list = [[] * 9]
print(result_list)
for i in range(2, 10):
	for j in range(1, 10):
		print(i*j)
		result_list[i-2].append(i* j)
		print(i)


print(result_list)