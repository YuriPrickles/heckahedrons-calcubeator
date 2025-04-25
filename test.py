import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="MerLine",
    password="MagikrabsGauntlet",
    database="wirral"
)

mycursor = mydb.cursor()