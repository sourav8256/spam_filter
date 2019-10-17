import MySQLdb
from datetime import datetime

def validate_request(key):


    conn = MySQLdb.connect (host = "sourav8256.mysql.pythonanywhere-services.com",
                    user = "sourav8256",
                    passwd = "password123",
                    db = "sourav8256$database")

    mycursor = conn.cursor()
    mycursor.execute("SElECT * FROM `registration` WHERE `api_key`=%s",(key,));
    row = mycursor.fetchone()
    mycursor.close()
    conn.close()


    if mycursor.rowcount > 0 :

        if row[5] == "ACTIVE" :

            if row[2] > datetime.timestamp(datetime.now()) :

                return True


    return False



print(validate_request("firstandnwapikey"))
print(validate_request("firstandnewapikey"))
