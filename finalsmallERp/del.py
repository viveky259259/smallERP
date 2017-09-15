#!/usr/bin/python3.5

print("content-type:text/html\r\n\r\n")

import sys
import json
import cgi
import pymysql

try:
	conn = pymysql.connect ( "localhost" , "root" , "" , "vivek" )
except:	
	print("connection unsuccessful<br>")

cursor = conn.cursor ( )

print("""
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<HEAD><TITLE> edit</TITLE>
<SCRIPT src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js">


function updateTable(tablename,tableemail,tablepassword){
	var name=tablename;
	var email=tableemail;
	var password=tablepassword;
	
	$.ajax({
		url:"update.py",
		type:"post",
		datatype:"json",
		data:{'name':name, 'password':password, 'email':email},
		success:function(result){
			$("#result").html(result);
		},
		error:function(error){
			if (e.originalEvent.defaultPrevented) return;		}
		});
	


	}











</SCRIPT>
""")
print("</head>")
print("<body>")

fs = cgi.FieldStorage()

#json_parsed = json.loads(data)
name=fs.getvalue("name")
#print(name)

try:
	hello=cursor.execute('DELETE FROM form1 WHERE name="%s"'%(name))
	conn.commit()

	cursor.execute("Select * from form1")
	print("<br><br>")
	print("<table border=1 id=\"databaseTable\" class=\"databaseTable\"><thead><tr><th> CHECK</th><th> Name</th><th> Email</th><th> Password</th><th>Action</th></tr></thead><tbody>")
	data=cursor.fetchall()
	for row in data:
		print("<tr id="+row[0]+"><TD><INPUT type=\"checkbox\" name=\"chk\"/></TD> <td  onclick=\"updateTable('"+row[0]+"',0,'"+row[0]+"') \"  >"+row[0]+"</td><td  onclick=\"updateTable('"+row[1]+"',1,'"+row[0]+"') \" >"+row[1]+"</td><td  onclick=\"updateTable('"+row[2]+"',2,'"+row[0]+"') \"  >"+row[2]+"</td><td><Button class= \"Delete\" onclick=\"deleteTable('"+row[0]+"')\">Delete</Button></td></tr>")
	cursor.close()
	print("</tbody></table><br>")
	print("</body></html>")
except:

	print(conn.rollback())
	print("rollback")
conn.close()

