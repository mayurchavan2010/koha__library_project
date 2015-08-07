import MySQLdb
db=MySQLdb.connect("192.168.8.45","deeksha","123","deeksha")
dbLo=MySQLdb.connect("localhost","shailesh","123","shailesh")
curs=db.cursor()
curaLocl=dbLo.cursor()
curs.execute("select Accession,BookNo,BookName,Author_FirstName1,Author_LastName1,Author_MiddleName1,Author_FirstName2,Author_LastName2,Author_MiddleName2,CallNo from lib_booktitle")

for i in curs.fetchall():
	curaLocl.execute("insert into shailesh.book_info(accession,BookNo,authorName,callNo) values(%s,%s,%s,%s)",(i[0],i[1],i[2],i[9]))
dbLo.commit()
dbLo.close()

