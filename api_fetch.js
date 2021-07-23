


// FUNCTION METHOD GET


//Fetch to GET User Adam. Since Adam does not exist, the expected response is 404

fetch("http://127.0.0.1:5000/user/Adam").then( // then diz: quando a promessa for encaminhada vai fazer a funcao do then
async(response) => { // funcao async é a função que faz o await 
    const data = await response.json(); //o cod vai travar aqui até o response vir
    console.log(data)
}
) 
/*
RESPOSE IN THE CONSOLE: 

404 (NOT FOUND)

*/
 

//Fetch to GET User Ann. Since Ann does exist, the expected response is a dictionary with Ann's information 
fetch("http://127.0.0.1:5000/user/Ann").then(
async(response) => {
    const data = await response.json(); //o cod vai travar aqui até o response vir
    console.log(data)
}
) 

/*
  response --> 
  
  {
    "name": "Ann",
    "age": 32,
    "occupation": "Doctor"
}
*/


 // FUNCTION METHOD PUT: creates a user if it does not exist it updates user's data

const info_user = new FormData()
// payload
info_user.append("age","90")
info_user.append("occupation","retired")

fetch("http://127.0.0.1:5000/user/Matheus",{
    method: "PUT",
    body: info_user,
    redirect: "follow"
}).then(
    async(response) => {
        const server_response = await response.json()
        console.log(server_response)
    }
)
/*
RESPOSE =>> {name: "Matheus", age: "90", occupation: "retired"}
*/

 

 // FUNCTION METHOD POST: creates a user if it does not exist it returns: "User with name {} already exists"

 //const info_user = new FormData()
 // payload
 info_user.append("age","90")
 info_user.append("occupation","retired")
 
 fetch("http://127.0.0.1:5000/user/Ann",{
     method: "POST",
     body: info_user,
     redirect: "follow"
 }).then(
     async(response) => {
         const server_response = await response.json()
         console.log(server_response)
     }
 )
 
/*
RESPOSE IN THE CONSOLE: 

POST http://127.0.0.1:5000/user/Ann 400 (BAD REQUEST)
VM77:11 User with name Ann already exists
*/

 // FUNCTION METHOD DELETE - deleting user Jason 


 fetch("http://127.0.0.1:5000/user/Jason", {method: "DELETE"}) 
 .then(async(response) => {  
     const data = await response.json(); //o cod vai travar aqui até o response vir
     console.log(data)
 
 }) 

 /*
RESPOSE IN THE CONSOLE: 

Jason is deleted.
*/

// FUNCTION METHOD GET to Jason just to check if this user has really been deleted

fetch("http://127.0.0.1:5000/user/Jason").then( // then diz: quando a promessa for encaminhada vai fazer a funcao do then
async(response) => { // funcao async é a função que faz o await
    const data = await response.json(); //o cod vai travar aqui até o response vir
    console.log(data)
}
) 
 /*
RESPOSE IN THE CONSOLE: 
null
*/
 
// Response is null, which means the delete method worked :) 