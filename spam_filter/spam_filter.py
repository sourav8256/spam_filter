import sys
import numpy as np
import pandas as pd
import json
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB

model_file = 'model.sav'
count_vector_file = 'count_vector.sav'


def predict(sample):
    result = {}
    result['input'] = sample
    cv = joblib.load(count_vector_file)
    x_testcv = cv.transform([sample])
    loaded_model = joblib.load(model_file)
    predictions = loaded_model.predict(x_testcv)
    prediction = predictions[0]
    result['debug'] = int(json.dumps(int(predictions[0])))
    if prediction == 0:
        result['value'] = 1
        result['message'] = ("Spam")
    else:
        result['value'] = 0
        result['message'] = ("Not Spam")
    return json.dumps(result)


def train():
    print("Training model...\n")
    df = pd.read_csv('mysite/spam_filter/smsspam', sep='\t', names=['Status', 'Message'])
    df.loc[df["Status"] == 'ham', "Status", ] = 1
    df.loc[df["Status"] == 'spam', "Status", ] = 0

    df_x = df["Message"]
    df_y = df["Status"]

    x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.3, random_state=4)

    cv1 = CountVectorizer()
    x_traincv = cv1.fit_transform(x_train)
    mnb = MultinomialNB()
    y_train = y_train.astype('int')
    mnb.fit(x_traincv, y_train)
    # save the model to disk
    joblib.dump(mnb, model_file)
    # cv1.fit_transform(x_train)
    joblib.dump(cv1, count_vector_file)
    print("Training complete ... \n")
    return test(mnb, cv1, x_test, y_test)


def test(mnb, cv1, x_test, y_test):
    print("Testing model ... \n")
    x_testcv = cv1.transform(x_test)
    predictions = mnb.predict(x_testcv)
    a = np.array(y_test)
    count = 0
    for i in range(len(predictions)):
        if predictions[i] == a[i]:
            count = count + 1
    accuracy = count/len(predictions)*100
    return ("Testing complete Accuracy is "+str(accuracy)+" %\n")



    #train()
    #predict("subscribe to my channel")

if __name__ == "__main__":
    train()
    test()
    predict()
