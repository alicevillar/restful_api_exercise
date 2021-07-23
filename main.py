from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "James",
        "age": 30,
        "occupation": "Network Engineer"
    },
    {
        "name": "Ann",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jason",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class User(Resource):
 
    def get(self, name): # it is necessary to give the argument for the name.
        for user in users:
            if (name == user["name"]):
                return user, 200


    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
        # check to see if the user inserted already exists
        for x in users:
            if (name == x["name"]):
                return "User with name {} already exists".format(name), 400

        # here is the ELSE. Thus, if user does not exist, he or she must be created
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        # check if user exists. If it does exist, then it updates the data
        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        # here is the ELSE. If user is not found, has to be created and put in this variable
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201 # status HTTP "201 Created"

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        # Ex.: imagine we have users A,B,C,D,. I want to delete user A. I search for A in the list.
        # The new list will have all the users exepct from user A. Boom! A was deleted :)

        return "{} is deleted.".format(name), 200
        #another way to do this: return f"{name} is deleted", 200

api.add_resource(User,"/user/<string:name>")
app.run(debug=True)

'''  
Another way to do what is in line 76
elementos = []
for el in users:
    if el["name"] != name:
        elementos.append(el)

users = elementos
'''
