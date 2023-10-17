#WEB API LIB
from flask import Flask
from flask import request
from flask_cors import CORS
import json
import time

#MACHINE LEARNING LIB
import pandas as pd
#machine learning algorythm (decisin tree)
from sklearn.tree import DecisionTreeClassifier

#CREATING FLASK APP
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

#MACHINE LEARNING
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




#API
@app.route('/', methods = ["GET", "POST"])
def handle_request():
    
    input = str(request.args.get("input"))  #request the input

    myList = input.split()
    res = [eval(i) for i in myList]
    data = []
    
    if input == "None":
        input = "makato"
    
    else:
        #making prediction of next chord (position / voicing)
        predictions = model.predict([ res ])

        #NEW
        value1 = str(predictions[0][0])
        value2 = str(predictions[0][1])
        this_prediction = value1 + value2
    
        data = this_prediction

        #OLD
        #data = str(predictions)

    data_set = {"input": input, "res": res, "prediction": data}
    json_dump = json.dumps(data_set)

    return json_dump

    


    
    

