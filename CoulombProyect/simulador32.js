
 /* inicio */
 var inicio=document.querySelector("#inicio");
 /*inicio.addEventListener("click",function(){
     window.location.href="index.html";

 })*/

 function t_direccion(id1,id2,id3){ //funcion que evalua los radio button
    var dir;
    if(document.getElementById(id1).checked){
        dir="c1";
    }
    if(document.getElementById(id2).checked){
        dir="c2";
    }
    if(document.getElementById(id3).checked){
        dir="c3";
    }
    return dir;
}



function t_carga(id1,id2){ //funcion que evalua los radio button
    var signo;
    if(document.getElementById(id1).checked){
        signo="+";
    }
    if(document.getElementById(id2).checked){
        signo="-";
    }
    return signo;
}



 var k = 9e9;

function fuerzac1(q1,q2,q3,p1,p2,p3,dt){
    // Conversión de centímetros a metros
var h = dt / 100;
hip=h;
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
var resultante = Math.sqrt(sumax ** 2 + sumay ** 2);

// Ángulo de la resultante
var x = Math.atan(sumay / sumax);
var grados = (x * 180) / Math.PI;

// Calculamos la dirección de la resultante con respecto al eje X
var angulo = (x*180)/Math.PI;
if (sumax < 0 && sumay > 0) {
  angulo = 180 + grados;
} else if (sumax < 0 && sumay < 0) {
  angulo = 180 + grados;
} else if (sumax > 0 && sumay < 0) {
    angulo = 360 + grados;
}
/* 
console.log("componentes de la F: "+"("+sumax+","+sumay+")");
console.log("fuerza resultante: "+resultante);
console.log("fuerza con angulo: "+angulo);
console.log("cateto: "+c);
 */


return{
  cateto:c,
  fuerzax:sumax,
  fuerzay:sumay,
  fuerzar:resultante,
  angulo:angulo,
 
};
 }

 //2--------------------------------------------
function fuerzac2(q1,q2,q3,p1,p2,p3,dt){
    // Conversión de centímetros a metros
var h = dt / 100;
hip=h;
// Determinamos el valor de los catetos según las propiedades de un triángulo isósceles
var c = h / Math.sqrt(2);

// Planteamos las condiciones de equilibrio Σfx = 0 ; Σfy = 0

// Fuerzas que actúan en la carga de referencia
var f12 = (k * q1 * q2) / (c ** 2);
var f32 = (k * q3 * q2) / (c ** 2);

// Descomponemos las fuerzas
var f12x = f12 * Math.cos((90 * Math.PI) / 180); // Dada la geometría del problema, esta componente siempre será 0.
var f32y = f32 * Math.sin((0 * Math.PI) / 180); // Dada la geometría del problema, esta componente siempre será 0.

// Asignamos dirección a cada una de las fuerzas
var f12y;
if (p2 === "+" && p1 === "+") {
  f12y = -f12 * Math.sin((90 * Math.PI) / 180);
} else if (p2 === "+" && p1 === "-") {
  f12y = f12 * Math.sin((90 * Math.PI) / 180);
} else if (p2 === "-" && p1 === "+") {
  f12y = f12 * Math.sin((90 * Math.PI) / 180);
} else if (p2 === "-" && p1 === "-") {
  f12y = -f12 * Math.sin((90 * Math.PI) / 180);
}

// Para f32
var f32x;
if (p3 === "+" && p2 === "+") {
  f32x = -f32 * Math.cos((0 * Math.PI) / 180);
} else if (p3 === "+" && p2 === "-") {
  f32x = f32 * Math.cos((0 * Math.PI) / 180);
} else if (p3 === "-" && p2 === "+") {
  f32x = f32 * Math.cos((0 * Math.PI) / 180);
} else if (p3 === "-" && p2 === "-") {
  f32x = -f32 * Math.cos((0 * Math.PI) / 180);
}

var sumax = f12x + f32x;
var sumay = f12y + f32y;
var resultante = Math.sqrt(sumax ** 2 + sumay ** 2);

// Ángulo de la resultante
var x = Math.atan(sumay / sumax);
var grados = (x * 180) / Math.PI;

// Calculamos la dirección de la resultante con respecto al eje X
var angulo = (x * 180) / Math.PI;
if (sumax < 0 && sumay > 0) {
  angulo = 180 + grados;
} else if (sumax < 0 && sumay < 0) {
  angulo = 180 + grados;
} else if (sumax > 0 && sumay < 0) {
  angulo = 360 + grados;
}

/* console.log("ang"+angulo) */
return{
  cateto:c,
  fuerzax:sumax,
  fuerzay:sumay,
  fuerzar:resultante,
  angulo:angulo,
  
};


 }

 var hip=0;
 //3-------------------------------------
