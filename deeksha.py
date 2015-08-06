import MySQLdb
db=MySQLdb.connect("192.168.8.45","deeksha","123","deeksha")
dbLo=MySQLdb.connect("localhost","root","","shailesh")
curs=db.cursor()
curaLocl=dbLo.cursor()
#curs.execute("select Accession,BookNo,BookName,Author_FirstName1,Author_LastName1,Author_MiddleName1,Author_FirstName2,Author_LastName2,Author_MiddleName2,CallNo from lib_booktitle")
#for i in curs.fetchall():
#	print i
#	authorsList=""
	#if i[3] != "None" or i[3] != "":
	#	print i[3]
	#	authorsList=authorsList+i[3]
	#if i[4] != "None" or i[4] != "":
	#	print i[4]
	#	authorsList=authorsList + i[4]
	#if i[5] != "None" or i[5] != "":
        #	print i[5]
	#        authorsList=authorsList + i[5]	
	#print authorsList	
#	authorsList=i[3]+" "+i[4]+" "+" "+i[5]
	
	#curaLocl.execute("insert into book_info values("+str(i[0])+","+str(i[1])+",'"+i[2]+"','shailesh cheke',"+str(i[9])+")")
curaLocl.execute("insert into shailesh.book_info(accession,BookNo) values(123,123)")
dbLo.close()
db.close()
