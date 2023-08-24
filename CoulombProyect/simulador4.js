
 /* inicio */
 var inicio=document.querySelector("#inicio");
 /*inicio.addEventListener("click",function(){
     window.location.href="index.html";

 })*/

 function t_direccion(id1,id2,id3,id4){ //funcion que evalua los radio button
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
    if(document.getElementById(id4).checked){
        dir="c4";
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


 function fuerzac1(q1,q2,q3,q4,p1,p2,p3,p4,dt){
      
  // Conversión de centímetros a metros
  var L = dt / 100;

  // Calculamos las medidas de las diagonales principales del cuadrado
  // Al trazar las diagonales principales del cuadrado se forman 2 triángulos isósceles
  // Cuyas hipotenusas tienen la forma C * sqrt(2)
  let h = L * Math.sqrt(2); // Medida de las diagonales principales

  // Planteamos las condiciones de equilibrio Σfx = 0 ; Σfy = 0

  // Fuerzas que actúan en la carga de referencia
  let f21 = (k * q2 * q1) / (L ** 2);
  let f31 = (k * q3 * q1) / (L ** 2);
  let f41 = (k * q4 * q1) / (h ** 2);

  // Descomponemos las fuerzas
  // Dada la geometría del problema, estas componentes siempre serán 0.
  let f21y = f21 * Math.sin((0 * Math.PI) / 180);
  let f31x = f31 * Math.cos((90 * Math.PI) / 180);

  // Asignamos dirección a cada una de las fuerzas

  // Para f21
  let f21x;
  if (p1 === "+" && p2 === "+") {
    f21x = -f21 * Math.cos((0 * Math.PI) / 180);
  } else if (p1 === "+" && p2 === "-") {
    f21x = f21 * Math.cos((0 * Math.PI) / 180);
  } else if (p1 === "-" && p2 === "+") {
    f21x = f21 * Math.cos((0 * Math.PI) / 180);
  } else if (p1 === "-" && p2 === "-") {
    f21x = -f21 * Math.cos((0 * Math.PI) / 180);
  }

  // Para f31
  let f31y;
  if (p1 === "+" && p3 === "+") {
    f31y = f31 * Math.sin((90 * Math.PI) / 180);
  } else if (p1 === "+" && p3 === "-") {
    f31y = -f31 * Math.sin((90 * Math.PI) / 180);
  } else if (p1 === "-" && p3 === "+") {
    f31y = -f31 * Math.sin((90 * Math.PI) / 180);
  } else if (p1 === "-" && p3 === "-") {
    f31y = f31 * Math.sin((90 * Math.PI) / 180);
  }

  // Para f41
  let f41x, f41y;
  if (p1 === "+" && p4 === "+") {
    f41x = f41 * Math.cos((45 * Math.PI) / 180);
    f41y = -f41 * Math.sin((45 * Math.PI) / 180);
  } else if (p1 === "+" && p4 === "-") {
    f41x = -f41 * Math.cos((45 * Math.PI) / 180);
    f41y = f41 * Math.sin((45 * Math.PI) / 180);
  } else if (p1 === "-" && p4 === "+") {
    f41x = -f41 * Math.cos((45 * Math.PI) / 180);
    f41y = f41 * Math.sin((45 * Math.PI) / 180);
  } else if (p1 === "-" && p4 === "-") {
    f41x = f41 * Math.cos((45 * Math.PI) / 180);
    f41y = -f41 * Math.sin((45 * Math.PI) / 180);
  }

  var sumax = f21x + f31x + f41x;
  var sumay = f21y + f31y + f41y;
  var resultante = Math.sqrt(Math.pow(sumax, 2) + Math.pow(sumay, 2));

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

  console.log(sumax);
  console.log(sumay);
  console.log(resultante);
  console.log(angulo);

    return{
      fuerzax:sumax,
      fuerzay:sumay,
      fuerzar:resultante,
      angulo:angulo,
      cateto:h,
    }
      
  }


  
  function fuerzac2(q1,q2,q3,q4,p1,p2,p3,p4,dt){
    let L = dt / 100;

    // Calculating the measures of the main diagonals of the square
    // When drawing the main diagonals of the square, two isosceles triangles are formed
    // with hypotenuses in the form C * sqrt(2)
    let h = L * Math.sqrt(2); // Measure of the main diagonals
    
    // Setting up the equilibrium conditions: Σfx = 0, Σfy = 0
    
    // Forces acting on the reference load
    let f12 = (k * q1 * q2) / (L ** 2);
    let f32 = (k * q3 * q2) / (h ** 2);
    let f42 = (k * q4 * q2) / (L ** 2);
    
    // Decomposing the forces
    // Given the geometry of the problem, these components will always be 0
    let f12y = f12 * Math.sin((0 * Math.PI) / 180);
    let f42x = f42 * Math.cos((90 * Math.PI) / 180);
    
    // Assigning direction to each force
    
    // For f12
    let f12x;
    if (p1 === "+" && p2 === "+") {
      f12x = f12 * Math.cos((0 * Math.PI) / 180);
    } else if (p1 === "+" && p2 === "-") {
      f12x = -f12 * Math.cos((0 * Math.PI) / 180);
    } else if (p1 === "-" && p2 === "+") {
      f12x = -f12 * Math.cos((0 * Math.PI) / 180);
    } else if (p1 === "-" && p2 === "-") {
      f12x = f12 * Math.cos((0 * Math.PI) / 180);
    }
    
    // For f32
    let f32y, f32x;
    if (p2 === "+" && p3 === "+") {
      f32y = f32 * Math.sin((45 * Math.PI) / 180);
      f32x = f32 * Math.cos((45 * Math.PI) / 180);
    } else if (p2 === "+" && p3 === "-") {
      f32y = -f32 * Math.sin((45 * Math.PI) / 180);
      f32x = -f32 * Math.cos((45 * Math.PI) / 180);
    } else if (p2 === "-" && p3 === "+") {
      f32y = -f32 * Math.sin((45 * Math.PI) / 180);
      f32x = -f32 * Math.cos((45 * Math.PI) / 180);
    } else if (p2 === "-" && p3 === "-") {
      f32y = f32 * Math.sin((45 * Math.PI) / 180);
      f32x = f32 * Math.cos((45 * Math.PI) / 180);
    }
    
    // For f42
    let f42y;
    if (p2 === "+" && p4 === "+") {
      f42y = f42 * Math.sin((90 * Math.PI) / 180);
    } else if (p2 === "+" && p4 === "-") {
      f42y = -f42 * Math.sin((90 * Math.PI) / 180);
    } else if (p2 === "-" && p4 === "+") {
      f42y = -f42 * Math.sin((90 * Math.PI) / 180);
    } else if (p2 === "-" && p4 === "-") {
      f42y = f42 * Math.sin((90 * Math.PI) / 180);
    }
    
    let sumax = f12x + f32x + f42x;
    let sumay = f12y + f32y + f42y;
    let resultante = Math.sqrt(sumax ** 2 + sumay ** 2);
    
    // Angle of the resultant
    let x = Math.atan(sumay / sumax);
    let grados = (x * 180) / Math.PI;
    
    // Calculating the direction of the resultant with respect to the x-axis
    var angulo = (x * 180) / Math.PI;
// Calculamos la dirección de la resultante con respecto al eje X
if (sumax < 0 && sumay > 0) {
  angulo = 180 + angulo;
} else if (sumax < 0 && sumay < 0) {
  angulo = 180 + angulo;
} else if (sumax > 0 && sumay < 0) {
  angulo = 360 + angulo;
}

/* console.log("angul"+angulo); */
return{
  fuerzax:sumax,
  fuerzay:sumay,
  fuerzar:resultante,
  angulo:angulo,
  cateto:h,
}
    
    
    
        
    }


    function fuerzac3(q1,q2,q3,q4,p1,p2,p3,p4,dt){
      L = dt / 100;

// Calculating the measures of the main diagonals of the square
// When drawing the main diagonals of the square, two isosceles triangles are formed
// with hypotenuses in the form C * sqrt(2)
let h = L * Math.sqrt(2); // Measure of the main diagonals

// Setting up the equilibrium conditions: Σfx = 0, Σfy = 0

// Forces acting on the reference load
let f13 = (k * q1 * q3) / (L ** 2);
let f23 = (k * q2 * q3) / (h ** 2);
let f43 = (k * q4 * q3) / (L ** 2);

// Decomposing the forces
// Given the geometry of the problem, these components will always be 0
let f13x = f13 * Math.cos((90 * Math.PI) / 180);
let f43y = f43 * Math.sin((0 * Math.PI) / 180);

// Assigning direction to each force

// For f13
let f13y;
if (p1 === "+" && p3 === "+") {
  f13y = -f13 * Math.sin((90 * Math.PI) / 180);
} else if (p1 === "+" && p3 === "-") {
  f13y = f13 * Math.sin((90 * Math.PI) / 180);
} else if (p1 === "-" && p3 === "+") {
  f13y = f13 * Math.sin((90 * Math.PI) / 180);
} else if (p1 === "-" && p3 === "-") {
  f13y = -f13 * Math.sin((90 * Math.PI) / 180);
}

// For f23
let f23y, f23x;
if (p2 === "+" && p3 === "+") {
  f23y = -f23 * Math.sin((45 * Math.PI) / 180);
  f23x = -f23 * Math.cos((45 * Math.PI) / 180);
} else if (p2 === "+" && p3 === "-") {
  f23y = f23 * Math.sin((45 * Math.PI) / 180);
  f23x = f23 * Math.cos((45 * Math.PI) / 180);
} else if (p2 === "-" && p3 === "+") {
  f23y = f23 * Math.sin((45 * Math.PI) / 180);
  f23x = f23 * Math.cos((45 * Math.PI) / 180);
} else if (p2 === "-" && p3 === "-") {
  f23y = -f23 * Math.sin((45 * Math.PI) / 180);
  f23x = -f23 * Math.cos((45 * Math.PI) / 180);
}

// For f43
let f43x;
if (p4 === "+" && p3 === "+") {
  f43x = -f43 * Math.cos((0 * Math.PI) / 180);
} else if (p4 === "+" && p3 === "-") {
  f43x = f43 * Math.cos((0 * Math.PI) / 180);
} else if (p4 === "-" && p3 === "+") {
  f43x = f43 * Math.cos((0 * Math.PI) / 180);
} else if (p4 === "-" && p3 === "-") {
  f43x = -f43 * Math.cos((0 * Math.PI) / 180);
}

let sumax = f13x + f23x + f43x;
let sumay = f13y + f23y + f43y;
let resultante = Math.sqrt(sumax ** 2 + sumay ** 2);

// Angle of the resultant
let x = Math.atan(sumay / sumax);
let grados = (x * 180) / Math.PI;

// Calculating the direction of the resultant with respect to the x-axis
var angulo = (x * 180) / Math.PI;
if (sumax < 0 && sumay > 0) {
  angulo = 180 + grados;
} else if (sumax < 0 && sumay < 0) {
  angulo = 180 + grados;
} else if (sumax > 0 && sumay < 0) {
  angulo = 360 + grados;
}

return{
  fuerzax:sumax,
  fuerzay:sumay,
  fuerzar:resultante,
  angulo:angulo,
  cateto:h,
}
   
          
      }
    function fuerzac4(q1,q2,q3,q4,p1,p2,p3,p4,dt){
   
      L = dt / 100;

      // Calculating the measures of the main diagonals of the square
      // When drawing the main diagonals of the square, two isosceles triangles are formed
      // with hypotenuses in the form C * sqrt(2)
      let h = L * Math.sqrt(2); // Measure of the main diagonals
      
      // Setting up the equilibrium conditions: Σfx = 0, Σfy = 0
      
      // Forces acting on the reference load
      let f14 = (k * q1 * q4) / (h ** 2);
      let f24 = (k * q2 * q4) / (L ** 2);
      let f34 = (k * q3 * q4) / (L ** 2);
      
      // Decomposing the forces
      // Given the geometry of the problem, these components will always be 0
      let f24x = f24 * Math.cos((90 * Math.PI) / 180);
      let f34y = f34 * Math.sin((0 * Math.PI) / 180);
      
      // Assigning direction to each force
      
      // For f14
      let f14x, f14y;
      if (p1 === "+" && p4 === "+") {
        f14x = f14 * Math.cos((45 * Math.PI) / 180);
        f14y = -f14 * Math.sin((45 * Math.PI) / 180);
      } else if (p1 === "+" && p4 === "-") {
        f14x = -f14 * Math.cos((45 * Math.PI) / 180);
        f14y = f14 * Math.sin((45 * Math.PI) / 180);
      } else if (p1 === "-" && p4 === "+") {
        f14x = -f14 * Math.cos((45 * Math.PI) / 180);
        f14y = f14 * Math.sin((45 * Math.PI) / 180);
      } else if (p1 === "-" && p4 === "-") {
        f14x = f14 * Math.cos((45 * Math.PI) / 180);
        f14y = -f14 * Math.sin((45 * Math.PI) / 180);
      }
      
      // For f24
      let f24y;
      if (p2 === "+" && p4 === "+") {
        f24y = -f24 * Math.sin((90 * Math.PI) / 180);
      } else if (p2 === "+" && p4 === "-") {
        f24y = f24 * Math.sin((90 * Math.PI) / 180);
      } else if (p2 === "-" && p3 === "+") {
        f24y = f24 * Math.sin((90 * Math.PI) / 180);
      } else if (p2 === "-" && p3 === "-") {
        f24y = -f24 * Math.sin((90 * Math.PI) / 180);
      }
      
      // For f34
      let f34x;
      if (p4 === "+" && p3 === "+") {
        f34x = f34 * Math.cos((0 * Math.PI) / 180);
      } else if (p4 === "+" && p3 === "-") {
        f34x = -f34 * Math.cos((0 * Math.PI) / 180);
      } else if (p4 === "-" && p3 === "+") {
        f34x = -f34 * Math.cos((0 * Math.PI) / 180);
      } else if (p4 === "-" && p3 === "-") {
        f34x = f34 * Math.cos((0 * Math.PI) / 180);
      }
      
      let sumax = f14x + f24x + f34x;
      let sumay = f14y + f24y + f34y;
      let resultante = Math.sqrt(sumax ** 2 + sumay ** 2);
      
      // Angle of the resultant
      let x = Math.atan(sumay / sumax);
      let grados = (x * 180) / Math.PI;
      
      // Calculating the direction of the resultant with respect to the x-axis
      var angulo = (x * 180) / Math.PI;
      if (sumax < 0 && sumay > 0) {
        angulo = 180 + grados;
      } else if (sumax < 0 && sumay < 0) {
        angulo = 180 + grados;
      } else if (sumax > 0 && sumay < 0) {
        angulo = 360 + grados;
      }
      
      return{
        fuerzax:sumax,
        fuerzay:sumay,
        fuerzar:resultante,
        angulo:angulo,
        cateto:h,
      }
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

        var canvas=document.querySelector("#plano1 canvas");
    
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
        c.lineTo(x2,y1);
        c.lineTo(x1,y1);
        c.lineWidth=1;
        c.strokeStyle="black";
        c.stroke();

        /* dibuja las cargas */

        c.beginPath();
        c.arc(x1, y1, r, 0, 2 * Math.PI);
        c.fillStyle = 'red';
        c.fill();

        c.beginPath();
        c.arc(x2, y1, r, 0, 2 * Math.PI);
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
    c.moveTo(700,y_canvas);
    c.lineTo(695,y_canvas-5);
    c.strokeStyle='green';
    c.lineWidth=3;
    c.stroke();
    c.moveTo(700,y_canvas);
    c.lineTo(705,y_canvas-5);
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

        if(posicion==4){
            puntos(x2,y2);
            var radians = (ffuerza.angulo) * (Math.PI / 180);
            var x_cartesiano = ffuerza.fuerzar * Math.cos(radians);
            var y_cartesiano = ffuerza.fuerzar * Math.sin(radians);
            var x_canvas = 700 + x_cartesiano;
            var y_canvas = 300 - y_cartesiano;
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
            var y_canvas = 300 - y_cartesiano;
            //vector fuerza
            
            c.beginPath();
            c.moveTo(700,300);
            c.lineTo(x_canvas, y_canvas);
            c.strokeStyle = 'black';   
            c.lineWidth = 3;
            c.stroke();
            c.closePath();
            CrearFlecha(ffuerza.angulo,x_canvas,y_canvas);
            
            //dibujar eje x
            c.beginPath();
            c.moveTo(700,300);
            c.lineTo(x_canvas,300);
            c.strokeStyle='orange';
            c.lineWidth=3;
            c.stroke();
            //flecha para eje x
            if(x_canvas>700){
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
            c.moveTo(700,300);
            c.lineTo(700,y_canvas);
            c.strokeStyle='green';
            c.lineWidth=3;
            c.stroke();
            //flecha para eje y
            if(y_canvas<300){
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
              c.moveTo(700, y_canvas);
              c.lineTo(705,y_canvas-5);
              c.strokeStyle='green';
              c.lineWidth=3;
              c.stroke();
              c.moveTo(700,y_canvas);
              c.lineTo(695,y_canvas-5);
              c.strokeStyle='green';
              c.lineWidth=3;
              c.stroke();
          
            }
          
          //dibujo del angulo
    
          var a=ffuerza.angulo;
          var radio=60;
          
          c.beginPath();
          c.moveTo(x2+r,y1);
          c.lineTo(x2+r+10,y1)
          c.arc(x2,y1,radio,0 * Math.PI/180,-a * Math.PI/180,true);
          c.fillStyle="transparent"
          c.strokeStyle="black";
    
    
          c.fill();
          c.stroke();
          puntos(x2,y1);
    
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

      function llenar(vq1,vq2,vq3,vq4,t_cargas1,t_cargas2,t_cargas3,t_cargas4,ffuerza,poss,posicion){
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
     }else if(t_cargas1=="-"){
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
     
     /* polaridad4 */
     var span_t1=document.querySelector("#plano1 .span71");
     span_t1.innerHTML=t_cargas4;
     span_t1.style.top=(poss.y1-poss.r).toString() + "px";
     span_t1.style.left=(poss.x2-poss.r).toString() + "px";
     if(t_cargas4=="+"){
         span_t1.style.backgroundColor="#ff0e0e"
     }else{
         span_t1.style.backgroundColor="#0e6dff"
     }

      /* carga */
    var span_c=document.querySelector("#plano1 .span8");
    span_c.innerHTML="("+(vq1).toString() +"x10^-6)C";
    span_c.style.top=(poss.y1-poss.r-20).toString() + "px";
    span_c.style.left=(poss.x1-60).toString() + "px";
    /* carga2 */
    var span_c=document.querySelector("#plano1 .span9");
    span_c.innerHTML="("+(vq2).toString() +"x10^-6)C";
    span_c.style.top=(poss.y2-poss.r-20).toString() + "px";
    span_c.style.left=(poss.x1-60).toString() + "px";
    /* carga3 */
    var span_c=document.querySelector("#plano1 .span10");
    span_c.innerHTML="("+(vq3).toString() +"x10^-6)C";
    span_c.style.top=(poss.y2-poss.r-20).toString() + "px";
    span_c.style.left=(poss.x2-60).toString() + "px";
    /* carga4 */
    var span_c=document.querySelector("#plano1 .span101");
    span_c.innerHTML="("+(vq4).toString() +"x10^-6)C";
    span_c.style.top=(poss.y1-poss.r-20).toString() + "px";
    span_c.style.left=(poss.x2-60).toString() + "px";


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
    /* ponemos el angulo*/
    var span_df=document.querySelector("#plano1 .span131");
    var span_f=document.querySelector(".span131 span");
    
    span_f.innerHTML=((ffuerza.angulo).toFixed(3)).toString() +"N";
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

    var span_sim=document.querySelector("#plano1 .span21");
    span_sim.style.top=(poss.y1-40).toString() + "px";
    span_sim.style.left=(poss.x2-10).toString() + "px";
  


      }


 /* principal */

 var cargar=document.querySelector(".formulario");
cargar.addEventListener("submit",function(){

    var cf=t_direccion("cf1","cf2","cf3","cf4");

    var carga1=document.querySelector("#carga1");
    var carga2=document.querySelector("#carga2");
    var carga3=document.querySelector("#carga3");
    var carga4=document.querySelector("#carga4");
    var distancia=document.querySelector("#distancia");
    

    var vq1=carga1.value;
        var vq2=carga2.value;
        var vq3=carga3.value;
        var vq4=carga4.value;
        var dt=distancia.value;

        var t_cargas1=t_carga("pos1","neg1");
        var t_cargas2=t_carga("pos2","neg2");
        var t_cargas3=t_carga("pos3","neg3");
        var t_cargas4=t_carga("pos4","neg4");

        
    var contenedor=document.querySelector("#contenedor1");

    if(cf=="c1"){
        contenedor.style.display="block";
        var ffuerza=fuerzac1(vq1*1e-6,vq2*1e-6,vq3*1e-6,vq4*1e-6,t_cargas1,t_cargas2,t_cargas3,t_cargas4,dt);

        var poss=dibujoB(t_cargas1,t_cargas2,t_cargas3,ffuerza,1);
        llenar(vq1,vq2,vq3,vq4,t_cargas1,t_cargas2,t_cargas3,t_cargas4,ffuerza,poss,1);
        
        
    }
    if(cf=="c2"){
        contenedor.style.display="block";
        var ffuerza= fuerzac2(vq1*1e-6,vq2*1e-6,vq3*1e-6,vq4*1e-6,t_cargas1,t_cargas2,t_cargas3,t_cargas4,dt);
        var poss=dibujoB(t_cargas1,t_cargas2,t_cargas3,ffuerza,2);
        llenar(vq1,vq2,vq3,vq4,t_cargas1,t_cargas2,t_cargas3,t_cargas4,ffuerza,poss,2);
        
        
    }
    if(cf=="c3"){
        contenedor.style.display="block";
        var ffuerza= fuerzac3(vq1*1e-6,vq2*1e-6,vq3*1e-6,vq4*1e-6,t_cargas1,t_cargas2,t_cargas3,t_cargas4,dt);
        var poss=dibujoB(t_cargas1,t_cargas2,t_cargas3,ffuerza,3);
        llenar(vq1,vq2,vq3,vq4,t_cargas1,t_cargas2,t_cargas3,t_cargas4,ffuerza,poss,3);
        
        
    }
    if(cf=="c4"){
        contenedor.style.display="block";
        var ffuerza= fuerzac4(vq1*1e-6,vq2*1e-6,vq3*1e-6,vq4*1e-6,t_cargas1,t_cargas2,t_cargas3,t_cargas4,dt);
        var poss=dibujoB(t_cargas1,t_cargas2,t_cargas3,ffuerza,4);
        llenar(vq1,vq2,vq3,vq4,t_cargas1,t_cargas2,t_cargas3,t_cargas4,ffuerza,poss,4);
        
        
    }

    



})