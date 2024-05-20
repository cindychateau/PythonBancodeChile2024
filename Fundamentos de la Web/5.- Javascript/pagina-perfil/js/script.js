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