function fuerzac3(q1,q2,q3,p1,p2,p3,dt){
 
    // Conversión de centímetros a metros
var h = dt / 100;
hip=h;
// Determinamos el valor de los catetos según las propiedades de un triángulo isósceles
var c = h / Math.sqrt(2);

// Planteamos las condiciones de equilibrio Σfx = 0 ; Σfy = 0

// Fuerzas que actúan en la carga de referencia
var f13 = (k * q1 * q3) / (h ** 2);
var f23 = (k * q2 * q3) / (c ** 2);

// Descomponemos las fuerzas
var f23y = f23 * Math.cos((0 * Math.PI) / 180); // Dada la geometría del problema, esta componente siempre será 0.

// Asignamos dirección a cada una de las fuerzas
var f23x;
if (p2 === "+" && p3 === "+") {
  f23x = f23 * Math.cos((0 * Math.PI) / 180);
} else if (p2 === "+" && p3 === "-") {
  f23x = -f23 * Math.cos((0 * Math.PI) / 180);
} else if (p2 === "-" && p3 === "+") {
  f23x = -f23 * Math.cos((0 * Math.PI) / 180);
} else if (p2 === "-" && p3 === "-") {
  f23x = f23 * Math.cos((0 * Math.PI) / 180);
}

// Para f13
var f13x, f13y;
if (p1 === "+" && p3 === "+") {
  f13x = f13 * Math.cos((45 * Math.PI) / 180);
  f13y = -f13 * Math.sin((45 * Math.PI) / 180);
} else if (p1 === "+" && p3 === "-") {
  f13x = -f13 * Math.cos((45 * Math.PI) / 180);
  f13y = f13 * Math.sin((45 * Math.PI) / 180);
} else if (p1 === "-" && p3 === "+") {
  f13x = -f13 * Math.cos((45 * Math.PI) / 180);
  f13y = f13 * Math.sin((45 * Math.PI) / 180);
} else if (p1 === "-" && p3 === "-") {
  f13x = f13 * Math.cos((45 * Math.PI) / 180);
  f13y = -f13 * Math.sin((45 * Math.PI) / 180);
}

var sumax = f23x + f13x;
var sumay = f23y + f13y;
var resultante = Math.sqrt(sumax ** 2 + sumay ** 2);

// Ángulo de la resultante
var x = Math.atan(sumay / sumax);
var angulo = (x * 180) / Math.PI;

// Calculamos la dirección de la resultante con respecto al eje X
if (sumax < 0 && sumay > 0) {
  angulo = 180 + angulo;
} else if (sumax < 0 && sumay < 0) {
  angulo = 180 + angulo;
} else if (sumax > 0 && sumay < 0) {
  angulo = 360 + angulo;
}


return{
  cateto:c,
  fuerzax:sumax,
  fuerzay:sumay,
  fuerzar:resultante,
  angulo:angulo,

  
};


}

 

