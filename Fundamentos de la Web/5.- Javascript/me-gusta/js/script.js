

function like(tag) {
    //output = <strong id="cantidad">0</strong> 
    let output = document.querySelector(`#${tag}`);
    let contador=parseInt(output.textContent);
    contador+=1;
    //.innerText -> texto
    //.textContent -> texto
    //.innerHTML -> acepta etiquetas
    output.textContent = contador;
}