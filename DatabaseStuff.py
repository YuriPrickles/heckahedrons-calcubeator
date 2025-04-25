import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="MerLine",
    password="MagikrabsGauntlet",
    database="wirral"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM tag")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)