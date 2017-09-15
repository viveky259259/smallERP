#!/usr/bin/python3.5

print("content-type:text/html\r\n\r\n")
import pymysql
import json,sys
#open database connection 
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

<SCRIPT>
$(document).ready(function(){
	$(".Delete").click(function(){
		$(this).css("color","yellow");

	});
	$(".Update").click(function(){
		$(this).css("color","red");

	});
	
	$(".fillForm").click(function(){
		$(this).css("color","black");

	});
	$(".Add").click(function(){
		$(this).css("color","#987456");

	});
	
	


	var data={};
	data.name=$("#name").val();
	data.email=$("#email").val();
	data.password=$("#password").val();

	$(".Add").click(function(){
		var namedata =$("#name").val();
		var emaildata =$("#email").val();
		var passworddata =$("#password").val();
		var jsData=JSON.stringify( data );
		$.ajax({
               url: "ajaxre.py",
               type: "post",
               datatype:"json",
               data: {'name': namedata,'email':emaildata, 'password':passworddata },
               success: function(result){
               	$("#result").html(result);
               },
               error:function(error){
					if (e.originalEvent.defaultPrevented) return;		}
           });
		
		
		});

	$(".update").click(function(){
		alert("going to update");
		$.ajax({
               url: "updateForm.py",
               type: "post",
               datatype:"json",
               success: function(result){
               	$("#form").html(result);
               },
               error:function(error){
					if (e.originalEvent.defaultPrevented) return;		}
           });
		
		
		});




	});


</SCRIPT>
""")


print("</head>")
print("<body>")
print("""<div id="form">
<form method="post" name="InputForm" >
Name:<input name="name" id="name"></input><br/>
Password:<input name="password" id="password"></input><br/>
Email: <input name="email" id= "email" ></input>
<br/>
<br />
 
</form>
<button class="Add" type="submit">Add</button></div>
""")

conn.close()
print("""
<div id="result">
</div>

""")

print("</body></html>")

