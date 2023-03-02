import DBConnection


conn = DBConnection.DBConnect()
myconnection = conn.estdbconnection()

mycursor=myconnection.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)