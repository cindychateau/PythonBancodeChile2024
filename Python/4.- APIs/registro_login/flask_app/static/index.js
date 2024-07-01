let form_login = document.querySelector("#form-login");
form_login.onsubmit = function(event) {
    //event = evento que estoy escuchando por defecto.
    event.preventDefault(); //Prevenimos comportamiento por default

    //Obteniendo todos los datos del formulario
    let formulario = new FormData(form_login);
    /*
    formulario = {
        "email": "elena@cd.com",
        "password": "1234"
    }
    */

    fetch("/login", {method: "POST", body: formulario})
        .then(response => response.json())
        .then(data => {
            if(data.message == "success") {
                window.location.href = "/dashboard";
            } else {
                let mensajes_alerta = document.querySelector('.mensajes-alerta');
                mensajes_alerta.innerHTML = data.message;
                mensajes_alerta.classList.add("alert");
                mensajes_alerta.classList.add("alert-danger");
            }
        })
}