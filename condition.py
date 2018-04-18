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
     said1 = fill["field"]
     said2 = fill["condition"]
     said3 = fill["val"]
     main= said1 +"|"+said2+"|"+said3
     form = 1
     db.query('insert into cond1 (t1) values ("' \
               +main +'")')
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
      var nam=document.getElementById("selectlistid");
      txtName.value = ( nam.options[nam.selectedIndex].text);
//      var x = document.getElementById("selectlistid");
//      x.remove(x.selectedIndex);
    }}
    function SetCol() {{
      var txtName = document.getElementById("selectname");
      var com= document.getElementById("selectlistid2");
      txtName.value = txtName.value+"|"+( com.options[com.selectedIndex].text);
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


<h1 style="color:blue;">Specify your column and condition criteria </h1>
<hr>
<form method=POST> <br>
<table  align='center' cellspacing=2 cellpadding=5 id="data_table" border=1>
<tr>
<th>Field</th>
<th>Type</th>
<th>Value</th>
</tr>

<tr>
<td><select id="selectlistid" onchange="SetName()">
   {zzzzzzzz}
</select><input type="text"name ="field" id="new_name" width="1" height="1"></td>
<td><input type="text" name="condition" id="new_country">
<select id="typeid" onchange="SetType()">
<option value="Where ="> Where =</option>
<option value="Where <">Where < </option>
<option value="Where >">Where > </option>
<option value="Group by">Group by </option>
<option value="Order By">Order By</option>
</select></td>
<td><input type="text" name= "val" id="new_age"></td>
<td><input type="submit" class="add" onclick="add_row();" value="Add Row"></td>
</tr>

</table>
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
