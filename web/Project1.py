import os
from flask import Flask,jsonify,request
from flask_restful import Resource,Api
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")

db = client.aNewDB

userName = db["UserNum"]

userName.insert({
    'num_of_users':0
})

class visit(Resource):
    def get(self):
        previous_count = userName.find({})[0]['num_of_users']
        new_count = previous_count + 1
        userName.update({},{"$set":{'num_of_users':new_count}})
        return str("Hello User ..." + str(new_count))



def checkpostdata(postData,functionname):
    if (functionname == 'add' or functionname == 'subtract' or functionname == 'multiply' or functionname == 'division'):
        if 'x' not in postData or 'y' not in postData:
            return 301
        elif (functionname == 'division' and postData['y']==0):
            return 302
        else:
            return 200


class Add(Resource):
    def post(self):
        postData = request.get_json()
        status_code = checkpostdata(postData,'add')
        if (status_code != 200):
            retJson ={
                "Mesage": "An Error happend",
                "Status Code":status_code
            }
            return jsonify(retJson)

        x= postData['x']
        y= postData['y']
        x= int(x)
        y= int(y)
        result = x+y
        JsonRect ={
            "Message": result,
            "Status Code": 200
        }
        return jsonify(JsonRect)



class Subtract(Resource):
    def post(self):
        postData = request.get_json()
        status_code = checkpostdata(postData,'subtract')
        if (status_code != 200):
            retJson ={
                "Mesage": "An Error happend",
                "Status Code":status_code
            }
            return jsonify(retJson)

        x= postData['x']
        y= postData['y']
        x= int(x)
        y= int(y)
        result = x-y
        JsonRect ={
            "Message": result,
            "Status Code": 200
        }
        return jsonify(JsonRect)



class Multiply(Resource):
        def post(self):
            postData = request.get_json()
            status_code = checkpostdata(postData,'multiply')

            if (status_code != 200):
                retJson ={
                    "Mesage": "An Error happend",
                    "Status Code":status_code
                }
                return jsonify(retJson)

            x= postData['x']
            y= postData['y']
            x= int(x)
            y= int(y)
            result = x*y
            JsonRect ={
                "Message": result,
                "Status Code": 200
            }
            return jsonify(JsonRect)


class Division(Resource):
            def post(self):
                postData = request.get_json()
                status_code = checkpostdata(postData,'division')

                if (status_code != 200):
                    retJson ={
                        "Mesage": "An Error happend",
                        "Status Code":status_code
                    }
                    return jsonify(retJson)

                x= postData['x']
                y= postData['y']
                x= int(x)
                y= int(y)
                result = (x*1.0)/y
                JsonRect ={
                    "Message": result,
                    "Status Code": 200
                }
                return jsonify(JsonRect)

api.add_resource(Add,'/add')
api.add_resource(Subtract,'/subtract')
api.add_resource(Multiply,'/multiply')
api.add_resource(Division,'/division')
api.add_resource(visit,'/hello')



if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
