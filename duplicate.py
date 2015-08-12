'''
Script for extracting the duplicate entries for accession 

'''
import MySQLdb
import xlsxwriter
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('duplicate_list.xlsx')
worksheet = workbook.add_worksheet()
dbLo=MySQLdb.connect("localhost","shailesh","123","shailesh")
curaLocl = dbLo.cursor()
curaLocl.execute("select t.accession,t.BookNo,t.BookName,t.authorName,t.callNo from book_info as t inner join accession_count as j on t.accession=j.accession where j.count > 1;")
dat=curaLocl.fetchall()
row = 0
col = 0
for i in dat:
	worksheet.write(row,col,i[0])
	worksheet.write(row,col+1,i[1])
	worksheet.write(row,col+2,i[2])
	worksheet.write(row,col+3,i[3])
	worksheet.write(row,col+4,i[4])
	col=0
	row=row+1
workbook.close()

