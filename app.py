import pandas as pd

#machine learning algorythm (decisin tree)
from sklearn.tree import DecisionTreeClassifier

#IMPORT DATA
music_data = pd.read_csv("chords2.csv")

#CLEANING DATA
#input dataset
X = music_data.drop(columns=["ta", "tv"])

#output dataset
y = music_data.drop(columns=["pa", "pv"])



model = DecisionTreeClassifier()

#adding datasets to model (input, output)
model.fit(X,y)





#WEB API
from flask import Flask
from flask import request
import json
import time

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def handle_request():


    
    text = str(request.args.get("input"))  #request the input
    character_count = len(text)

    myList = text.split()
    res = [eval(i) for i in myList]

    
    #make a 2 predictions (ask what gendre probably like 21old male, 22old female)
    predictions = model.predict([ [3,2] ])

    

    data_set = {"input": res, "timestamp": time.time(), "character_count": character_count}
    json_dump = json.dumps(data_set)

    return json_dump
    




