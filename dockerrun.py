#!/usr/bin/python3
print("content-type: text/html")
print()
import subprocess as sp
import cgi
form = cgi.FieldStorage()
osname = form.getvalue("x")
#osname = input("enter ur OS name: ")
cmd = docker run -d -it --name {} ubuntu:14.04.format(osname)
output = sp.getstatusoutput(cmd)
status = output[0]
result = output[1]
if status == 0:
    print("OS launched {}".format(osname))
else:
    print("error {}".format(result))