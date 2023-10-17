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


    
    #text = str(request.args.get("input"))  #request the input
    #character_count = len(text)

    text = str("3 2")

    myList = text.split()
    res = "nope"
    data = "none"
    
    if text == "None":
        text = "makato"
    
    else:
        myList = text.split()
        res = [eval(i) for i in myList]

        #make a 2 predictions (ask what gendre probably like 21old male, 22old female)
        predictions = model.predict([ res ])
        data = predictions
    

    data_set = {"data": data, "text": text}
    json_dump = json.dumps(data_set)

    return json_dump

    


    
    