function CrearFlecha(angulo, Xfin, Yfin){//se crea la cabeza del vector
  var canvass=document.querySelector("#plano1 .canva2");
  canvass.width=1000;
  canvass.height=1000;
  let c=canvass.getContext("2d");
  if(angulo>=0 && angulo<22.5){
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-10,Yfin+10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-10,Yfin-10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
    
  }

  if(angulo>=22.5 && angulo<45){
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin,Yfin+10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-10,Yfin-5);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();  
  }

  if(angulo>=45 && angulo<67.5){
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+2,Yfin+10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-10,Yfin-5);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();  
  }
 
  
  if(angulo>=67.5 && angulo<90){
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+5,Yfin+10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-10,Yfin);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }

  if(angulo>=90 && angulo<112.5){
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-10,Yfin+10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+10,Yfin+10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }

  if(angulo>=112.5 && angulo<135){
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-6,Yfin+10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+17,Yfin+10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }

  if(angulo>=135 && angulo<157.5){ 
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+12,Yfin+3);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-5,Yfin+10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }
  
  if(angulo>=157.5 && angulo<180){ 
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+10,Yfin-10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+10,Yfin+10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }

  if(angulo>=180 && angulo<202.5){ 
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+10,Yfin-10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+10,Yfin+10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }

  if(angulo>=202.5 && angulo<225){ 
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+5,Yfin-11);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+10,Yfin+10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }

  if(angulo>=225 && angulo<247.5){
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin,Yfin-10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+10,Yfin);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }

  if(angulo>=247.5 && angulo<270){
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-4,Yfin-13);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+10,Yfin+5);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }

  if(angulo>=270 && angulo<292.5){
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-10,Yfin-10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+10,Yfin-10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }

  if(angulo>=292.5 && angulo<315){
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin+2,Yfin-10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-10,Yfin-2);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }

  
  if(angulo>=315 && angulo<337.5){
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-2,Yfin-10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-10,Yfin+5);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }

  if(angulo>=337.5 && angulo<360){
    c.beginPath();
    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-2,Yfin-10);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();

    c.moveTo(Xfin,Yfin);
    c.lineTo(Xfin-10,Yfin+5);
    c.strokeStyle = 'black';   
    c.lineWidth = 3;
    c.stroke();
  }


}

 function dibujoB(t_cargas1,t_cargas2,t_cargas3,ffuerza,posicion){

  var canvas=document.querySelector("#plano1 .canva1");
    
  canvas.width=1000;
  canvas.height=1000;

  var c=canvas.getContext("2d");

  var x=500;
  var y=500;

  var x1=x-200;
  var x2=x+200;

  var y1=y-200
  var y2=y+200;

  r=45;

  var dt=ffuerza.cateto*100;
  

    c.moveTo(x1,y1); //dibuja la linea entre cargas
    c.lineTo(x1,y2);
    c.lineTo(x2,y2);
    c.lineWidth=1;
    c.strokeStyle="black";
    c.stroke();

    

    //-------------

    /* dibuja las cargas */

    c.beginPath();
    c.arc(x1, y1, r, 0, 2 * Math.PI);
    c.fillStyle = 'red';
    c.fill();

    c.beginPath();
    c.arc(x1, y2, r, 0, 2 * Math.PI);
    c.fillStyle = 'red';
    c.fill();

    c.beginPath();
    c.arc(x2, y2, r, 0, 2 * Math.PI);
    c.fillStyle = 'red';
    c.fill();

    //--------------------------puntos
    function puntos(xpts,ypts){
      
      var desplazamiento=ypts-r-100;

      /* arriba */
      
      for(var i=ypts-r;i>=desplazamiento;i=i-10){
        c.beginPath();
        c.moveTo(xpts,i);
        c.lineTo(xpts,i-5);
        c.lineWidth=1;
        c.strokeStyle="black";
        c.stroke();
        }
      

      /* abajo */
      var desplazamiento=ypts+r+100;
      for(var i=ypts+r;i<=desplazamiento;i=i+10){
        c.beginPath();
        c.moveTo(xpts,i);
        c.lineTo(xpts,i+5);
        c.lineWidth=1;
        c.strokeStyle="black";
        c.stroke();
        }

      /* izquierda */
      desplazamiento=xpts-r-100;
      for(var i=xpts-r;i>=desplazamiento;i=i-10){
        c.beginPath();
        c.moveTo(i,ypts);
        c.lineTo(i-5,ypts);
        c.lineWidth=1;
        c.strokeStyle="black";
        c.stroke();
        }
    
      /* derecha */
      desplazamiento=xpts+r+100;
      for(var i=xpts+r;i<=desplazamiento;i=i+10){
        c.beginPath();
        c.moveTo(i,ypts);
        c.lineTo(i+5,ypts);
        c.lineWidth=1;
        c.strokeStyle="black";
        c.stroke();
        }
    }

    
    //---------fin puntos

  //console.log("hipotenusa:"+ hip);
   hip=hip*100;
  if(ffuerza.fuerzar>hip*3){
    console.log("hipotenusa de:"+ hip);
  } 

 if(posicion==1){
  
  var radians = (ffuerza.angulo) * (Math.PI / 180);
  var x_cartesiano = ffuerza.fuerzar * Math.cos(radians);
  var y_cartesiano = ffuerza.fuerzar * Math.sin(radians);
  var x_canvas = 300 + x_cartesiano;
  var y_canvas = 300 - y_cartesiano;
  var fuer2=ffuerza.fuerzar;

  console.log("X de canvas antes:"+ x_canvas);
  console.log("Y de canvas antes:"+ y_canvas);
  if(ffuerza.fuerzar<60){
    console.log("magnutud sin amplificar1:"+ffuerza.fuerzar)
    fuer2=fuer2+65;
  }

  if(x_canvas<0 || y_canvas<0){
    console.log("magnutud sin simplicar2:"+ffuerza.fuerzar);
    fuer2=300;
  }

  if(x_canvas>800 || y_canvas>800){
    console.log("magnutud sin simplicar:"+ffuerza.fuerzar);
    fuer2=300;
  }

  radians = (ffuerza.angulo) * (Math.PI / 180);
  x_cartesiano = fuer2 * Math.cos(radians);
  y_cartesiano = fuer2 * Math.sin(radians);
  x_canvas = 300 + x_cartesiano;
  y_canvas = 300 - y_cartesiano;

  //vector fuerza
    c.beginPath();
    c.moveTo(300,300);
    c.lineTo(x_canvas, y_canvas);
    c.strokeStyle = 'black';   
    c.lineWidth = 5;
    c.stroke();
    c.closePath();
    CrearFlecha(ffuerza.angulo,x_canvas,y_canvas);//para crear la flecha de la direccion del vector 
  
    //dibujar eje x
    c.beginPath();
    c.moveTo(300,300);
    c.lineTo(x_canvas,300);
    c.strokeStyle='orange';
    c.lineWidth=3;
    c.stroke();
    //flecha para eje x
    if(x_canvas>300){
      c.moveTo(x_canvas,300);
      c.lineTo(x_canvas-5,295);
      c.strokeStyle='orange';
      c.lineWidth=3;
      c.stroke();
      c.moveTo(x_canvas,300);
      c.lineTo(x_canvas-5,305);
      c.strokeStyle='orange';
      c.lineWidth=3;
      c.stroke();
    }
    else{
      c.moveTo(x_canvas,300);
      c.lineTo(x_canvas+5,295);
      c.strokeStyle='orange';
      c.lineWidth=3;
      c.stroke();
      c.moveTo(x_canvas,300);
      c.lineTo(x_canvas+5,305);
      c.strokeStyle='orange';
      c.lineWidth=3;
      c.stroke();

    }

    //dibujar eje y
    c.beginPath();
    c.moveTo(300,300);
    c.lineTo(300,y_canvas);
    c.strokeStyle='green';
    c.lineWidth=3;
    c.stroke();
    //flecha para eje y
    if(y_canvas<300){
      c.moveTo(300,y_canvas);
      c.lineTo(295,y_canvas+5);
      c.strokeStyle='green';
      c.lineWidth=3;
      c.stroke();
      c.moveTo(300,y_canvas);
      c.lineTo(305,y_canvas+5);
      c.strokeStyle='green';
      c.lineWidth=3;
      c.stroke();
    }
    else{
      c.moveTo(300,y_canvas);
      c.lineTo(305,y_canvas-5);
      c.strokeStyle='green';
      c.lineWidth=3;
      c.stroke();
      c.moveTo(300,y_canvas);
      c.lineTo(295,y_canvas-5);
      c.strokeStyle='green';
      c.lineWidth=3;
      c.stroke();

    }
    
    /*console.log(ffuerza.fuerzax);
    console.log(ffuerza.fuerzay);*/
    

  var a=ffuerza.angulo;
  var radio=50;
  
  c.beginPath();
  c.moveTo(300+r,300);
  c.lineTo(300+r+10,300)
  c.arc(300,300,radio,0 * Math.PI/180,-a * Math.PI/180,true);
  c.fillStyle="transparent"
  c.strokeStyle="black";


  c.fill();
  c.stroke();

  puntos(x1,y1);

}

if(posicion==2){

  var radians = (ffuerza.angulo) * (Math.PI / 180);
  var x_cartesiano = ffuerza.fuerzar * Math.cos(radians);
  var y_cartesiano = ffuerza.fuerzar * Math.sin(radians);
  var x_canvas = 300 + x_cartesiano;
  var y_canvas = 700 - y_cartesiano;
  var fuer2=ffuerza.fuerzar;
  if(ffuerza.fuerzar<60){
    console.log("magnutud sin amplificar1:"+ffuerza.fuerzar)
    fuer2=fuer2+65;
  }

  if(x_canvas<0 || y_canvas<0){
    console.log("magnutud sin simplicar2:"+ffuerza.fuerzar);
    fuer2=300;
  }

  if(x_canvas>800 || y_canvas>800){
    console.log("magnutud sin simplicar:"+ffuerza.fuerzar);
    fuer2=300;
  }

  var radians = (ffuerza.angulo) * (Math.PI / 180);
  var x_cartesiano = fuer2 * Math.cos(radians);
  var y_cartesiano = fuer2 * Math.sin(radians);
  var x_canvas = 300 + x_cartesiano;
  var y_canvas = 700 - y_cartesiano;
  //vector fuerza
  
  c.beginPath();
  c.moveTo(300,700);
  c.lineTo(x_canvas, y_canvas);
  c.strokeStyle = 'black';   
  c.lineWidth = 3;
  c.stroke();
  c.closePath();
  CrearFlecha(ffuerza.angulo,x_canvas,y_canvas);
 
  //dibujar eje x
  c.beginPath();
  c.moveTo(300,700);
  c.lineTo(x_canvas,700);
  c.strokeStyle='orange';
  c.lineWidth=3;
  c.stroke();
  //flecha para eje x
  if(x_canvas>300){
    c.moveTo(x_canvas,700);
    c.lineTo(x_canvas-5,695);
    c.strokeStyle='orange';
    c.lineWidth=3;
    c.stroke();
    c.moveTo(x_canvas,700);
    c.lineTo(x_canvas-5,705);
    c.strokeStyle='orange';
    c.lineWidth=3;
    c.stroke();
  }
  else{
    c.moveTo(x_canvas,700);
    c.lineTo(x_canvas+5,695);
    c.strokeStyle='orange';
    c.lineWidth=3;
    c.stroke();
    c.moveTo(x_canvas,700);
    c.lineTo(x_canvas+5,705);
    c.strokeStyle='orange';
    c.lineWidth=3;
    c.stroke();

  }

  //dibujar eje y
  c.beginPath();
  c.moveTo(300,700);
  c.lineTo(300,y_canvas);
  c.strokeStyle='green';
  c.lineWidth=3;
  c.stroke();
  //flecha para eje y
  if(y_canvas<700){
    c.moveTo(300,y_canvas);
    c.lineTo(295,y_canvas+5);
    c.strokeStyle='green';
    c.lineWidth=3;
    c.stroke();
    c.moveTo(300,y_canvas);
    c.lineTo(305,y_canvas+5);
    c.strokeStyle='green';
    c.lineWidth=3;
    c.stroke();
  }
  else{
    c.moveTo(300,y_canvas);
    c.lineTo(305,y_canvas-5);
    c.strokeStyle='green';
    c.lineWidth=3;
    c.stroke();
    c.moveTo(300,y_canvas);
    c.lineTo(295,y_canvas-5);
    c.strokeStyle='green';
    c.lineWidth=3;
    c.stroke();

  } 
  

  
  //dibujo del angulo

  var a=ffuerza.angulo;
  var radio=50;
  
  c.beginPath();
  c.moveTo(300+r,700);
  c.lineTo(300+r+10,700)
  c.arc(300,700,radio,0 * Math.PI/180,-a * Math.PI/180,true);
  c.fillStyle="transparent"
  c.strokeStyle="black";
  c.fill();
  c.stroke();
  puntos(x1,y2);

}

if(posicion==3){

  puntos(x2,y2);
  var radians = (ffuerza.angulo) * (Math.PI / 180);
  var x_cartesiano = ffuerza.fuerzar * Math.cos(radians);
  var y_cartesiano = ffuerza.fuerzar * Math.sin(radians);
  var x_canvas = 700 + x_cartesiano;
  var y_canvas = 700 - y_cartesiano;
  var fuer2=ffuerza.fuerzar;
  if(ffuerza.fuerzar<60){
    console.log("magnutud sin amplificar1:"+ffuerza.fuerzar)
    fuer2=fuer2+65;
  }

  if(x_canvas<0 || y_canvas<0){
    console.log("magnutud sin simplicar2:"+ffuerza.fuerzar);
    fuer2=300;
  }

  if(x_canvas>800 || y_canvas>800){
    console.log("magnutud sin simplicar:"+ffuerza.fuerzar);
    fuer2=300;
  }
  var radians = (ffuerza.angulo) * (Math.PI / 180);
  var x_cartesiano = fuer2 * Math.cos(radians);
  var y_cartesiano = fuer2 * Math.sin(radians);
  var x_canvas = 700 + x_cartesiano;
  var y_canvas = 700 - y_cartesiano;
  //vector fuerza
  
  c.beginPath();
  c.moveTo(700,700);
  c.lineTo(x_canvas, y_canvas);
  c.strokeStyle = 'black';   
  c.lineWidth = 3;
  c.stroke();
  c.closePath();
  CrearFlecha(ffuerza.angulo,x_canvas,y_canvas);
  
  //dibujar eje x
  c.beginPath();
  c.moveTo(700,700);
  c.lineTo(x_canvas,700);
  c.strokeStyle='orange';
  c.lineWidth=3;
  c.stroke();
  //flecha para eje x
  if(x_canvas>700){
    c.moveTo(x_canvas,700);
    c.lineTo(x_canvas-5,695);
    c.strokeStyle='orange';
    c.lineWidth=3;
    c.stroke();
    c.moveTo(x_canvas,700);
    c.lineTo(x_canvas-5,705);
    c.strokeStyle='orange';
    c.lineWidth=3;
    c.stroke();
  }
  else{
    c.moveTo(x_canvas,700);
    c.lineTo(x_canvas+5,695);
    c.strokeStyle='orange';
    c.lineWidth=3;
    c.stroke();
    c.moveTo(x_canvas,700);
    c.lineTo(x_canvas+5,705);
    c.strokeStyle='orange';
    c.lineWidth=3;
    c.stroke();

  }

  //dibujar eje y
  c.beginPath();
  c.moveTo(700,700);
  c.lineTo(700,y_canvas);
  c.strokeStyle='green';
  c.lineWidth=3;
  c.stroke();
  //flecha para eje y
  if(y_canvas<700){
    c.moveTo(700,y_canvas);
    c.lineTo(695,y_canvas+5);
    c.strokeStyle='green';
    c.lineWidth=3;
    c.stroke();
    c.moveTo(700,y_canvas);
    c.lineTo(705,y_canvas+5);
    c.strokeStyle='green';
    c.lineWidth=3;
    c.stroke();
  }
  else{
    c.moveTo(x_canvas,700);
    c.lineTo(x_canvas+5,695);
    c.strokeStyle='green';
    c.lineWidth=3;
    c.stroke();
    c.moveTo(x_canvas,700);
    c.lineTo(x_canvas+5,705);
    c.strokeStyle='green';
    c.lineWidth=3;
    c.stroke();

  }

  //dibujo del angulo

  var a=ffuerza.angulo;
  var radio=50;
  
  c.beginPath();
  c.moveTo(x2+r,y2);
  c.lineTo(x2+r+10,y2)
  c.arc(x2,y2,radio,0 * Math.PI/180,-a * Math.PI/180,true);
  c.fillStyle="transparent"
  c.strokeStyle="black";


  c.fill();
  c.stroke();
  puntos(x2,y2);

}

return{
  x:x,
  y:y,
  x1:x1,
  x2:x2,
  y1:y1,
  y2:y2,
  r:r,
}




}
function posangulo(px,py,angulo,rad){
      
  var ax;
  var ay;
  if(angulo==0){//
    ax=px+rad+5;
    ay=py-28;
  }
  if(angulo>0 && angulo<=30){//
    ax=px+rad+15;
    ay=py-30;
  }
  if(angulo>30 && angulo<=60){//
    ax=px+rad+5;
    ay=py-35;
  }
  if(angulo>60 && angulo<90){//
    ax=px+rad;
    ay=py-65;
  }
  if(angulo==90){//
    ax=px-3;
    ay=py-70;
  }
  if(angulo>90 && angulo<=120){//
    ax=px+10;
    ay=py-80;
  }
  if(angulo>120 && angulo<150){
    ax=px+40;
    ay=py-65;
  }
  if(angulo>150 && angulo<180){//
    ax=px-39;
    ay=py-73;
  }
  if(angulo==180){
    ax=px+rad+5;
    ay=py-5;
  }
  if(angulo>180 && angulo<=210){
    ax=px+rad+5;
    ay=py-25;

  }
  if(angulo>210 && angulo<=240){
    ax=px+rad+5;
    ay=py-25;

  }
  if(angulo>240 && angulo<270){//
    ax=px-rad-12;
    ay=py+30;

  }
  if(angulo==270){
    ax=px-5;
    ay=py+65;
  }
  if(angulo>270 && angulo<=300){//
    ax=px-20;
    ay=py+50;

  }
  if(angulo>300 && angulo<=330){
    ax=px+rad+5;
    ay=py-25;

  }
  if(angulo>330 && angulo<360){//
    ax=px+rad-5;
    ay=py+30;

  }
  if(angulo==360){
    ax=px+rad+5;
    ay=py+10;

  }
  console.log("ang: "+angulo);
  return {
    ax:ax,
    ay:ay,
  }

}

