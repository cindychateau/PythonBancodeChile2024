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
for(let i=0; i < 4; i++) {
    console.log("Hola");
    console.log("¿Cómo estás?");
}
