 <h1>RESTful API - Exercises</h1>
 
This repository contains an assignement of Module 3 (“Secure Software Development”) Unit 9 ( Developing an API for a Distributed Environment) of my MSc in Computer Science at the University of Essex, UK. This is an exercise to create a RESTful API using Python Flask. Click [here](https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3) to find the Source Code. 
 
:round_pushpin:The file [main.py](https://github.com/alicevillar/restful_api_exercise/blob/main/main.py) contains the code.  I decided to go further so in the file [api_fetch.js](https://github.com/alicevillar/restful_api_exercise/blob/main/api_fetch.js) I did the HTTP requests for each method (get, post, put and delete) with Javascript.
  

<h1>Table of Contents</h1>
 
<!-- TOC -->
- [1. Question 1](#1-question-1)
- [2. Question 2](#2-question-2)
- [1. Question 3](#3-question-3)
- [2. Question 4](#4-question-4)

<!-- TOC -->


## Question 1  

#### :arrow_forward: Run the API.py code. Take a screenshot of the terminal output. What command did you use to compile and run the code?

I used Pythin in Pycharm, so I just executed the code and accessed the command line (also known as terminal). What happened was an error message saying: get() missing one positional argument. Click [here](https://github.com/alicevillar/restful_api_exercise/blob/main/type_error.JPG) to see the print screen. To fix this error I only had to insert the missing argument in the function add_resorce, which now looks like this: 

 
 ```
api.add_resource(User,"/user/<string:name>")
```
## Question 2  

#### :arrow_forward:  Run the following command at the terminal prompt: w3m http://127.0.0.1:5000/user/Ann What happens when this command is run, and why?

This command has the final positional argument for the get function, so it returns a dictionary with Ann's information:
 

```
{
    "name": "Ann",
    "age": 32,
    "occupation": "Doctor"
}
```

## Question 3   

#### :arrow_forward: Run the following command at the terminal prompt: w3m http://127.0.0.1:5000/user/Adam What happens when this command is run, and why?

Adam does not exist in the list or users, so the command will the result will be " null" . I will have the following response in the console: 404 (NOT FOUND). I also did the request in Javascript:
```
// FUNCTION METHOD GET
//Fetch to GET User Adam. Since Adam does not exist, the expected response is 404

fetch("http://127.0.0.1:5000/user/Adam").then(  
async(response) => {  
    const data = await response.json();  
    console.log(data)
}
) 
```
 ===>>> RESPOSE IN THE CONSOLE: 404 (NOT FOUND)
 
## Question 4

#### :arrow_forward: What capability is achieved by the flask library?

Flask is a widely used micro web framework for creating APIs in Python. Flask's framework is more explicit than Django's framework and is also easier to learn because it has less base code to implement a simple web-Application. Flask comes with all its benefit of the fast template, strong WSGI features, and extensive documentation. It is important to highlight the capabilities of Flask-RESTful and Flask-RestPlus: 

* Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs. It is a lightweight abstraction that works with your existing ORM/libraries. 
* Flask-RESTPlus is an extension to Flask which improves upon its capabilities. Flask-RestPlus provides syntaxic suger (makes programs easier to read, write, or understand) and automatically generates Swagger documentation on top of Flask-Restful.


