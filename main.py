import csv
from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
f = open("data.csv", "r")
reader = csv.reader(f)

data = {"BigSprings" : {"Spaces": [], "Time": []},
        "Lot6" : {"Spaces": [], "Time": []},
        "Lot26" : {"Spaces": [], "Time": []},
        "Lot30" : {"Spaces": [], "Time": []},
        "Lot32" : {"Spaces": [], "Time": []}}

for row in reader:
        #row[0] = parking lot name
        #row[1] = time
        #row[2] = space
    if row[0] == "Big Springs":
        data["BigSprings"]["Spaces"].append(row[1])
        data["BigSprings"]["Time"].append(row[2])
    elif row[0] == "Lot 6":
        data["Lot6"]["Spaces"].append(row[1])
        data["Lot6"]["Time"].append(row[2])
    elif row[0] == "Lot 26":
        data["Lot26"]["Spaces"].append(row[1])
        data["Lot26"]["Time"].append(row[2])
    elif row[0] == "Lot 30":
        data["Lot30"]["Spaces"].append(row[1])
        data["Lot30"]["Time"].append(row[2])
    elif row[0] == "Lot 32":
        data["Lot32"]["Spaces"].append(row[1])
        data["Lot32"]["Time"].append(row[2])

print(data["BigSprings"])
print(data["Lot6"])
print(data["Lot26"])
print(data["Lot30"])
print(data["Lot32"])
f.close()

@app.route('/BigSprings', methods=['GET'])
def springs():
    return json.dumps(data["BigSprings"])

@app.route('/Lot6', methods=['GET'])
def lot6():
    return json.dumps(data["Lot6"])

@app.route('/Lot26', methods=['GET'])
def lot26():
    return json.dumps(data["Lot26"])

@app.route('/Lot30', methods=['GET'])
def lot30():
    return json.dumps(data["Lot30"])

@app.route('/Lot32', methods=['GET'])
def lot32():
    return json.dumps(data["Lot32"])
app.run()