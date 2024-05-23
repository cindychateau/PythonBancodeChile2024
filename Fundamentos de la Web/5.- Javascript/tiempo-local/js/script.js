alert("Cargando Reporte del Clima");

const temperatures = {
    BuenosAires: ["22C 15C", "23C 28C", "21C 23C", "14C 18C", "12C 15C"],
    CiudadDeMexico: ["23C 15C", "24C 28C", "23C 23C", "14C 18C", "10C 15C"],
    Santiago: ["24C 15C", "25C 28C", "21C 24C", "14C 13C", "16C 15C"],
    SaoPaulo: ["25C 15C", "26C 28C", "21C 26C", "13C 18C", "19C 15C"],
    Quito: ["26C 15C", "27C 28C", "21C 28C", "11C 18C", "18C 15C"],
} //ACÁ tenemos un objeto con nuestras temperaturas si?

function eliminar_cookies() {
    let pie_de_pagina = document.querySelector("footer");
    pie_de_pagina.remove(); //Elmina el elemento
}

function eliminar(elemento) {
    elemento.remove();
}

function cambiar_temperatura(elemento, ciudadSelect) {
    //elemento = <a href="#" onclick="cambiar_temperatura(this)">Buenos Aires</a>
    //ciudad = Buenos Aires
    let ciudad = elemento.innerText;
    console.log(ciudad);

    //.innerText -> texto interno
    let h2_ciudad = document.querySelector("#titulo_ciudad");
    h2_ciudad.innerText = ciudad;

    //SELECCIONAMOS todoo los campos de temperaturas:
    let temperaturas = document.querySelectorAll(".temperatura_label");
    //VAMOS A VERLAS EN CONSOLA
    console.log(temperaturas);
    console.log(temperatures[ciudadSelect]);//ESTO SERIA LAS TEMPERATURAS SELECCIONADAS DEL OBJETO DE TEMPERATURAS,SI?
    temperaturas.forEach((temp, indice) => {
        console.log(temp);
        temp.innerText = temperatures[ciudadSelect][indice];
        //Selecciona la ciudad correspondiente y lo hace indice por indice 
    })

}
