console.log("¡Hola mundo!"); 
console.log("¡Hola chicas!");//Imprimir en consola

var num = 1;
let texto="Este es un texto"; //let -> SOLO existe en el bloque que se declara
const otroNum = 2; //const -> No pueden cambiarse
var decimales = 1.11; //flotantes
var bulian = true; //true o false

console.log(texto);

var despues; //declaro variable, aún no tiene valor. undefined
console.log(despues);
despues = "Texto colocado después";
console.log(despues);

var num1 = 1;
var num2 = 10;
var suma = num1 + num2; //suma = 1 + 10 = 11
console.log(suma);

var nombre = "Elena de Troya";
var mensaje = "Mi nombre es: ";
console.log(mensaje+nombre); //Concatenación

var otro_nombre = "Juana de Arco";
var edad = 18;
var mensaje_concatenado = "Mi nombre es: "+otro_nombre+" ¿cómo estás? Tengo "+edad+" años."; //Concatención
var mensaje_interpolado = `Mi nombre es: ${otro_nombre} ¿cómo estás? Tengo ${edad} años.`; //Interpolación
console.log(mensaje_concatenado); 
console.log(mensaje_interpolado);

var combinamosTexto = "ABC";
console.log(combinamosTexto + num1);
console.log(combinamosTexto + num1 + num2);
console.log(num1 + num2 + combinamosTexto);
console.log(num1 + num2 + combinamosTexto + num);

var orden = 10 + 20 / 6; //¿Qué valor tiene orden?
console.log(orden); // 1.- (), 2.- /*%, 3.- +-  
console.log(7%2); // sobrante en división = 1

var n = 14;
n += 5; // n = n + 5; Con cualquier operación
console.log(n);

var nombre_completo = "Pedro";
console.log(nombre_completo+nombre_completo+nombre_completo+nombre_completo);
nombre_completo += " Páramo"; //"Pedro" + " Páramo"
console.log(nombre_completo);

if(bulian) { // a === b; a !== b; a < b; a <= b; a > b; a >= b
    console.log("Variable verdadera");
} else {
    console.log("Variable falsa");
}

if(n >= 15){
    console.log("Número mayor a 15");
} else {
    console.log("Número menor a 15");
}

if(n < 15) {
    console.log("N es menor a 15");
}

var edad_infante = 4;
if(edad_infante < 2) {
    console.log("Es un bebe");
} else if(edad_infante < 5) {
    console.log("Es un toddler");
} else {
    console.log("Es un niño");
}

var temperatura = 20;
var estaLloviendo = false; //NO está lloviendo
if(temperatura >= 18/*t*/ && !estaLloviendo/*t*/) { // && ampersand -> AMBAS condicionales deben cumplirse
    console.log("Es un gran día para salir a pasear!");
}

if(estaLloviendo){ //estaLloviendo == true
    console.log("Lleva un paraguas en tu paseo");
}

if(!estaLloviendo){ //estaLloviendo == false 
    console.log("Las nubes estás despejadas");
}

var edad_conducir = 17;
var permisoPadres = true; //SI tiene permiso de los padres
if(edad_conducir >= 18/*f*/ || permisoPadres) { // || -> una u otra condicional debe cumplirse
    console.log("Puedes obtener tu licencia de conducir");
}

/* BUCLES/CICLOS */
/*
i = 0
Hola
Cómo estás?
----
i = 1
Hola
Cómo estás?
----
i = 2
Hola
Cómo estás?
----
i = 3
Hola
Cómo estás?
----
i = 4
*/
let a = "B";

for(let i=0; i < 4; i++) { /* for(inicializar; condicional; paso)  */
    console.log("Hola");
    console.log("¿Cómo estás?");
    let a = "A";
    console.log(a); // A
}
console.log(a); //B
//ya no existe i
//console.log(i); i solo existe en el bloque de código en el que la declaré

for(let i=3; i > 0; i--){
    console.log(i);
}

/*
x = 0
Entramos al while
x = 2
----
Entramos al while
x = 4
----
*/
let x = 0;
while(x < 3){
    console.log("Entramos al while");
    x += 2;
}

let inicio = 2;
let final = 10;
/*
inicio = 2
final = 10
Entramos al segundo while
inicio = 3
final = 8
---
Entramos al segundo while
inicio = 4
final = 6
---
Entramos al segundo while
inicio = 5
final = 4
---
*/
while(inicio < final) {
    console.log("Entramos al segundo while");
    inicio++;
    final -= 2;
}

// == ===

var variable1 = 1; //num
var variable2 = "1"; //string

if(variable1 == variable2) { // == -> buscando que los valores sean iguales
    console.log("Tiene el mismo valor");
}

if(variable1 === variable2) { // === -> mismo valor y mismo tipo
    console.log("Tienen el mismo valor Y el mismo tipo");
}

console.log(variable1+variable2);

// Sigma -  Escribe código que sume todos los valores del 1 al 100 en una variable sum y, al final, console.log dé como resultado 1 + 2 + 3 + ... + 98 + 99 + 100. Deberíamos obtener 5050 al final.

//Sigma pares e impares - Escribe código que sume los valores pares del 1 al 100 en una variable suma_pares y valores impares en una variable suma_impares. Intenta hacer UN solo bucle. % -> mod. 5%2 
