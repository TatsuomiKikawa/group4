import datetime
#import mysql.connector
import mysql.connector
try:
 #cnx = mysql.connector.connect()
 #cnx = mysql.connector.connect(user='root', password='yamamoto.Py4', host='52.21.17.184')
 cnx = mysql.connector.connect(user='group4', host='52.21.17.184', password='yamamoto.Py4', database='group4')
 cursor = cnx.cursor()
except:
	print("例外です") 
query = ("SELECT * FROM group4 WHERE Flag = 1")

#hire_start = datetime.date(1999, 1, 1)
#hire_end = datetime.date(1999, 12, 31)

#cursor.execute(query, (hire_start, hire_end))
cursor.execute(query)
#for (first_name, last_name, hire_date) in cursor:
#  print("{}, {} was hired on {:%d %b %Y}".format(
#    last_name, first_name, hire_date))
#for fetched_line in cursor.fetchall():
#		id = fetched_line[3]

print(f'{cursor.fetchall()}')
cnx.close()
