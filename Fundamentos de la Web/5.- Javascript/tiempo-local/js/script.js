alert("Cargando Reporte del Clima");

function eliminar_cookies() {
    let pie_de_pagina = document.querySelector("footer");
    pie_de_pagina.remove(); //Elmina el elemento
}

function eliminar(elemento) {
    elemento.remove();
}

function cambiar_temperatura(elemento) {
    //elemento = <a href="#" onclick="cambiar_temperatura(this)">Buenos Aires</a>
    //ciudad = Buenos Aires
    let ciudad = elemento.innerText;
    console.log(ciudad);

    //.innerText -> texto interno
    let h2_ciudad = document.querySelector("#titulo_ciudad");
    h2_ciudad.innerText = ciudad;
}