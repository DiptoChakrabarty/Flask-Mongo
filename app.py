from flask import Flask,request,jsonify
from flask_restful import Api,Resource
from pymongo import MongoClient

app=Flask(__name__)
api=Api(app)

client = MongoClient("mongodb://localhost:27017")
db = client.cloud
clouds = db["clouds"]

class Add(Resource):
    def post(self):
        data = request.get_json()
        topic = data["topic"]
        security = data["security"]

        clouds.insert({
            "topic" : topic,
            "security" : security
        })

        ret = {
            "status": 200,
            "msg": "Added to DB"
        }

        return jsonify(ret)

class Show(Resource):
    def get(self):
        datas = clouds.find({})
        data=[]

        for x in datas:
            data.append({
                "security": x["security"],
                "topic": x["topic"]
                
            })

        

        return jsonify(data)


api.add_resource(Add,"/add")
api.add_resource(Show,"/show")



if __name__ == "__main__":
    app.run(debug=True)