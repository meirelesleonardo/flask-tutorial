
import pyodbc 

from decouple import config


# Some other example server values are
# server = '(localdb)\MSSQLLocalDB' # for a named instance
# server = 'myserver,port' # to specify an alternate port
 
server = config("HOST_BD_SQLSERVER")
database = config("DATABASE_BD_SQLSERVER") 
username = config("USER_BD_SQLSERVER")
password = config("PASSWORD_BD_SQLSERVER")  
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()