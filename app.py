from flask import Flask
import json
from mondodb import mongodbConfig
mongodbConfig = mongodbConfig()
app = Flask(__name__)




@app.route('/')
def getAll():
    response =[]
    for item in mongodbConfig.machines.find({},{"_id":0 , "code":1}):
        response.append(item["code"])
    for item in mongodbConfig.pods.find({},{"_id":0 , "code":1}):
        response.append(item["code"])
    return json.dumps(response)



@app.route('/machines')
def getAllMachines():
    response =[]
    for item in mongodbConfig.machines.find({},{"_id":0 , "code":1}):
        response.append(item["code"])
    return json.dumps(response)



@app.route('/pods')
def getAllPods():
    response =[]
    for item in mongodbConfig.pods.find({},{"_id":0 , "code":1}):
        response.append(item["code"])
    print(response)
    return json.dumps(response)




@app.route('/machines/<param>')
def getMachinesFiltered(param):
    response = []
    if param == "small" or "large" or "espresso":
        query = {"size":param}
    elif param == "true" or "false":
        query = {"waterLine":param}
    for item in mongodbConfig.machines.find(query , {"_id":0 , "code":1}):
        response.append(item["code"])
    return json.dumps(response)



@app.route('/pods/<param>')
def getPodsFiltered(param):
    response = []
    if param == "1" or "3" or "5" or "7":
        query = {"packSize":param}
    elif param == "vanilla" or "caramel" or "psl" or "mocha" or "hazelnut":
        query = {"flavor":param}
    for item in mongodbConfig.pods.find(query , {"_id":0 , "code":1}):
        response.append(item["code"])
    return json.dumps(response)


#### to filter using product type write "http://127.0.0.1:5000/pods" or "http://127.0.0.1:5000/machines"
#### to filter pods using dozen packs replace param with 1 or 3 or 5 or 7
#### to filter pods using flavor replace param with vanilla or caramel or psl or mocha or hazelnut
#### to filter machines using water line replace param with true or false
#### to filter machines using machine size replace param with small or large or espresso