#!/usr/bin/python2

import  cgi
import  commands

print "Content-type:text/html"
print ""

#  taking date from apache and storing into web variable 
web=cgi.FieldStorage()

# only want to access data in x 
store=web.getvalue('key')
#  running commands
if  store ==  'DATE' :
	print  "<pre>"
	print  commands.getoutput('date')
	print  "</pre>"

elif  store ==  'FTP' :
	print  "<pre>"
	print  commands.getoutput('sudo -i yum  install ftp -y')
	print  "</pre>"

elif  store ==  'RAM' :
	print  "<pre>"
        print  commands.getoutput('vmstat')
        print  "</pre>"

elif  store ==  'CAL' :
	print  "<pre>"
	print  "<h2>"
        print  commands.getoutput('cal')
        print	"</h2>"
	print  "</pre>"

elif  store ==  'REBOOT' :
        print  "<pre>"
        print  commands.getoutput('sudo reboot')
        print  "</pre>"



else:
	print  "<a href='http://127.0.0.1/index.html'>"

	print   "Take me back"
	print  "</a>"
