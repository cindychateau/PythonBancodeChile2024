//API = Application Programming Interfaces
//AJAX = Asynchronous Javascript and XML

/* PROMESAS */
function muestra_perrito() {
    fetch("https://dog.ceo/api/breeds/image/random")
        .then(response => response.json())
        .then(data => {
            /*
            data = {
                "message": "url/img.jpg",
                "status": "success"
            }
            */
           
            console.log(data);
            // data["message"] o data.message
            let img_perrito = `<img alt="perrito" src="${data.message}" >`;
            let img_otra = "<img alt='perrito' src='"+data.message+"'>";
            
            document.querySelector(".imagen-perrito").innerHTML = img_perrito;
        });
}

/*
parametros => codigo
*/

/* ASYNC/AWAIT */
async function muestra_perritoAsync() {
    let response = await fetch("https://dog.ceo/api/breeds/image/random");
    let data = await response.json();
    /*
    data = {
        "message": "url/img.jpg",
        "status": "success"
    }
    */
    let img_perrito = `<img alt="perrito" src="${data.message}" >`;
    document.querySelector(".imagen-perrito").innerHTML = img_perrito;
}