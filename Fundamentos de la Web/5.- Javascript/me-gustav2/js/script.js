var contador1 = 9;
var contador2 = 12;
var contador3 = 9;

function like_1() {
    contador1++;
    var cantidad = document.querySelector('#cantidad1');
    cantidad.innerText = contador1;
}

function like_2() {
    contador2++;
    var cantidad = document.querySelector('#cantidad2');
    cantidad.innerText = contador2;
}

function like_3(){
    contador3++;
    var cantidad = document.querySelector('#cantidad3');
    cantidad.innerText = contador3;
}

function like(num) {
    var cantidad = document.querySelector('#cantidad'+num);
    var nueva_cantidad = parseInt(cantidad.innerText); //"9"  Convierto en entero
    nueva_cantidad++;
    cantidad.innerText = nueva_cantidad;
}