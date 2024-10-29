

# After the setup ofthe database generallyy it is not needed more after one run to set up database.



import mysql.connector
dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Rikm@8776'
)

#prepare a cursor object
cursorObject=dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")