function llenar(vq1,vq2,vq3,t_cargas1,t_cargas2,t_cargas3,ffuerza,poss,posicion){

  var convertirx=(poss.x).toString() + "px";
    var convertiry3 =(poss.y).toString() + "px";
    var convertiry2 =(poss.x1).toString() + "px";
    var convertirx1 =(poss.y1).toString() + "px";
    var convertirx2 =(poss.x2).toString() + "px";
    var convertirx2 =(poss.y2).toString() + "px";

    /* distancias */
    var span_dt=document.querySelector("#plano1 .span3");
    span_dt.innerHTML=((ffuerza.cateto).toFixed(3)).toString() +"m";
    span_dt.style.top="500px";
    span_dt.style.left="250px";

    var span_dt=document.querySelector("#plano1 .span4");
    span_dt.innerHTML=((ffuerza.cateto).toFixed(3)).toString() +"m";
    span_dt.style.top="710px";
    span_dt.style.left="500px";


    /* polaridades */

    var span_t1=document.querySelector("#plano1 .span5");
    span_t1.innerHTML=t_cargas1;
    span_t1.style.top=(poss.x1-poss.r).toString() + "px";
    span_t1.style.left=(poss.y1-poss.r).toString() + "px";
    if(t_cargas1=="+"){
        span_t1.style.backgroundColor="#ff0e0e"
    }else{
        span_t1.style.backgroundColor="#0e6dff"
    }
    /* polaridad2 */
    var span_t1=document.querySelector("#plano1 .span6");
    span_t1.innerHTML=t_cargas2;
    span_t1.style.top=(poss.x2-poss.r).toString() + "px";
    span_t1.style.left=(poss.x1-poss.r).toString() + "px";
    if(t_cargas2=="+"){
        span_t1.style.backgroundColor="#ff0e0e"
    }else{
        span_t1.style.backgroundColor="#0e6dff"
    }
    /* polaridad3 */
    var span_t1=document.querySelector("#plano1 .span7");
    span_t1.innerHTML=t_cargas3;
    span_t1.style.top=(poss.x2-poss.r).toString() + "px";
    span_t1.style.left=(poss.y2-poss.r).toString() + "px";
    if(t_cargas3=="+"){
        span_t1.style.backgroundColor="#ff0e0e"
    }else{
        span_t1.style.backgroundColor="#0e6dff"
    }

    /* carga */
    var span_c=document.querySelector("#plano1 .span8");
    span_c.innerHTML="("+(vq1).toString() +"x10^-6)C";
    span_c.style.top=(poss.y1-poss.r-28).toString() + "px";
    span_c.style.left=(poss.x1-150).toString() + "px";
    /* carga2 */
    var span_c=document.querySelector("#plano1 .span9");
    span_c.innerHTML="("+(vq2).toString() +"x10^-6)C";
    span_c.style.top=(poss.y2-poss.r-28).toString() + "px";
    span_c.style.left=(poss.x1-150).toString() + "px";
    /* carga3 */
    var span_c=document.querySelector("#plano1 .span10");
    span_c.innerHTML="("+(vq3).toString() +"x10^-6)C";
    span_c.style.top=(poss.y2-poss.r-28).toString() + "px";
    span_c.style.left=(poss.x2-150).toString() + "px";


    /* fuerzas */
    /* ponemos las fuerzas f1*/
    var span_df=document.querySelector("#plano1 .span11");
    var span_f=document.querySelector(".span11 span");
    span_f.innerHTML=((ffuerza.fuerzax).toFixed(3)).toString() +"N";
    span_df.style.top=(poss.y2 + 100).toString() + "px";
    span_df.style.left="450px";
    /* ponemos las fuerzas f2*/
    var span_df=document.querySelector("#plano1 .span12");
    var span_f=document.querySelector(".span12 span");
    span_f.innerHTML=((ffuerza.fuerzay).toFixed(3)).toString() +"N";
    span_df.style.top=(poss.y2 + 150).toString() + "px";
    span_df.style.left="450px";
    /* ponemos las fuerzas f3*/
    var span_df=document.querySelector("#plano1 .span13");
    var span_f=document.querySelector(".span13 span");
    span_f.innerHTML=((ffuerza.fuerzar).toFixed(3)).toString() +"N";
    span_df.style.top=(poss.y2 + 200).toString() + "px";
    span_df.style.left="450px";

    //posiciona angulo

    if(posicion==1){
    var possimbolo=posangulo(poss.x1,poss.y1,ffuerza.angulo,poss.r);
    }
    if(posicion==2){
    var possimbolo=posangulo(poss.x1,poss.y2,ffuerza.angulo,poss.r);
    }
    if(posicion==3){
    var possimbolo=posangulo(poss.x2,poss.y2,ffuerza.angulo,poss.r);
    }

    var span_sim=document.querySelector("#plano1 .span16");
    span_sim.style.top=(possimbolo.ay).toString() + "px";
    span_sim.style.left=(possimbolo.ax).toString() + "px";

    //valor del angulo
    
    var span_df=document.querySelector("#plano1 .span17");
    var span_f=document.querySelector(".span17 span");
    span_f.innerHTML=((ffuerza.angulo).toFixed(3)).toString() +"°";
    span_df.style.top=(poss.y2 + 250).toString() + "px";
    span_df.style.left="450px";

    /* --------------------------------q */

    var span_sim=document.querySelector("#plano1 .span18");
    span_sim.style.top=(poss.y1-40).toString() + "px";
    span_sim.style.left=(poss.x1-10).toString() + "px";

    var span_sim=document.querySelector("#plano1 .span19");
    span_sim.style.top=(poss.y2-40).toString() + "px";
    span_sim.style.left=(poss.x1-10).toString() + "px";

    var span_sim=document.querySelector("#plano1 .span20");
    span_sim.style.top=(poss.y2-40).toString() + "px";
    span_sim.style.left=(poss.x2-10).toString() + "px";
  

 }
