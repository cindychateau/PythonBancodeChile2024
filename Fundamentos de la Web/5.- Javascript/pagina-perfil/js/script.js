console.log("¡Entramos a la página!");

function alerta() {
    alert("Hiciste click en profile");
    console.log("El usuario hizo click en el título Profile");
}

//elemento = <a href="#" onclick="eliminar(this)" >View More</a>
/* this se refiere al elemento con el cual estoy interactuando */
function eliminar(elemento) {
    elemento.remove();
}

//elemento = <a href="#" onclick="cambiar_texto(this)">Home</a>
function cambiar_texto(abc1) {
    //innerText -> texto interno
    abc1.innerText = "Texto distinto";
}

function cambia_imagen(elemento_img) {
    elemento_img.src = "images/todd-s.jpg";
}

function regresa_imagen(elemento_img) {
    //src -> la ruta de la imagen
    elemento_img.src = "images/jane-m.jpg";
}

function editar_perfil() {
    //querySelector -> seleccionar cualquier elemento de mi documento HTML, usando selectores
    
    //.getElementById("identificador")
    var elemento_nombre = document.querySelector("#nombre");
    elemento_nombre.innerText = "Cynthia Castillo";

    //.getElementByClassname("clase")
    var lugar = document.querySelector('.lugar');
    lugar.innerText = "Monterrey";
    //.style -> cambia estilos
    //.propiedadACambiar
    lugar.style.color = "purple";
    //.lugar { text-transform: "uppercase" }
    lugar.style.textTransform = "uppercase";

    var parrafito = document.querySelector(".card-body p"); //Primer párrafo
    //innerHTML -> ingresar texto+etiquetas
    parrafito.innerHTML = "Desarrolladora, Instructora de Programación <br> Mamá gatuna";

    //.querySelectorAll -> Lista/array
    /*
    var parrafos = document.querySelectorAll('.card-body p');
    parrafos[0] = primerparrafo;
    parrafos[1] = segundoparrafo;
    */

}

function cambiar_mode() {
    var elemento_body = document.querySelector("body");
    //classList -> array con las clases que tiene mi elemento

    if(elemento_body.classList.contains("dark-mode")) {
        elemento_body.classList.remove("dark-mode");
    } else {
        elemento_body.classList.add("dark-mode");
    }

    
}