


// FUNCTION METHOD GET

 
 

//GET Adam
fetch("http://127.0.0.1:5000/user/Adam").then( // then diz: quando a promessa for encaminhada vai fazer a funcao do then
async(response) => { // funcao async é a função que faz o await 
    const data = await response.json(); //o cod vai travar aqui até o response vir
    console.log(data)
}
) 

// response --> 404 (NOT FOUND)

//GET Ann
fetch("http://127.0.0.1:5000/user/Ann").then(
async(response) => {
    const data = await response.json(); //o cod vai travar aqui até o response vir
    console.log(data)
}
) 

 // response --> {name: "Ann", age: 32, occupation: "Doctor"}



 // FUNCTION METHOD PUT

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

 // FUNCTION METHOD POST


 
 // FUNCTION METHOD DELETE


