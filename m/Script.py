import mysql.connector
import datetime
import csv

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="product"
)
cursor=db.cursor()

# sql="CREATE TABLE data(Segment VARCHAR(200),Country VARCHAR(200),Product VARCHAR(200),Discount_Band VARCHAR(200),Units_Sold int,Manufacturing_Price int,Sale_Price int,Gross_Sales int,Discounts int,Sales int,COGS int,Profit int,Date date,Month_Number int,Month_Name VARCHAR(200),Year int)"
# cursor.execute(sql)

filename="C:/Users/Asus/Desktop/m/Financial.csv"
with open(filename,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    x=next(csvreader)
    for row in csvreader:
        Segment=row[0].strip()
        Country=row[1].strip()
        Product=row[2].strip()
        Discount_Band=row[3].strip()
        Units_Sold=float(row[4].replace("$","").strip())
        Manufacturing_Price=float(row[5].replace("$","").strip())
        Sale_Price=float(row[6].replace("$","").strip())
        Gross_Sales=float(row[7].replace("$","").replace(",","").strip())
        Discounts=float("0" + row[8].replace("$","").replace(",","").replace("-","").strip())
        Sales=float(row[9].replace("$","").replace(",","").replace("-","").strip())
        COGS=float(row[10].replace("$","").replace(",","").strip())
        Profit=float("0" + row[11].replace("$","").replace(",","").replace("-","").replace(")","").replace("(","").strip())
        Date= datetime.datetime.strptime(row[12],'%m/%d/%Y').strftime("%Y-%m-%d")
        Month_Number=float(row[13])
        Month_Name=row[14].strip()
        Year=float(row[15])
        sql="Insert into data( Segment, Country, Product, Discount_Band, Units_Sold, Manufacturing_Price, Sale_Price, Gross_Sales, Discounts, Sales, COGS, Profit, Date, Month_Number, Month_Name,Year ) values" 
        sql+="('{}','{}','{}','{}','{}' ,'{}' ,'{}' ,'{}' ,'{}' ,'{}' ,'{}' ,'{}' ,'{}','{}' ,'{}','{}' )".format(Segment,Country,Product,Discount_Band,Units_Sold ,Manufacturing_Price ,Sale_Price ,Gross_Sales ,Discounts ,Sales ,COGS ,Profit ,Date ,Month_Number ,Month_Name,Year)
        #print(sql)
        cursor.execute(sql)

db.commit()