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
</SCRIPT>
<SCRIPT language="javascript">

function updateTable(oldValue,collumn,referenceName){
	var newValue = prompt("Please enter new value", oldValue)
	if(newValue==null){
	
	}
	else
	{
	if(collumn==0){
	var column='name'; 
	}
	else if(collumn==1){
	var column='email';
	}
	else if(collumn==2){
	var column='password'
	}

	$.ajax({
		url: "updateColumn.py",
		type: "post",
		datatype:"json",
		data: {'column':column,'oldValue':oldValue,'newValue':newValue,'referenceName':referenceName},
		success:function(result){
			$("#result").html(result);
		},
		error:function(error){
			if (e.originalEvent.defaultPrevented) return;		}
		});
	
	}
	}
function deleteTable(tableid){
	
	var nameToDel =tableid;
	
	
	$.ajax({
           url: "del.py",
           type: "post",
           datatype:"json",
           data: {'name': nameToDel},
           success: function(result){
           	$("#result").html(result);
           },
           error:function(error){
				if (e.originalEvent.defaultPrevented) return;		}
       });
}




</script>

""")
print("</head>")
print("<body>")

fs = cgi.FieldStorage()

#json_parsed = json.loads(data)
name=fs.getvalue("name")
password=fs.getvalue("password")
email=fs.getvalue("email")
#print(name+" "+password+" "+email)


try:
	hello=cursor.execute('insert into form1 values("%s", "%s","%s")' %(name, email, password))

	conn.commit()
	
	cursor.execute("Select * from form1")
	
	print("<br><br>")
	print("<table border=1 id=\"databaseTable\" class=\"databaseTable\"><thead><tr><th> CHECK</th><th> Name</th><th> Email</th><th> Password</th><th>Action</th></tr></thead><tbody>")
	data=cursor.fetchall()
	for row in data:
		print("<tr id="+row[0]+"><TD><INPUT type=\"checkbox\" name=\"chk\"/></TD> <td  onclick=\"updateTable('"+row[0]+"',0,'"+row[0]+"') \"  >"+row[0]+"</td><td  onclick=\"updateTable('"+row[1]+"',1,'"+row[0]+"') \" >"+row[1]+"</td><td  onclick=\"updateTable('"+row[2]+"',2,'"+row[0]+"') \"  >"+row[2]+"</td><td><Button class= \"Delete\" onclick=\"deleteTable('"+row[0]+"')\">Delete</Button></td></tr>")
	cursor.close()
	print("</tbody></table><br>")
	print(row)
except:

	conn.rollback()
	print("rollback")
conn.close()
print("""
	<div id="result">

</div>""")
print("</body></html>")









#print(fs["name"].key)
#sys.stdout.write(json.dumps(fs,indent=1))
#sys.stdout.write("\n")

#jsonData = '{"name": "Frank", "age": 39}'
#jsonToPython = json.loads(data)
#print(jsonToPython)
#print("")