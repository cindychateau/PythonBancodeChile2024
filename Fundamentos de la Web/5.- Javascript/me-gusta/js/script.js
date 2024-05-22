var contador = 0;

function like() {
    contador++; //contador = contador +1;
    //output = <strong id="cantidad">0</strong> 
    let output = document.querySelector("#cantidad");
    //.innerText -> texto
    //.textContent -> texto
    //.innerHTML -> acepta etiquetas
    output.textContent = contador;
}