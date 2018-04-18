#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgitb
import cgi
import MySQLdb
import cgitb
import pandas as pd
import numpy as np
cgitb.enable()
#db = MySQLdb.connect('host=mysql://root:p220@localhost:3306/demo')
form = cgi.FieldStorage()
arguments = cgi.FieldStorage()
for i in arguments.keys():
 uploaded_file_path=arguments[i].value
df = pd.read_csv(uploaded_file_path )
lister = list(df)

html_list = ''
for value in lister:
   html_list += '<option value={0}>{0}</option>'.format(value)


html = """Content-type: text/html\n
 
<html>

<script src="https://www.w3schools.com/lib/w3.js"></script>
""".format(zzzzzzzz=html_list)
print(html)
print"""
<head>
<style>


div.blueTable {{
  overflow: scroll;
height:50%;
  text-align: left;
}}
div.blueTable td, table.blueTable th {{

  padding: 3px 2px;
}}
div.blueTable tbody td {{
  font-size: 9px;
}}
div.blueTable tr:nth-child(even) {{
  background: #D0E4F5;
}}
div.blueTable thead {{
  background: #1C6EA4;
  background: -moz-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  background: -webkit-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  background: linear-gradient(to bottom, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
}}
div.blueTable thead th {{
  font-size: 11px;
  font-weight: bold;
  color: #FFFFFF;

}}
div.blueTable thead th:first-child {{
  border-left: none;
}}

div.blueTable tfoot {{
  font-size: 14px;
  font-weight: bold;
  color: #FFFFFF;
  background: #D0E4F5;
  background: -moz-linear-gradient(top, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  background: -webkit-linear-gradient(top, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  background: linear-gradient(to bottom, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);

}}
div.bbbbb{{
background-color: lightblue;
}}
div.blueTable tfoot td {{
  font-size: 14px;
}}
div.blueTable tfoot .links {{
  text-align: right;
}}
div.blueTable tfoot .links a{{
  display: inline-block;
  background: #1C6EA4;
  color: #FFFFFF;
  padding: 2px 8px;

}}
      /* NOTE: The styles were added inline because Prefixfree needs access to your styles and they must be inlined if they are on local disk! */
    
.btn {{ display: inline-block; *display: inline; *zoom: 1; padding: 4px 10px 4px; margin-bottom: 0; font-size: 13px; line-height: 18px; color: #333333; text-align: center;text-shadow: 0 1px 1px rgba(255, 255, 255, 0.75); vertical-align: middle; background-color: #f5f5f5; background-image: -moz-linear-gradient(top, #ffffff, #e6e6e6); background-image: -ms-linear-gradient(top, #ffffff, #e6e6e6); background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#ffffff), to(#e6e6e6)); background-image: -webkit-linear-gradient(top, #ffffff, #e6e6e6); background-image: -o-linear-gradient(top, #ffffff, #e6e6e6); background-image: linear-gradient(top, #ffffff, #e6e6e6); background-repeat: repeat-x; filter: progid:dximagetransform.microsoft.gradient(startColorstr=#ffffff, endColorstr=#e6e6e6, GradientType=0); border-color: #e6e6e6 #e6e6e6 #e6e6e6; border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25); border: 1px solid #e6e6e6; -webkit-border-radius: 4px; -moz-border-radius: 4px; border-radius: 4px; -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05); -moz-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05); box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05); cursor: pointer; *margin-left: .3em; }}
.btn:hover, .btn:active, .btn.active, .btn.disabled, .btn[disabled] {{ background-color: #e6e6e6; }}
.btn-large {{ padding: 9px 14px; font-size: 15px; line-height: normal; -webkit-border-radius: 5px; -moz-border-radius: 5px; border-radius: 5px; }}
.btn:hover {{ color: #333333; text-decoration: none; background-color: #e6e6e6; background-position: 0 -15px; -webkit-transition: background-position 0.1s linear; -moz-transition: background-position 0.1s linear; -ms-transition: background-position 0.1s linear; -o-transition: background-position 0.1s linear; transition: background-position 0.1s linear; }}
.btn-primary, .btn-primary:hover {{ text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25); color: #ffffff; }}
.btn-primary.active {{ color: rgba(255, 255, 255, 0.75); }}
.btn-primary {{ background-color: #4a77d4; background-image: -moz-linear-gradient(top, #6eb6de, #4a77d4); background-image: -ms-linear-gradient(top, #6eb6de, #4a77d4); background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#6eb6de), to(#4a77d4)); background-image: -webkit-linear-gradient(top, #6eb6de, #4a77d4); background-image: -o-linear-gradient(top, #6eb6de, #4a77d4); background-image: linear-gradient(top, #6eb6de, #4a77d4); background-repeat: repeat-x; filter: progid:dximagetransform.microsoft.gradient(startColorstr=#6eb6de, endColorstr=#4a77d4, GradientType=0);  border: 1px solid #3762bc; text-shadow: 1px 1px 1px rgba(0,0,0,0.4); box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.5); }}
.btn-primary:hover, .btn-primary:active, .btn-primary.active, .btn-primary.disabled, .btn-primary[disabled] {{ filter: none; background-color: #6a77d4; }}
.btn-block {{ width: 10%; display:block; }}

* {{ -webkit-box-sizing:border-box; -moz-box-sizing:border-box; -ms-box-sizing:border-box; -o-box-sizing:border-box; box-sizing:border-box; }}

html {{ width: 100%; height:100%; }}

body {{ 

	
	font-family: 'Open Sans', sans-serif;
	

	background: -webkit-radial-gradient(0% 100%, ellipse cover, rgba(104,128,138,.4) 10%,rgba(138,114,76,0) 40%), linear-gradient(to bottom,  rgba(57,173,219,.25) 0%,rgba(42,60,87,.4) 100%), linear-gradient(135deg,  #670d10 0%,#092756 100%);
	filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#3E1D6D', endColorstr='#092756',GradientType=1 );
}}
.title {{ 

	top: 20%;

}}
.title {{ color: #fff; text-shadow: 0 0 10px rgba(0,0,0,0.3); letter-spacing:1px; text-align:center; }}

input {{ 
	
	margin-bottom: 10px; 
	background: rgba(0,0,0,0.3);
	border: none;
	outline: none;
	padding: 10px;
	font-size: 13px;
	color: #fff;
	text-shadow: 1px 1px 1px rgba(0,0,0,0.3);
	border: 1px solid rgba(0,0,0,0.3);
	border-radius: 4px;
	box-shadow: inset 0 -5px 45px rgba(100,100,100,0.2), 0 1px 1px rgba(255,255,255,0.2);
	-webkit-transition: box-shadow .5s ease;
	-moz-transition: box-shadow .5s ease;
	-o-transition: box-shadow .5s ease;
	-ms-transition: box-shadow .5s ease;
	transition: box-shadow .5s ease;
}}
input:focus {{ box-shadow: inset 0 -5px 45px rgba(100,100,100,0.4), 0 1px 1px rgba(255,255,255,0.2); }}

    </style>
<script type="text/javascript" src="table_script.js"></script>
</head>
</body>
<script>
    function SetName() {{
      var txtName = document.getElementById("new_name");
      txtName.value = ( document.getElementById("selectlistid").value);
//      var x = document.getElementById("selectlistid");
//      x.remove(x.selectedIndex);
    }}
    function SetCol() {{
      var txtName = document.getElementById("selectname");
      txtName.value = txtName.value+"|"+( document.getElementById("selectlistid2").value);
//      var x = document.getElementById("selectlistid");
//      x.remove(x.selectedIndex);
    }}

     function SetType() {{
      var txtType = document.getElementById("new_country");
      txtType.value = ( document.getElementById("typeid").value);
//      var x = document.getElementById("selectlistid");
//      x.remove(x.selectedIndex);
    }}
</script>
<body onload="">
<p><h2></h2></p>
<center><div class="bbbbb"><a href="http://localhost/cgi-bin/condition.py" target="_blank" color="RED">Click here to Give your Conditions</a>
</div><br><br>
<div class="bbbbb"><a href="http://localhost/cgi-bin/selection.py" target="_blank" color="RED">Click here to Select your columns</a>
</div></br><br><br><br>
<div class="bbbbb"><a href="http://localhost/cgi-bin/spark.sh" target="_blank" color="RED">Click here to Process</a>
</div>
<input type="submit" class="btn btn-primary btn-large" action="http://localhost/cgi-bin/spark.sh" value="Submit">
</div>
<center>

        <div w3-include-html="http://localhost/test/f2.html"class="blueTable">Selected Table</div>
        </center>   
<script>
w3.includeHTML();
</script>
<center>
<div class="bbbbb">
        <a href="http://localhost/test/plot.php" target="_blank">Plot your Datab</a><br></div>
        Your File Path is
        </center>   
</body>
</html>
""".format(zzzzzzzz=html_list)
print ""

arguments = cgi.FieldStorage()
for i in arguments.keys():
 print arguments[i].value
