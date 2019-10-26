
# A very simple Flask Hello World app for you to get started with...
import sys
from flask import Flask,request

import os
import MySQLdb
from spam_filter.spam_filter import train
from spam_filter.spam_filter import predict


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello'

@app.route("/train")
def train_model():
    return train()

@app.route("/predict")
def predict_spam():
    if validate_request(request.args.get('apikey')):
        return predict(request.args.get('message'))
    else:
        return "invalid key"




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



if __name__ == '__main__':
	app.run()
#	app.run(port=80)
