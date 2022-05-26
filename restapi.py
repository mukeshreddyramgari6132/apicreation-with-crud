from flask import Flask,Response,request
from pymongo import MongoClient
import json
from bson.objectid import ObjectId
app=Flask(__name__)

mongo=MongoClient(host="localhost",port=27017)
db = mongo.mukesh_reddys
mongo.server_info()

@app.route("/mobiles67",methods=["GET"])
def get_some_users():
    try:
        data=list(db.mobiles67.find())
        print(data)
        for user in data:
            user["_id"]=str(user["_id"])
        return Response(response=json.dumps(data),status=500,mimetype="application/json")
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message":"can  not read mobiles67"}),status=500,mimetype="application/json")
 #######post         
@app.route('/mobiles67',methods=["POST"])
def user_sent():
    try:
        user={'1':'2'}
        dbResponse = db.mobiles67.insert_one(user)
        print(dbResponse.inserted_id)
        return Response(response=json.dumps({"message":"user created","id":f"{dbResponse.inserted_id}"}),status=200,mimetype="application/json")

    except Exception as ex:
        print(ex)
#####update
@app.route('/mobiles67/<id>',methods=["PATCH"])
def user_update(id):
    try:
        dbResponse = db.mobiles67.update_one({'_id':ObjectId(id)},{'$set':{'name':request.form['url1']}})
        if dbResponse.modified_count == 1:
            return Response(response=json.dumps({"message":"user updsate one value"}),status=200,mimetype="application/json")
        return Response(response=json.dumps({"message":"user updsate nothing value"}),status=200,mimetype="application/json")
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message":"sorry cannot updated"}),status=200,mimetype="application/json")
############delete
@app.route('/mobiles67/<id>',methods=["DELETE"])
def user_delete(id):
    try:
        dbResponse = db.mobiles67.delete_one({'_id':ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(response=json.dumps({"message":"user delete one value","id":f"{id}"}),status=200,mimetype="application/json")
        return Response(response=json.dumps({"message":"user deleted nothing value"}),status=200,mimetype="application/json")
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message":"sorry cannot updated"}),status=200,mimetype="application/json")

if __name__=="__main__":
    app.run(port=5000,debug=True)