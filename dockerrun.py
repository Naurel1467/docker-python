#!/usr/bin/python3
#/var/lib/tomcat9/webapps/ROOT/WEB-INF/cgi  <------locatioon of cgi file in tomcat9
print("content-type: text/html")
print()
import subprocess as sp
import cgi
form = cgi.FieldStorage()
osname = form.getvalue("x")    
osimage = cgi.FieldStorage("i")             # 'x' is the input value from user
#osname = input("enter ur OS name: ")
#to call the value of 'x' from above 'osname' variable we need to use {} .format(osname)
cmd = "sudo docker run -d -it --name {} {} ".format(osname,osimage)    # 'x' is stored in osname and get called by cmd
output = sp.getstatusoutput(cmd)   #this function(subprocess alias sp) stores its output in variable called "output"
status = output[0]
result = output[1] 
if status == 0:
    print("OS launched {}".format(osname))
else:
    print("error {}".format(result))
