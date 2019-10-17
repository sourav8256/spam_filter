import MySQLdb

conn = MySQLdb.connect (host = "sourav8256.mysql.pythonanywhere-services.com",
                        user = "sourav8256",
                        passwd = "password123",
                        db = "sourav8256$database")
cursor = conn.cursor ()
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone ()
print("server version:" + row[0])
cursor.close ()
conn.close ()