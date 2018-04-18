#!/bin/sh
printf "Content-Type: text/html\r\n\r\n"
#python /usr/lib/cgi-bin/upload1.py
/usr/local/spark/bin/spark-submit /usr/lib/cgi-bin/sp1.py
#python /usr/lib/cgi-bin/upload1.py

#printf "Content-Type: text/html\n\n"
#/usr/local/spark/bin/spark-submit /usr/lib/cgi-bin/sparkapp.py
#printf "Content-type:text/html\r\n\r\n"
#printf "<html>\n"
#printf "<head>\n"
#printf "<title>Hello Word - First CGI Program</title>\n"
#printf "</head>\n"
#printf "<body>\n"
#printf "<h2>Hello Word! This is my first CGI program</h2>\n"
#printf "</body>\n"
#printf "</html>\n"
#printf "Content-Type: text/plain\r\n\r\n"