var cargar=document.querySelector(".formulario");
cargar.addEventListener("submit",function(){

    var cf=t_direccion("cf1","cf2","cf3");

    var carga1=document.querySelector("#carga1");
    var carga2=document.querySelector("#carga2");
    var carga3=document.querySelector("#carga3");
    var distancia=document.querySelector("#distancia");
    

    var vq1=carga1.value;
        var vq2=carga2.value;
        var vq3=carga3.value;
        var dt=distancia.value;

        var t_cargas1=t_carga("pos1","neg1");
        var t_cargas2=t_carga("pos2","neg2");
        var t_cargas3=t_carga("pos3","neg3");

    

    var contenedor=document.querySelector("#contenedor1");

    /*  function fuerzac1(q1,q2,q3,p1,p2,p3,h){ */
    
        

    if(cf=="c1"){
        contenedor.style.display="block";
        var ffuerza=fuerzac1(vq1*1e-6,vq2*1e-6,vq3*1e-6,t_cargas1,t_cargas2,t_cargas3,dt);

        
        var poss=dibujoB(t_cargas1,t_cargas2,t_cargas3,ffuerza,1);
        llenar(vq1,vq2,vq3,t_cargas1,t_cargas2,t_cargas3,ffuerza,poss,1);
        


        
        
    }

    if(cf=="c2"){
      contenedor.style.display="block";
      var ffuerza=fuerzac2(vq1*1e-6,vq2*1e-6,vq3*1e-6,t_cargas1,t_cargas2,t_cargas3,dt);

  
      var poss=dibujoB(t_cargas1,t_cargas2,t_cargas3,ffuerza,2);
      llenar(vq1,vq2,vq3,t_cargas1,t_cargas2,t_cargas3,ffuerza,poss,2);

     


    }
    if(cf=="c3"){
      contenedor.style.display="block";
      var ffuerza=fuerzac3(vq1*1e-6,vq2*1e-6,vq3*1e-6,t_cargas1,t_cargas2,t_cargas3,dt);
      
      var poss=dibujoB(t_cargas1,t_cargas2,t_cargas3,ffuerza,3);
      llenar(vq1,vq2,vq3,t_cargas1,t_cargas2,t_cargas3,ffuerza,poss,3);



    }

    
})