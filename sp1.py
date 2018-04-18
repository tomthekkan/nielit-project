#!/usr/bin/python
#-*-coding:utf-8-*-
from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql import SQLContext
import pandas
import cgi, cgitb, os, sys
import pandas as pd
import numpy as np
import MySQLdb
 
#from pyspark.context import SQLContext
#import org.apache.spark.sql.SQLContext




sc = SparkContext("local", "Simple App")
sqlContext = SQLContext(sc)
#spark = SparkSession(sc)
db= MySQLdb.connect("localhost", "root", "p220", "demo")
cursor= db.cursor()
cursor.execute("DROP TABLE proj11")
db.close()
df = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema", "true").load("/home/tom/Desktop/test/datafile.csv")
df.registerTempTable("ftable")

#Reading condition table
d1= sqlContext.read.format("jdbc").options( url="jdbc:mysql://localhost:3306/demo",driver = "com.mysql.jdbc.Driver",dbtable = "cond1",user="root", password="p220", header = False).load().persist().toPandas()

#Reading column selection table

d2= sqlContext.read.format("jdbc").options( url="jdbc:mysql://localhost:3306/demo",driver = "com.mysql.jdbc.Driver",dbtable = "condition2",user="root", password="p220", header = False).load().persist().toPandas()



i=0
while i<len(d1.index):
	s = d1['t1'][i]
	s1 = s.split('|')
	s2 = s1[1].split()
	a = "select * from ftable %s %s %s %s" %(s2[0], s1[0],s2[1],s1[2])
	b = sqlContext.sql(a)
	#b.show()
	i=i+1


b.registerTempTable("ftable2")
s = d2['d1'][0]
m = s.replace('|',',')
n = m[1:]
p = " select %s from ftable2" %(n)
r = sqlContext.sql(p)




#a = sqlContext.sql("select * from ftable limit 15")

r.write.format('jdbc').options(url='jdbc:mysql://localhost/demo',driver='com.mysql.jdbc.Driver',dbtable='proj11',user='root',password='p220').mode('append').save()
#df = sqlContext.read.load('home/tom/Documents/myworks/items.csv', format='com.databricks.spark.csv', header='true', inferSchema='true',encoding='utf-8')
#df.show()
#f = sqlContext.read.csv("/home/tom/Documents/myworks/items.csv", header=True, mode="DROPMALFORMED",encoding='utf-8')
#f.show()
#d1= sqlContext.read.format("jdbc").options( url="jdbc:mysql://localhost:3306/demo",driver = "com.mysql.jdbc.Driver",dbtable = "abc",user="root", password="p220").load().persist()


#a.show()
#d1= sqlContext.read.format("jdbc").option("url", "jdbc:mysql://localhost/demo").option("driver", "com.mysql.jdbc.Driver").option("dbtable", "abc").option("user", "root").option("password", "p220").load()

#df.registerTempTable("ftable")
#a = sqlContext.sql("select * from ftable")
b=r.toPandas()
#m = b.iloc[1:]
#m = b
#df = pd.read_csv(uploaded_file_path )
b.to_csv('/home/tom/Desktop/test/inp.csv',encoding="utf-8")
b.to_html(r'/var/www/html/test/f9.html', columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, bold_rows=True, classes=None, escape=True, max_rows=None, max_cols=None, show_dimensions=False, notebook=False, decimal='.', border=None)

db= MySQLdb.connect("localhost", "root", "p220", "demo")    
cursor= db.cursor()
cursor.execute("TRUNCATE TABLE cond1")
cursor.execute("TRUNCATE TABLE condition2")
#cursor.execute("DROP TABLE proj11")
db.close()
print """
<html>

<script src="https://www.w3schools.com/lib/w3.js"></script>
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
<center><div class="bbbbb"><a href="http://localhost/cgi-bin/Pro2.py" target="_blank" color="RED">Click here to Give your Conditions</a>
</div>
<div class="bbbbb"><a href="http://localhost/cgi-bin/selecttab.py" target="_blank" color="RED">Click here to Select your columns</a>
</div>
<div class="bbbbb"><a href="http://localhost/cgi-bin/spark.sh" target="_blank" color="RED">Click here to Select your columns</a>
</div>
<input type="submit" class="btn btn-primary btn-large" action="http://localhost/cgi-bin/spark.sh" value="Submit">
</div>
<center>

        <div w3-include-html="http://localhost/test/f9.html"class="blueTable">Selected Table</div>
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
"""

#print a
#d1.registerTempTable("d1table")
#sqlContext.sql("select * from d1table").toPandas().to_csv('/home/tom/Desktop/test/out.csv',encoding='utf-8')
#d1.show()
