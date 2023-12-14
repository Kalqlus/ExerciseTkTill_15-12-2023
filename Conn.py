import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'ContactsKS'
}

Connection = mysql.connector.connect(**config)

if Connection.is_connected(): print("Connected to MySQL database")
cursor = Connection.cursor()
