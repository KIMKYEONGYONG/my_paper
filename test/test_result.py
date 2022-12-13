#!/usr/bin/python3

import    cgi

print("Content-type: text/html;charset=utf-8\n\n")
import os


폼 = cgi.FieldStorage()
context =  폼["id1"].value
print(context)

'''
os.system("python gpt2-generate-test.py --context='"+context +"'")

res = os.popen("python gpt2-generate-test.py --context='"+context +"'").read()
print("<td>"+res+"</td>")
'''
