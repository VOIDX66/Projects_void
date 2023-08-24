 /* inicio */
 var inicio=document.querySelector("#inicio");
 /*inicio.addEventListener("click",function(){
     window.location.href="index.html";

 })*/

 

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


 function fuerzac(q1,q2,q3,q5,p1,p2,p3,p4,p5,dt){
  let L = dt / 100;
  // calculamos las medidas de las diagonales principales del cuadrado
  /* al trazar las diagonales principales del cuadrado se forman 2 triangulos isoceles
  cuyas hipotenusas tiene la forma C*raiz(2)
  como la carga de referencia esta en el centro es decir en la mitad
  de las diagonales */
  let h = (L * Math.sqrt(2)) / 2; // diagonales principales sobre 2.
  // planteamos las condiciones de equilibrio Σfx = 0 ; Σfy = 0
  // fuerzas que actuan la carga de ref
  let f35 = (k * q3 * q5) / Math.pow(h, 2);
  let f25 = (k * q2 * q5) / Math.pow(h, 2);
  let f15 = (k * q1 * q5) / Math.pow(h, 2);
  // descomponemos las fuerzas
  // asignamos dirreccion a cada una de las fuerzas
  // para f15
  let f15x, f15y;
  if (p5 === '+' && p1 === '+') {
    f15x = f15 * Math.cos((45 * Math.PI) / 180);
    f15y = -f15 * Math.sin((45 * Math.PI) / 180);
  } else if (p5 === '+' && p1 === '-') {
    f15x = -f15 * Math.cos((45 * Math.PI) / 180);
    f15y = f15 * Math.sin((45 * Math.PI) / 180);
  } else if (p5 === '-' && p1 === '+') {
    f15x = -f15 * Math.cos((45 * Math.PI) / 180);
    f15y = f15 * Math.sin((45 * Math.PI) / 180);
  } else if (p5 === '-' && p1 === '-') {
    f15x = f15 * Math.cos((45 * Math.PI) / 180);
    f15y = -f15 * Math.sin((45 * Math.PI) / 180);
  }
  // para f35
  let f35x, f35y;
  if (p5 === '+' && p3 === '+') {
    f35x = -f35 * Math.cos((45 * Math.PI) / 180);
    f35y = f35 * Math.sin((45 * Math.PI) / 180);
  } else if (p5 === '+' && p3 === '-') {
    f35x = f35 * Math.cos((45 * Math.PI) / 180);
    f35y = -f35 * Math.sin((45 * Math.PI) / 180);
  } else if (p5 === '-' && p3 === '+') {
    f35x = f35 * Math.cos((45 * Math.PI) / 180);
    f35y = -f35 * Math.sin((45 * Math.PI) / 180);
  } else if (p5 === '-' && p3 === '-') {
    f35x = -f35 * Math.cos((45 * Math.PI) / 180);
    f35y = f35 * Math.sin((45 * Math.PI) / 180);
  }
  // para f25
  let f25x, f25y;
  if (p5 === '+' && p2 === '+') {
    f25x = f25 * Math.cos((45 * Math.PI) / 180);
    f25y = f25 * Math.sin((45 * Math.PI) / 180);
  } else if (p5 === '+' && p2 === '-') {
    f25x = -f25 * Math.cos((45 * Math.PI) / 180);
    f25y = -f25 * Math.sin((45 * Math.PI) / 180);
  } else if (p5 === '-' && p2 === '+') {
    f25x = -f25 * Math.cos((45 * Math.PI) / 180);
    f25y = -f25 * Math.sin((45 * Math.PI) / 180);
  } else if (p5 === '-' && p2 === '-') {
    f25x = f25 * Math.cos((45 * Math.PI) / 180);
    f25y = f25 * Math.sin((45 * Math.PI) / 180);
  }
  
  let fx, fy;
  if (p5 === '+' && p4 === '+') {
    // 0 = f15x + f35x + f45x - f25x
    fx = (f15x + f35x + f25x) / Math.cos((45 * Math.PI) / 180);
    // 0 = f15y + f25y + f35y - f45y
    fy = (f15y + f25y + f35y) / Math.sin((45 * Math.PI) / 180);
  } else if (p5 === '-' && p4 === '-') {
    // 0 = f15x + f35x + f45x - f25x
    fx = (f15x + f35x + f25x) / Math.cos((45 * Math.PI) / 180);
    // 0 = f15y + f25y + f35y - f45y
    fy = (f15y + f25y + f35y) / Math.sin((45 * Math.PI) / 180);
  } else if (p5 === '+' && p4 === '-') {
    // 0 = f15x + f25x + f35x + f45x
    fx = (-f15x - f35x - f25x) / Math.cos((45 * Math.PI) / 180);
    // 0 = f15y + f25y + f35y + f45y
    fy = (-f15y - f25y - f35y) / Math.sin((45 * Math.PI) / 180);
  } else if (p5 === '-' && p4 === '+') {
    // 0 = f15x + f25x + f35x + f45x
    fx = (-f15x - f35x - f25x) / Math.cos((45 * Math.PI) / 180);
    // 0 = f15y + f25y + f35y + f45y
    fy = (-f15y - f25y - f35y) / Math.sin((45 * Math.PI) / 180);
  }
  
  /* 0 = f15x + f35x + f45x + f25x 
  de la anterior ecuacion despejamos f45x y obtenemos:*/
  // let f45 = Math.abs((-f15x - f35x - f25x) / Math.cos((45 * Math.PI) / 180));
  // f45 = f45 * Math.pow(10, 6);
  
  /* esta porción de codigo es para verificar los datos que calculados por el programa
  console.log(h);
  console.log(f15x);
  console.log(f25x);
  console.log(f35x);
  console.log("\n");
  
  console.log(f15y);
  console.log(f25y);
  console.log(f35y);
  console.log("\n");
  
  console.log(f15);
  console.log(f25);
  console.log(f35);
  console.log("\n");
  
  console.log(fx);
  console.log(fy);
  let seno = Math.sin((45 * Math.PI) / 180);
  let coseno = Math.cos((45 * Math.PI) / 180);
  console.log(seno);
  console.log(coseno);
  */
  
  /* una vez hallada la magnitud de la fuerza, procedemos a 
  calcular la magnitud de q4 */
  let q4 = (fx * Math.pow(h, 2)) / (k * q5);
  
  // q4 = q4 * Math.pow(10, 6);
  console.log(`La magnitud de q4 para que q5 quede en equilibrio es de: ${q4.toExponential(1)} coulombios.
  Y su respectiva magnitud de fuerza f25 = ${fx.toFixed(2)} N.`);



return{
    vq4:q4,
    fuerzar:fx,
}

 }
   /* verifica tipo de fuerzas 1 atraccion 2 repulsion */
   function verificaT(tc1,tc2){
    let vf;
    if(tc1!=tc2){
        vf=1;
    }else{
        vf=2;
    }
    return vf;
}


 function dibujoB(t_cargas1,t_cargas2,t_cargas3,t_cargas4,t_cargas5,ffuerza){

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


    c.beginPath();
    c.arc(x, y, r, 0, 2 * Math.PI);
    c.fillStyle = 'red';
    c.fill();

    
    
    function verificaC(tC){
        let clr;
        if(tC=="+"){
            clr="#ff0e0e";
        }else{
            clr="#0e6dff";
        }
        return clr;

    }

  
    
    /* cambio */
    var tc1=verificaT(t_cargas1,t_cargas5);
    var tc2=verificaT(t_cargas2,t_cargas5);
    var tc3=verificaT(t_cargas3,t_cargas5);
    var tc4=verificaT(t_cargas4,t_cargas5);

    //linea carga1
    let clr= verificaC(t_cargas1);
    
    
    c.beginPath();
    c.moveTo(x,y); //dibuja las fuerzas
    if(tc1==1){
        c.lineTo(x1+50,y1+50);
        c.lineTo(x1+65,y1+50);
        c.moveTo(x1+50,y1+50);
        c.lineTo(x1+50,y1+65);
    }else if(tc1==2){
        c.lineTo(x2-50,y2-50);
        c.lineTo(x2-65,y2-50);
        c.moveTo(x2-50,y2-50);
        c.lineTo(x2-50,y2-65);
    }
    
    c.lineWidth=5;
    c.strokeStyle=clr;
    c.stroke();


        //linea carga2
        clr= verificaC(t_cargas2);
        tc=verificaT(t_cargas2,t_cargas5);
        if(tc2==2 && tc4==1){
          clr="blueviolet";
        }
        if(tc2==1 && tc4==2){
          clr="blueviolet";
        }
        c.beginPath();
        c.moveTo(x,y); //dibuja las fuerzas
        
        if(tc==1){
          c.lineTo(x1+50,y2-50);
          c.lineTo(x1+65,y2-50);
          c.moveTo(x1+50,y2-50);
          c.lineTo(x1+50,y2-65);
            
        }else if(tc==2){
          c.lineTo(x2-50,y1+50);
          c.lineTo(x2-65,y1+50);
          c.moveTo(x2-50,y1+50);
          c.lineTo(x2-50,y1+65);
        }
        
        c.lineWidth=5;
        c.strokeStyle=clr;
        c.stroke();

    

    //linea carga3
    clr= verificaC(t_cargas3);
    tc=verificaT(t_cargas3,t_cargas5);
    if(tc1==2 && tc3==1){
      clr="blueviolet";
    }
    if(tc1==1 && tc3==2){
      clr="blueviolet";
    }
    c.beginPath();
    c.moveTo(x,y); //dibuja las fuerzas
    if(tc==1){
        c.lineTo(x2-50,y2-50);
        c.lineTo(x2-65,y2-50);
        c.moveTo(x2-50,y2-50);
        c.lineTo(x2-50,y2-65);
    }else if(tc==2){
        c.lineTo(x1+50,y1+50);
        c.lineTo(x1+65,y1+50);
        c.moveTo(x1+50,y1+50);
        c.lineTo(x1+50,y1+65);
    }
    
    c.lineWidth=5;
    c.strokeStyle=clr;
    c.stroke();

    //linea carga4
    clr= verificaC(t_cargas4);
    tc=verificaT(t_cargas4,t_cargas5);
    if(tc2==2 && tc4==1){
      clr="blueviolet";
    }
    if(tc2==1 && tc4==2){
      clr="blueviolet";
    }
    c.beginPath();
    c.moveTo(x,y); //dibuja las fuerzas
    
    if(tc==1){
      c.lineTo(x2-50,y1+50);
      c.lineTo(x2-65,y1+50);
      c.moveTo(x2-50,y1+50);
      c.lineTo(x2-50,y1+65);
        
    }else if(tc==2){
      c.lineTo(x1+50,y2-50);
      c.lineTo(x1+65,y2-50);
      c.moveTo(x1+50,y2-50);
      c.lineTo(x1+50,y2-65);
    }
    
    c.lineWidth=5;
    c.strokeStyle=clr;
    c.stroke();

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

 function llenar(vq1,vq2,vq3,vq5,t_cargas1,t_cargas2,t_cargas3,t_cargas4,t_cargas5,ffuerza,poss,dt){
     /* distancias */
     var span_dt=document.querySelector("#plano1 .span3");
     span_dt.innerHTML=((dt).toFixed(3)).toString() +"m";
     span_dt.style.top="500px";
     span_dt.style.left="250px";
 
     var span_dt=document.querySelector("#plano1 .span4");
     span_dt.innerHTML=((dt).toFixed(3)).toString() +"m";
     span_dt.style.top="725px";
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
              span_t1.style.backgroundColor="#ff0e0e";
          }else{
              span_t1.style.backgroundColor="#0e6dff";
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
          var span_t1=document.querySelector("#plano1 .span8");
          span_t1.innerHTML=t_cargas4;
          span_t1.style.top=(poss.y1-poss.r).toString() + "px";
          span_t1.style.left=(poss.x2-poss.r).toString() + "px";
          if(t_cargas4=="+"){
              span_t1.style.backgroundColor="#ff0e0e"
          }else{
              span_t1.style.backgroundColor="#0e6dff"
          }
    
          /* polaridad5 */
          var span_t1=document.querySelector("#plano1 .span9");
          span_t1.innerHTML=t_cargas5;
          span_t1.style.top=(poss.y-poss.r).toString() + "px";
          span_t1.style.left=(poss.x-poss.r).toString() + "px";
          if(t_cargas5=="+"){
              span_t1.style.backgroundColor="#ff0e0e"
          }else{
              span_t1.style.backgroundColor="#0e6dff"
          }

              /* carga */
          var span_c=document.querySelector("#plano1 .span10");
          span_c.innerHTML="("+(vq1).toString() +"x10^-6)C";
          span_c.style.top=(poss.y1-poss.r-20).toString() + "px";
          span_c.style.left=(poss.x1-60).toString() + "px";
          /* carga2 */
          var span_c=document.querySelector("#plano1 .span11");
          span_c.innerHTML="("+(vq2).toString() +"x10^-6)C";
          span_c.style.top=(poss.y2+poss.r).toString() + "px";
          span_c.style.left=(poss.x1-60).toString() + "px";
          /* carga3 */
          var span_c=document.querySelector("#plano1 .span12");
          span_c.innerHTML="("+(vq3).toString() +"x10^-6)C";
          span_c.style.top=(poss.y2+poss.r).toString() + "px";
          span_c.style.left=(poss.x2-60).toString() + "px";
          /* carga4 */
          var span_c=document.querySelector("#plano1 .span13");
          span_c.innerHTML=((ffuerza.vq4).toExponential(2)).toString() +"C";
          span_c.style.top=(poss.y1-poss.r-20).toString() + "px";
          span_c.style.left=(poss.x2-60).toString() + "px";
          /* carga5 */
          var span_c=document.querySelector("#plano1 .span14");
          span_c.innerHTML="("+(vq5).toString() +"x10^-6)C";
          span_c.style.top=(poss.y-15).toString() + "px";
          span_c.style.left=(poss.x+50).toString() + "px";


          /* tipos de fuerzas */


          /* verifica tipo de fuerzas 1 atraccion 2 repulsion */
          /* verificaT(t1,t2) */
          //-------------------------------------fuerza de 1
          let vf1=verificaT(t_cargas1,t_cargas5);

          if(vf1==1){
          var span_c=document.querySelector("#plano1 .span15");
          span_c.style.top=(poss.y1+poss.r+50).toString() + "px";
          span_c.style.left=(poss.x1+poss.r+70).toString() + "px";
          span_c.style.rotate="45grad"
          }if(vf1==2){
            var span_c=document.querySelector("#plano1 .span15");
            span_c.style.top=(poss.y2-poss.r-90).toString() + "px";
            span_c.style.left=(poss.x2-poss.r-70).toString() + "px";
            span_c.style.rotate="45grad"
            }

            //-----------------------------------------------------fuerza e 3
            let vf3=verificaT(t_cargas3,t_cargas5);

          if(vf3==1){
            var span_c=document.querySelector("#plano1 .span17");
            span_c.style.top=(poss.y2-poss.r-70).toString() + "px";
            span_c.style.left=(poss.x2-poss.r-80).toString() + "px";
            span_c.style.rotate="45grad"
          }if(vf3==2){
          var span_c=document.querySelector("#plano1 .span17");
          span_c.style.top=(poss.y1+poss.r+70).toString() + "px";
          span_c.style.left=(poss.x1+poss.r+60).toString() + "px";
          span_c.style.rotate="45grad"
            
            }
            
          //-------------------------------------fuerza de 2
          let vf2=verificaT(t_cargas2,t_cargas5);

          if(vf2==1){
          var span_c=document.querySelector("#plano1 .span16");
          span_c.style.top=(poss.y2-poss.r-90).toString() + "px";
          span_c.style.left=(poss.x1+poss.r+50).toString() + "px";
          span_c.style.rotate="-45grad"
          }if(vf2==2){
          var span_c=document.querySelector("#plano1 .span16");
          span_c.style.top=(poss.y1+poss.r+50).toString() + "px";
          span_c.style.left=(poss.x2-poss.r-90).toString() + "px";
          span_c.style.rotate="-45grad"
            
            }
          //-------------------------------------fuerza de 4
          let vf4=verificaT(t_cargas4,t_cargas5);

          if(vf4==1){
            var span_c=document.querySelector("#plano1 .span18");
          span_c.style.top=(poss.y1+poss.r+67).toString() + "px";
          span_c.style.left=(poss.x2-poss.r-70).toString() + "px";
          span_c.style.rotate="-45grad"
          }if(vf4==2){
            var span_c=document.querySelector("#plano1 .span18");
            span_c.style.top=(poss.y2-poss.r-73).toString() + "px";
            span_c.style.left=(poss.x1+poss.r+70).toString() + "px";
            span_c.style.rotate="-45grad"
            
            }
            if(ffuerza.vq4==0){
              //console.log(ffuerza.vq4);
              alert("Las fuerza que debe hacer q4 es de 0N ya que con las otras cargas esta en equilibrio el sistema")
            }
          /* fuerzas */
          /* ponemos las fuerzas f45*/
          var span_df=document.querySelector("#plano1 .span19");
          var span_f=document.querySelector(".span19 span");
          span_f.innerHTML=((ffuerza.fuerzar).toFixed(3)).toString() +"N";
          span_df.style.top=(poss.y2 + 200).toString() + "px";
          span_df.style.left="450px";  


          
    /* --------------------------------q */

    var span_sim=document.querySelector("#plano1 .span20");
    span_sim.style.top=(poss.y1-40).toString() + "px";
    span_sim.style.left=(poss.x1-10).toString() + "px";

    var span_sim=document.querySelector("#plano1 .span21");
    span_sim.style.top=(poss.y2-40).toString() + "px";
    span_sim.style.left=(poss.x1-10).toString() + "px";

    var span_sim=document.querySelector("#plano1 .span22");
    span_sim.style.top=(poss.y2-40).toString() + "px";
    span_sim.style.left=(poss.x2-10).toString() + "px";

    var span_sim=document.querySelector("#plano1 .span23");
    span_sim.style.top=(poss.y1-40).toString() + "px";
    span_sim.style.left=(poss.x2-10).toString() + "px";

    var span_sim=document.querySelector("#plano1 .span24");
    span_sim.style.top=(poss.y-40).toString() + "px";
    span_sim.style.left=(poss.x-10).toString() + "px";

 }



 /* principal */

 var cargar=document.querySelector(".formulario");
cargar.addEventListener("submit",function(){

    

    var carga1=document.querySelector("#carga1");
    var carga2=document.querySelector("#carga2");
    var carga3=document.querySelector("#carga3");
    var carga5=document.querySelector("#carga5");
    var distancia=document.querySelector("#distancia");
    

    var vq1=carga1.value;
        var vq2=carga2.value;
        var vq3=carga3.value;
        var vq5=carga5.value;
        var dt=distancia.value;

        var t_cargas1=t_carga("pos1","neg1");
        var t_cargas2=t_carga("pos2","neg2");
        var t_cargas3=t_carga("pos3","neg3");
        var t_cargas4=t_carga("pos4","neg4");
        var t_cargas5=t_carga("pos5","neg5");

        if(t_cargas1!=t_cargas3){
          alert("La polaridad de Q1 y Q3 deben ser iguales")
        }else if(t_cargas2!=t_cargas4){
          alert("La polaridad de Q2 y Q4 deben ser iguales")
        }else if(vq1 != vq3){
          alert("el valor de las cargas Q1 y Q3 deben ser iguales")
        }else{
          var contenedor=document.querySelector("#contenedor1");

    
          contenedor.style.display="block";
          var ffuerza= fuerzac(vq1*1e-6,vq2*1e-6,vq3*1e-6,vq5*1e-6,t_cargas1,t_cargas2,t_cargas3,t_cargas4,t_cargas5,dt);
          var poss=dibujoB(t_cargas1,t_cargas2,t_cargas3,t_cargas4,t_cargas5,ffuerza);
          llenar(vq1,vq2,vq3,vq5,t_cargas1,t_cargas2,t_cargas3,t_cargas4,t_cargas5,ffuerza,poss,dt/100);

        }
       

        
  
    
})

