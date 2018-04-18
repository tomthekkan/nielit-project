#!/usr/bin/env python
#!/usr/bin/php


"""Python, MySQL and CGI (Common Gateway Interface) all
in the same demo script.

Note - need to moderate live public boards of this type!
"""
import os
import cgi
import MySQLdb
import pandas as pd
import numpy as np
# Following line is what you would need to create table
# prior to running for the first time
#
# create table comment
#     (info  text, enteredat timestamp,
#     cid int primary key not null auto_increment)

# Connect to MySQL database
db = MySQLdb.connection(host='localhost',user="root",passwd="p220",db="demo")
#db = MySQLdb.connection('host=mysql://root:p220@localhost:3306/demo')

df = pd.read_csv('/home/tom/Desktop/test/datafile.csv')
# Collect values from form
inputs = cgi.FieldStorage()
fill = {}
for key in inputs:
   fill[key] = inputs[key].value

# If the form was completed, save what was entered on it
try:
     said1 = fill["selected1"]
     form = 1
     db.query('insert into condition2 (d1) values ("' \
               +said1 +'")')
except:
     form = 0
lister = list(df)

html_list = ''
for value in lister:
   html_list += '<option value={0}>{0}</option>'.format(value)


print """Content-type: text/html\n
 
<!DOCTYPE html>
<html>
  <head>
<script src="https://www.w3schools.com/lib/w3.js"></script>
    <title>Condition</title>
<script>

    function SetName() {{
      var txtName = document.getElementById("new_name");
      txtName.value = ( document.getElementById("selectlistid").value);
//      var x = document.getElementById("selectlistid");
//      x.remove(x.selectedIndex);
    }}
    function SetCol() {{
      var txtName = document.getElementById("selectname");
      var nam=document.getElementById("selectlistid2");
      txtName.value = txtName.value+"|"+( nam.options[nam.selectedIndex].text);
//      txtName.value = txtName.value+"|"+( document.getElementById("selectlistid2").value);
//      var x = document.getElementById("selectlistid");
//      x.remove(x.selectedIndex);
    }}

     function SetType() {{
      var txtType = document.getElementById("new_country");
      txtType.value = ( document.getElementById("typeid").value);
//      var x = document.getElementById("selectlistid");
//      x.remove(x.selectedIndex);
    }}
</script><body>
<link rel="stylesheet" href="cgi-bin\bootstrap.css">


<h1 style="color:blue;">Specify your column </h1>
<hr>
<form method=POST> <br>
<h2>Select your columns
<h2>
<select id="selectlistid2" onchange="SetCol()">
   {zzzzzzzz}
</select>
<input type="text" name="selected1" id="selectname" width="1" height="1"><br>
<input type="submit" class="btn btn-primary btn-large" name ="selected" >

</form>
<center>

        <div w3-include-html="http://localhost/test/f2.html"class="blueTable" >rthgsdfhs</div>
        </center>   
<hr>
</body></html>
""".format(zzzzzzzz=html_list)
print ""

arguments = cgi.FieldStorage()
for i in arguments.keys():
 print arguments[i].value
