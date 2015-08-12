'''
script to migrate book information to koha database
'''
from pymarc import Record,Field,record_to_xml
import MySQLdb
record=Record()
print dir(record)
dbLo=MySQLdb.connect("localhost","shailesh","123","shailesh")
dbKoha=MySQLdb.connect("localhost","root","","koha1")
curaKoha=dbKoha.cursor()
curaLocl = dbLo.cursor()
curaLocl.execute("select BookNo,BookName,authorName from book_info group by BookNo;")
dat=curaLocl.fetchall()
curaLocl.execute("select accession,BookNo,callNo from book_info;")
datIte=curaLocl.fetchall()
for i in dat:
		record=Record()
		record.add_field(Field(tag='040',indicators=['0','1'],subfields=['c','LIBRARY OF CONGRESS']))
		record.add_field(Field(tag='245',indicators=['0','1'],subfields=['a',i[1]]))	
		record.add_field(Field(tag='942',indicators=['0','1'],subfields=['2','book of parag','c','BOOK']))
		record.add_field(Field(tag='100',indicators=['0','1'],subfields=['a',i[2]]))
		record.add_field(Field(tag='999',indicators=['0','1'],subfields=['c','8','d','8']))
		marcI=record_to_xml(record)
		#print i[0],i[1],i[2]
		curaKoha.execute("insert into biblio(biblionumber,title,author) values(%s,%s,%s);",(i[0],i[1],i[2]))
		curaKoha.execute("insert into biblioitems(biblionumber,biblioitemnumber,marcxml) values(%s,%s,%s);",(i[0],i[0],marcI))

for i in datIte:
		barcode='1111'+str(i[0])
		curaKoha.execute("insert into items(itemnumber,biblionumber,biblioitemnumber,barcode,itemcallnumber) values(%s,%s,%s,%s,%s);",(i[0],i[1],i[1],barcode,i[2]))

dbKoha.commit()
dbKoha.close()		
