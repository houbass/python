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

#make a 2 predictions (ask what gendre probably like 21old male, 22old female)
predictions = model.predict([ [3, 2] ])
print(predictions)


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "THIS IS MY NEW API"
