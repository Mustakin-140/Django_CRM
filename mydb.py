import mysql.connector
dataBase=mysql.connector.connect(
host='localhost',
user='root',
passwd='Mahi@cse140'     
 )

cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("DONE")