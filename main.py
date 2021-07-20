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
 
    def get(self, name): #precisa passar um argument name. nao passou, entao deu erro
        for user in users:
            if (name == user["name"]):
                return user, 200
 
    # função só para testar p/ ver se a api está funcionando
    #def get(self):
        #return users, 200

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
# verifica se o usuário inserido já existe.
        for x in users:
            if (name == x["name"]):
                return "User with name {} already exists".format(name), 400

# aqui vem o ELSE. Ou seja, se o user não existe, então é preciso criá-lo
        # para criar o usuário, usa a variável user, que recebe um dicionário com todos os argumentos do usuário
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201
# vai fazer o mesmo q no post e depois vai fazer um for p/ver se o nome já exite.
    #se já existe vai atualizar os dados
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        # faz um for para encontrar o usuário. Se encontrou, atualiza dos dados
        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        # aqui vem o ELSE. Ou seja, se não encontrou então cria o usuário e coloca na variável user.
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
# a,b,c,d,. Quero deletar o A. Daí, verifico procurando A na lista. Tudo o que não for A, entra na lista nova.
        #ou seja, a lista nova não vai contar o A, que portanto terá sido deletado.
        #Outra forma de escrever isso:
# varrendo usuário por usuário pelo for e vai inserir os dados se o nome do usuário for diferent
        return "{} is deleted.".format(name), 200

        #return f"{name} is deleted", 200

api.add_resource(User,"/user/<string:name>") 

app.run(debug=True)

'''  
elementos = []
for el in users:
    if el["name"] != name:
        elementos.append(el)

users = elementos
'''
