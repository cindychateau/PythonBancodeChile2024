/*
Función: Bloque de código al que nombramos y al que podemos llamar/invocar las veces que yo necesite

function nombre_funcion(parametros1, parametro2...) {
    //Código
    return valor/variable
}

*/

function saludo() {
    console.log("Hola");
    console.log("¿Cómo estás?");
}

saludo();
saludo();
saludo();
saludo();

//nombre = "Juana"
function saludo_nombre(nombre) { //let
    console.log(`¡Hola ${nombre}!`);
}

saludo_nombre("Elena");
saludo_nombre("Juana");

//nombre = "Elena", apellido = "De Troya"
function saludo_especial(nombre, apellido) {
    console.log(`¡Hola ${nombre} ${apellido}!`);
}

saludo_especial("Elena", "De Troya");

//num1 = 10, num2 = 20
//<- 30
function sumatoria(num1, num2) {
    return num1 + num2;
}

var resultado = sumatoria(10, 20); //resultado = 30
console.log(resultado*2);
console.log(sumatoria(5, 2));

function bucle(num) {
    for(let i=0; i<num; i++){
        return i; //sales de función
    }
}
