// Conversión de centímetros a metros
let h = h / 100;

// Determinamos el valor de los catetos según las propiedades de un triángulo isósceles
let c = h / Math.sqrt(2);

// Planteamos las condiciones de equilibrio Σfx = 0 ; Σfy = 0

// Fuerzas que actúan en la carga de referencia
let f21 = (k * q2 * q1) / (c ** 2);
let f31 = (k * q3 * q1) / (h ** 2);

// Descomponemos las fuerzas
let f21x = f21 * Math.cos((90 * Math.PI) / 180); // Dada la geometría del problema, esta componente siempre será 0.

// Asignamos dirección a cada una de las fuerzas
let f21y;
if (p1 === "+" && p2 === "+") {
  f21y = f21 * Math.sin((90 * Math.PI) / 180);
} else if (p1 === "+" && p2 === "-") {
  f21y = -f21 * Math.sin((90 * Math.PI) / 180);
} else if (p1 === "-" && p2 === "+") {
  f21y = -f21 * Math.sin((90 * Math.PI) / 180);
} else if (p1 === "-" && p2 === "-") {
  f21y = f21 * Math.sin((90 * Math.PI) / 180);
}

// Para f31
let f31x, f31y;
if (p1 === "+" && p3 === "+") {
  f31x = -f31 * Math.cos((45 * Math.PI) / 180);
  f31y = f31 * Math.sin((45 * Math.PI) / 180);
} else if (p1 === "+" && p3 === "-") {
  f31x = f31 * Math.cos((45 * Math.PI) / 180);
  f31y = -f31 * Math.sin((45 * Math.PI) / 180);
} else if (p1 === "-" && p3 === "+") {
  f31x = f31 * Math.cos((45 * Math.PI) / 180);
  f31y = -f31 * Math.sin((45 * Math.PI) / 180);
} else if (p1 === "-" && p3 === "-") {
  f31x = -f31 * Math.cos((45 * Math.PI) / 180);
  f31y = f31 * Math.sin((45 * Math.PI) / 180);
}

let sumax = f21x + f31x;
let sumay = f21y + f31y;
let resultante = Math.sqrt(sumax ** 2 + sumay ** 2);

// Ángulo de la resultante
let x = Math.atan(sumay / sumax);
let grados = (x * 180) / Math.PI;

// Calculamos la dirección de la resultante con respecto al eje X
let angulo;
if (sumax < 0 && sumay > 0) {
  angulo = 180 + grados;
} else if (sumax < 0 && sumay < 0) {
  angulo = 180 + grados;
} else if (sumax > 0 && sumay < 0) {
    angulo = 360 + grados;
}

console.log("componentes de la F: "+"("+sumax+","+sumay+")");
console.log("fuerza resultante: "+resultante);
console.log("fuerza con angulo: "+angulo);
