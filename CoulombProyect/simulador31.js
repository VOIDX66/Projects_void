
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

function Coulomb(q1,q2,d){
    let f=(k * q1* q2)/(Math.pow(d,2))
    return f;
}

 function fuerzac1(q1, q2,q3,d){//funcion ejecutada cuando ambas fuerzas son iguales
    let d1=d/2;
    let d2=d-d1;

    let f1= Coulomb(q1,q2,d1);
    let f2= Coulomb(q3,q2,d2);
    let f3= f1-f2;

    return {
        distancia1: d1,
        distancia2: d2,
        fuerza1:f1,
        fuerza2:f2,
        fuerza3:f3,
    };


 }

function fuerzac2(q1, q2, q3, d) {
    let A = q1 - q3;
    let B = -(2 * q1 * d);
    let C = q1 * Math.pow(d, 2);
    let x, y;
    
    if (q1 !== q3) {
      let discriminant = Math.sqrt(Math.pow(B, 2) - 4 * A * C);
      let x1 = (-B + discriminant) / (2 * A);
      let x2 = (-B - discriminant) / (2 * A);
    
      if (x1 > 0 && x1 < d) {
        x = x1;
        y = d - x1;

      } else if (x2 > 0 && x2 < d) {
        x = x2;
        y = d - x;

      }
    } else {
      x = (q1 * Math.pow(d, 2)) / (2 * q1 * d);
      y = d - x;
    }
    
    let f12 = (k * q1 * q2) / Math.pow(x, 2);
    let f32 = (k * q3 * q2) / Math.pow(y, 2);
    


    return {
        distancia1: x,
        distancia2: y,
        fuerza1:f12,
        fuerza2:f32,
        
    };
    
}


function dibujar(c,distancia1,distancia2,dt,t_cargas1,t_cargas2,t_cargas3,posicion) {
    
    var canvas=document.querySelector("#plano1 canvas");
    
    canvas.width=900;
    canvas.height=600;

    var c=canvas.getContext("2d");

    
    var x=450;
    var y=180;
    var y2=260;
    var y3=320;
    r=45;

    var x1;
    var x2;

    dt=dt*100;
    distancia1=distancia1*100;
    distancia2=distancia2*100;

    if(distancia1==distancia2){
        x1=x-300;
        x2=x+300;
    }
    if(distancia1 != distancia2){
        x1=x-300;
        x2=x+300;
        var aux=distancia1+distancia2;
        var aux2=600/aux;
        var aux3=distancia1*aux2;
        var aux4=x1+aux3;
        
        x=aux4;

    }

    c.moveTo(x1,y); //dibuja la linea entre cargas
    c.lineTo(x,y);
    c.lineTo(x2,y);
    c.lineWidth=1;
    c.strokeStyle="black";
    c.stroke();


    var arreglox=[x1,x2,x];// dibuja la forma de las cargas
        arreglox.forEach(function(elemento){
            c.beginPath();
            c.arc(elemento, y, r, 0, 2 * Math.PI);
            c.fillStyle = 'red';
            c.fill();
        })

        c.moveTo(x1,y2); //dibuja la segunda linea
        c.strokeStyle="blue";
        c.lineTo(x,y2);
        c.stroke(); 
        c.beginPath(); // Restablecer el contexto de dibujo antes de cambiar el estilo de trazo
        c.moveTo(x,y2)
        c.strokeStyle="red";
        c.lineTo(x2,y2);
        c.lineWidth=1;
        c.stroke();
     
    
    var cx=(x2-x1)/dt



  
    
    
    arreglox.forEach(function(elemento){//dibuja los puntos  de linea
        c.beginPath();
        c.moveTo(elemento,y2);
        c.lineTo(elemento,y2-10);
        c.lineTo(elemento,y2+10);
        c.lineWidth=1.5;
        c.strokeStyle="black";
        c.stroke(); 
    })

    for(var i=x1;i<=x2;i=i+cx){ //dibuja los centimetros
        c.beginPath();
        c.moveTo(i,y3);
        c.lineTo(i,y3-5);
        c.lineWidth=1.5;
        c.strokeStyle="black";
        c.stroke(); 
    }

    c.moveTo(x1,y3); //dibuja la tercera linea
    c.lineTo(x,y3);
    c.strokeStyle="black";
    c.lineTo(x2,y3);
    c.lineWidth=1;
    c.stroke();

    var arreglox=[x1,x2];// dibuja la forma de las cargas
    arreglox.forEach(function(elemento){//dibuja los puntos  de dt
        c.beginPath();
        c.moveTo(elemento,y3);
        c.lineTo(elemento,y3-10);
        c.lineTo(elemento,y3+10);
        c.lineWidth=1.5;
        c.strokeStyle="black";
        c.stroke(); 
    })

    var colorL1;
    var colorL2;
    if(t_cargas1==t_cargas2){
        if(t_cargas1=="+"){
            colorL2="#ff0e0e"
        }
        if(t_cargas1=="-"){
            colorL2="#0e6dff"
        }   
    }if(t_cargas1!=t_cargas2){
        if(t_cargas1=="+"){
            colorL1="#ff0e0e"
        }
        if(t_cargas1=="-"){
            colorL1="#0e6dff"
        }  
    } 

    if(t_cargas3==t_cargas2){
        if(t_cargas3=="+"){
            colorL1="#ff0e0e"
        }
        if(t_cargas3=="-"){
            colorL1="#0e6dff"
        }   
    }if(t_cargas3!=t_cargas2){
        if(t_cargas3=="+"){
            colorL2="#ff0e0e"
        }
        if(t_cargas3=="-"){
            colorL2="#0e6dff"
        }  
    } 


    
    if(posicion==2 && (x-x1>90 && x2-x>90)) {   
        var tamañof;
        var tamañof2;
        if(x-x1 < x2-x){
            tamañof=(x+x1)/2;
            tamañof2=x-tamañof;
        }else if(x2-x < x-x1){
            tamañof2=((x+x2)/2)-x;
            tamañof=x-tamañof2;
            console.log(x)
            console.log(tamañof2)
            
        }else if(x2-x == x-x1){
            tamañof=x-180;
            tamañof2=180;
        }
        

        c.beginPath();// dibuja las fuerzas 1
        c.moveTo(x-r,y);
        c.lineTo(tamañof,y);
        c.lineTo(tamañof+10,y-10);
        c.moveTo(tamañof,y);
        c.lineTo(tamañof+10,y+10);
        c.lineWidth=5;
        c.strokeStyle=colorL1;
        c.stroke(); 
        
    
        c.beginPath();// dibuja las fuerzas 2
        c.moveTo(x+r,y);
        c.lineTo(x+tamañof2,y);
        c.lineTo(x+tamañof2-10,y-10);
        c.moveTo(x+tamañof2,y);
        c.lineTo(x+tamañof2-10,y+10);
        c.lineWidth=5;
        c.strokeStyle=colorL2;
        c.stroke(); 

    }else{
        function colores(v){
            let clr;
            if(v=="+"){
                clr="#ff0e0e";
            }else{
                clr="#0e6dff";
            }
            return clr;
        }

            let clr=colores(t_cargas2);
            let desplaz=y-r-30;
        
            for(var i=y+r;i>desplaz;i=i-10){
                c.beginPath();
                c.moveTo(x,i);
                c.lineTo(x,i-5);
                c.lineWidth=0.8;
                c.strokeStyle=clr;
                c.stroke();
                }
                
                c.beginPath();
                c.moveTo(x,y-r-30);
                c.lineTo(x-20,y-r-30);
                c.moveTo(x,y-r-30);
                c.lineTo(x+20,y-r-30);
                c.lineWidth=0.8;
                c.strokeStyle=clr;
                c.stroke();

    }
    




    return {
        x:x,
        x1:x1,
        x2:x2,
        y:y,
        y2:y2,
        y3:y3,
        r:r,
        dt:dt,
        distancia1:distancia1,
        distancia2:distancia2,
        r:r,
    };

 }

 function fuerzac3(q1,q2,q3,d){
    let y = d;
    let x = Math.sqrt((q2 * Math.pow(y, 2)) / q3);
    d = y - x;
    let f21 = (k * q2 * q1) / Math.pow(x, 2);
    let f31 = (k * q3 * q1) / Math.pow(y, 2);

 
    
    

    return {
        distancia1: x,
        distancia2: d,
        fuerza1:f21,
        fuerza2:f31,
        
    };

 }

 function fuerzac4(q1,q2,q3,d){
    var x = d;
    var y = Math.sqrt((q2 * x ** 2) / q1);
    var d = x - y;

    var f23 = (k * q2 * q3) / (y ** 2);
    var f13 = (k * q1 * q3) / (x ** 2);

    console.log("distacia1:"+d)
    console.log("distacia2:"+y)
    console.log("distacia:"+x)

    return {
        distancia1: d,
        distancia2: y,
        fuerza1:f23,
        fuerza2:f13,
        
    };

    
    
    
 }

 //bibuja las cargas las cargas si se aplica en la del medio
function dibujar2(c,distancia1,distancia2,dt,t_cargas1,t_cargas2,t_cargas3,posicion) {
    
    var canvas=document.querySelector("#plano1 canvas");
    
    canvas.width=900;
    canvas.height=600;

    var c=canvas.getContext("2d");

    
        var x;
        var y=180;
        var y2=260;
        var y3=320;
        r=45;
        var x1;
        var x2;

    
 
    

    

    dt=dt*100;
    distancia1=distancia1*100;
    distancia2=distancia2*100;
    /* console.log("distancia1: "+distancia1)
    console.log("distancia2: "+distancia2)
    console.log("distancia: "+dt) */
    


    if(posicion==1){
        x=500;
        x1=x-250;
        x2=x+300;

        var aux=distancia1+distancia2;
        var aux2=550/aux;
        var aux3=distancia1*aux2;
        var aux4=x1+aux3;
        x=aux4;
        console.log(aux4);
    
 

    }
    if(posicion==3){
        x=400;
        x1=x-300;
        x2=x+250;

        var aux=distancia1+distancia2;
        var aux2=550/aux;
        var aux3=distancia1*aux2;
        var aux4=x1+aux3;
        x=aux4;
        console.log(aux4);
    
 

    }
 

    c.moveTo(x1,y); //dibuja la linea entre cargas
    c.lineTo(x,y);
    c.lineTo(x2,y);
    c.lineWidth=1;
    c.strokeStyle="black";
    c.stroke();


    var arreglox=[x1,x,x2];// dibuja la forma de las cargas
        arreglox.forEach(function(elemento){
            c.beginPath();
            c.arc(elemento, y, r, 0, 2 * Math.PI);
            c.fillStyle = 'red';
            c.fill();
        })

        c.moveTo(x1,y2); //dibuja la segunda linea
        c.strokeStyle="blue";
        c.lineTo(x,y2);
        c.stroke(); 
        c.beginPath(); // Restablecer el contexto de dibujo antes de cambiar el estilo de trazo
        c.moveTo(x,y2)
        c.strokeStyle="red";
        c.lineTo(x2,y2);
        c.lineWidth=1;
        c.stroke();
     
    
    var cx=(x2-x1)/dt

  
    
    
    arreglox.forEach(function(elemento){//dibuja los puntos  de linea
        c.beginPath();
        c.moveTo(elemento,y2);
        c.lineTo(elemento,y2-10);
        c.lineTo(elemento,y2+10);
        c.lineWidth=1.5;
        c.strokeStyle="black";
        c.stroke(); 
    })

    for(var i=x1;i<=x2;i=i+cx){ //dibuja los centimetros
        c.beginPath();
        c.moveTo(i,y3);
        c.lineTo(i,y3-5);
        c.lineWidth=1.5;
        c.strokeStyle="black";
        c.stroke(); 
    }

    c.moveTo(x1,y3); //dibuja la tercera linea
    c.lineTo(x,y3);
    c.strokeStyle="black";
    c.lineTo(x2,y3);
    c.lineWidth=1;
    c.stroke();

    var arreglox=[x1,x2];// dibuja la forma de las cargas
    arreglox.forEach(function(elemento){//dibuja los puntos  de dt
        c.beginPath();
        c.moveTo(elemento,y3);
        c.lineTo(elemento,y3-10);
        c.lineTo(elemento,y3+10);
        c.lineWidth=1.5;
        c.strokeStyle="black";
        c.stroke(); 
    })

    if(posicion==1) {   
    var colorL1;
    var colorL2;
    if(t_cargas1==t_cargas2){
        if(t_cargas2=="+"){
            colorL1="#ff0e0e"
        }
        if(t_cargas2=="-"){
            colorL1="#0e6dff"
        }   
    }if(t_cargas1!=t_cargas2){
        if(t_cargas2=="+"){
            colorL2="#ff0e0e"
        }
        if(t_cargas2=="-"){
            colorL2="#066dff"
        }  
    } 

    if(t_cargas1==t_cargas3){
        if(t_cargas3=="+"){
            colorL1="#ff0e0e"
        }
        if(t_cargas3=="-"){
            colorL1="#0e6dff"
        }   
    }if(t_cargas1!=t_cargas3){
        if(t_cargas3=="+"){
            colorL2="#ff0e0e"
        }
        if(t_cargas3=="-"){
            colorL2="#0e6dff"
        }  
    } 


   

    
        var tamañof;
        var tamañof2;
        

        tamañof=(x1+x)/2;
        tamañof2=tamañof-x1;
        

        c.beginPath();/* dibuja las fuerzas 1*/
        c.moveTo(x1-r,y);
        c.lineTo(x1-tamañof2,y);
        c.lineTo(x1-tamañof2+10,y-10);
        c.moveTo(x1-tamañof2,y);
        c.lineTo(x1-tamañof2+10,y+10);
        c.lineWidth=5;
        c.strokeStyle=colorL1;
        c.stroke(); 
        
    
        c.beginPath();/* dibuja las fuerzas 2*/
        c.moveTo(x1+r,y);
        c.lineTo(x1+tamañof2,y);
        c.lineTo(x1+tamañof2-10,y-10);
        c.moveTo(x1+tamañof2,y);
        c.lineTo(x1+tamañof2-10,y+10);
        c.lineWidth=5;
        c.strokeStyle=colorL2;
        c.stroke(); 

    }
    if(posicion==3) {   
        var colorL1;
        var colorL2;
        if(t_cargas2==t_cargas3){
            if(t_cargas2=="+"){
                colorL2="#ff0e0e"
            }
            if(t_cargas2=="-"){
                colorL2="#0e6dff"
            }   
        }if(t_cargas2!=t_cargas3){
            if(t_cargas2=="+"){
                colorL1="#ff0e0e"
            }
            if(t_cargas2=="-"){
                colorL1="#066dff"
            }  
        } 
    
        if(t_cargas1==t_cargas3){
            if(t_cargas1=="+"){
                colorL2="#ff0e0e"
            }
            if(t_cargas1=="-"){
                colorL2="#0e6dff"
            }   
        }if(t_cargas1!=t_cargas3){
            if(t_cargas1=="+"){
                colorL1="#ff0e0e"
            }
            if(t_cargas1=="-"){
                colorL1="#0e6dff"
            }  
        } 
    
    
        
    
        
            var tamañof;
            var tamañof2;

            
            
    
            tamañof=(x+x2)/2;
            tamañof2=tamañof-x;
            console.log("ta"+tamañof2)

            if(tamañof2>240){
                tamañof2=tamañof2=240;
            }
    
            c.beginPath();/* dibuja las fuerzas 1*/
            c.moveTo(x2-r,y);
            c.lineTo(x2-tamañof2,y);
            c.lineTo(x2-tamañof2+10,y-10);
            c.moveTo(x2-tamañof2,y);
            c.lineTo(x2-tamañof2+10,y+10);
            c.lineWidth=5;
            c.strokeStyle=colorL1;
            c.stroke(); 
            
        
            c.beginPath();/* dibuja las fuerzas 2*/
            c.moveTo(x2+r,y);
            c.lineTo(x2+tamañof2,y);
            c.lineTo(x2+tamañof2-10,y-10);
            c.moveTo(x2+tamañof2,y);
            c.lineTo(x2+tamañof2-10,y+10);
            c.lineWidth=5;
            c.strokeStyle=colorL2;
            c.stroke(); 
    
        }
        if(x-x1<=90 || x2-x<=90){
            function colores(v){
                let clr;
                if(v=="+"){
                    clr="#ff0e0e";
                }else{
                    clr="#0e6dff";
                }
                return clr;
            }
    
                let clr=colores(t_cargas2);
                let desplaz=y-r-30;
            
                for(var i=y+r;i>desplaz;i=i-10){
                    c.beginPath();
                    c.moveTo(x,i);
                    c.lineTo(x,i-5);
                    c.lineWidth=0.8;
                    c.strokeStyle=clr;
                    c.stroke();
                    }
                    
                    c.beginPath();
                    c.moveTo(x,y-r-30);
                    c.lineTo(x-20,y-r-30);
                    c.moveTo(x,y-r-30);
                    c.lineTo(x+20,y-r-30);
                    c.lineWidth=0.8;
                    c.strokeStyle=clr;
                    c.stroke();
    
        }
        


    return {
        x:x,
        x1:x1,
        x2:x2,
        y:y,
        y2:y2,
        y3:y3,
        r:r,
        dt:dt,
        distancia1:distancia1,
        distancia2:distancia2,
        r:r,
    };

 }


 function llenar(dibujoB,c,vq1,vq2,vq3,fuerza1,fuerza2,t_cargas1,t_cargas2,t_cargas3,posicion){

    var convertirx=(dibujoB.x-10).toString() + "px";
    var convertiry3 =(dibujoB.y3+10).toString() + "px";
    var convertiry2 =(dibujoB.y2+10).toString() + "px";
    var convertirx1 =((dibujoB.x + dibujoB.x1)/2).toString() + "px";
    var convertirx2 =((dibujoB.x + dibujoB.x2)/2).toString() + "px";
    

    //posicion de la distancia total
    var span_dt=document.querySelector("#plano1 .span2");
    span_dt.innerHTML=(dibujoB.dt /100).toString() +"m";
    span_dt.style.top=convertiry3;
    span_dt.style.left="400px";
    if(posicion==1){
        span_dt.style.left="500px";
    }
    if(posicion==2){
        span_dt.style.left="400px";
    }
    

    //posicion dela distanciia1
    var span_dt=document.querySelector("#plano1 .span3");
    span_dt.innerHTML=((dibujoB.distancia1 /100).toFixed(5)).toString() +"m";
    span_dt.style.top=convertiry2;
    span_dt.style.left=convertirx1;

    //posicionamiento de la distancia2
    var span_dt=document.querySelector("#plano1 .span4");
    span_dt.innerHTML=((dibujoB.distancia2 /100).toFixed(5)).toString() +"m";
    span_dt.style.top=convertiry2;
    span_dt.style.left=convertirx2;

    //polaridad carga 1
    var span_t1=document.querySelector("#plano1 .span5");
    span_t1.innerHTML=t_cargas1;
    span_t1.style.top=(dibujoB.y - dibujoB.r).toString() + "px";
    span_t1.style.left=(dibujoB.x1 - dibujoB.r).toString() + "px";
    if(t_cargas1=="+"){
        span_t1.style.backgroundColor="#ff0e0e"
    }else{
        span_t1.style.backgroundColor="#0e6dff"
    }

    //polaridad carga 2
    var span_t1=document.querySelector("#plano1 .span6");
    span_t1.innerHTML=t_cargas2;
    span_t1.style.top=(dibujoB.y - dibujoB.r).toString() + "px";
    span_t1.style.left=(dibujoB.x - dibujoB.r).toString() + "px";
    if(t_cargas2=="+"){
        span_t1.style.backgroundColor="#ff0e0e"
    }else{
        span_t1.style.backgroundColor="#0e6dff"
    }

     //polaridad carga 3
    var span_t1=document.querySelector("#plano1 .span7");
    span_t1.innerHTML=t_cargas3;
    span_t1.style.top=(dibujoB.y - dibujoB.r).toString() + "px";
    span_t1.style.left=(dibujoB.x2 - dibujoB.r).toString() + "px";
    if(t_cargas3=="+"){
        span_t1.style.backgroundColor="#ff0e0e"
    }else{
        span_t1.style.backgroundColor="#0e6dff"
    }

    // ponemos los valores de las cargas

    //carga 1
    var span_c=document.querySelector("#plano1 .span8");
    span_c.innerHTML=(vq1).toString() +"x10^-6";
    span_c.style.top=(dibujoB.y - dibujoB.r-20).toString() + "px";
    span_c.style.left=(dibujoB.x1-30).toString() + "px";
    //carga 2
    var dvq1=0;
    if(dibujoB.x-dibujoB.x1<=90 || dibujoB.x2-dibujoB.x<=90){
        dvq1=35;
    }
    var span_c=document.querySelector("#plano1 .span9");
    span_c.innerHTML=(vq2).toString() +"x10^-6";
    span_c.style.top=(dibujoB.y - dibujoB.r-20-dvq1).toString() + "px";
    span_c.style.left=(dibujoB.x-30).toString() + "px";
    //carga 3
    var span_c=document.querySelector("#plano1 .span10");
    span_c.innerHTML=(vq3).toString() +"x10^-6";
    span_c.style.top=(dibujoB.y - dibujoB.r-20).toString() + "px";
    span_c.style.left=(dibujoB.x2-30).toString() + "px";
    
    /* ponemos las fuerzas f1*/
    var fu1;
    var fu2;
    if(posicion==1){
        fu1="F21: ";
        fu2="F31: ";
    }
    if(posicion==2){
        fu1="F12: ";
        fu2="F32: ";
    }
    if(posicion==3){
        fu1="F13: ";
        fu2="F23: ";
    }

    console.log("F1:" +fuerza1)
    var span_df=document.querySelector("#plano1 .span11");
    var span_f=document.querySelector(".span11 span");
    span_f.innerHTML=fu1+(fuerza1.toFixed(3)).toString() +"N";
    span_df.style.top=(dibujoB.y3 + 100).toString() + "px";
    span_df.style.left="350px";

    /* ponemos las fuerzas f2*/
    var span_df=document.querySelector("#plano1 .span12");
    var span_f=document.querySelector(".span12 span");
    span_f.innerHTML=fu2+(fuerza2.toFixed(3)).toString() +"N";
    span_df.style.top=(dibujoB.y3 + 150).toString() + "px";
    span_df.style.left="350px";
    /* ponemos las fuerzas f3*/

    var span_df=document.querySelector("#plano1 .span13");
    var span_f=document.querySelector(".span13 span");
    span_f.innerHTML="FR: "+((fuerza1-fuerza2).toFixed(3)).toString() +"N";
    span_df.style.top=(dibujoB.y3 + 200).toString() + "px";
    span_df.style.left="350px";

    if(posicion==1){
        if(t_cargas1==t_cargas2){
             //fuerzas en la flecha 1
    var span_ff=document.querySelector("#plano1 .span14");
    span_ff.innerHTML="F21";
    span_ff.style.top=(dibujoB.y-12).toString() + "px";
    span_ff.style.left=(dibujoB.x1-dibujoB.r-15).toString() + "px";
    //fuerzas en la flecha 2
    var span_ff=document.querySelector("#plano1 .span15");
    span_ff.innerHTML="F31"
    span_ff.style.top=(dibujoB.y-12).toString() + "px";
    span_ff.style.left=(dibujoB.x1+dibujoB.r).toString() + "px";
        }else if(t_cargas1==t_cargas3){
                        //fuerzas en la flecha 1
    var span_ff=document.querySelector("#plano1 .span14");
    span_ff.innerHTML="F31";
    span_ff.style.top=(dibujoB.y-12).toString() + "px";
    span_ff.style.left=(dibujoB.x1-dibujoB.r-15).toString() + "px";
    //fuerzas en la flecha 2
    var span_ff=document.querySelector("#plano1 .span15");
    span_ff.innerHTML="F21"
    span_ff.style.top=(dibujoB.y-12).toString() + "px";
    span_ff.style.left=(dibujoB.x1+dibujoB.r).toString() + "px";

        }
    }
    if(posicion==2){
        var pdy;
        var pdx1;
        var pdx2;
         if(dibujoB.x-dibujoB.x1>110 && dibujoB.x2-dibujoB.x>110){
            pdy=dibujoB.y-30;
            pdx1=dibujoB.x-dibujoB.r-30;
            pdx2=dibujoB.x+dibujoB.r;
         }else{
            pdy=dibujoB.y+5;
            pdx1=dibujoB.x-30;
            pdx2=dibujoB.x+5;



         }
        if(t_cargas2==t_cargas3){
            //fuerzas en la flecha 1
    var span_ff=document.querySelector("#plano1 .span14");
    span_ff.innerHTML="F32"
    span_ff.style.top=(pdy).toString() + "px";
    span_ff.style.left=(pdx1).toString() + "px";
    //fuerzas en la flecha 2
    var span_ff=document.querySelector("#plano1 .span15");
    span_ff.innerHTML="F12"
    span_ff.style.top=(pdy).toString() + "px";
    span_ff.style.left=(pdx2).toString() + "px";
        }else if(t_cargas2 != t_cargas3){
            //fuerzas en la flecha 1
    var span_ff=document.querySelector("#plano1 .span14");
    span_ff.innerHTML="F12"
    span_ff.style.top=(pdy).toString() + "px";
    span_ff.style.left=(pdx1).toString() + "px";
    //fuerzas en la flecha 2
    var span_ff=document.querySelector("#plano1 .span15");
    span_ff.innerHTML="F32"
    span_ff.style.top=(pdy).toString() + "px";
    span_ff.style.left=(pdx2).toString() + "px";
        }
        
    }
    if(posicion==3){
        if(t_cargas2==t_cargas3){
            //fuerzas en la flecha 1
    var span_ff=document.querySelector("#plano1 .span14");
    span_ff.innerHTML="F13"
    span_ff.style.top=(dibujoB.y-12).toString() + "px";
    span_ff.style.left=(dibujoB.x2-dibujoB.r-15).toString() + "px";
    //fuerzas en la flecha 2
    var span_ff=document.querySelector("#plano1 .span15");
    span_ff.innerHTML="F23"
    span_ff.style.top=(dibujoB.y-12).toString() + "px";
    span_ff.style.left=(dibujoB.x2+dibujoB.r).toString() + "px";
        }else if(t_cargas2 != t_cargas3){
            //fuerzas en la flecha 1
    var span_ff=document.querySelector("#plano1 .span14");
    span_ff.innerHTML="F23"
    span_ff.style.top=(dibujoB.y-12).toString() + "px";
    span_ff.style.left=(dibujoB.x2-dibujoB.r-15).toString() + "px";
    //fuerzas en la flecha 2
    var span_ff=document.querySelector("#plano1 .span15");
    span_ff.innerHTML="F13"
    span_ff.style.top=(dibujoB.y-12).toString() + "px";
    span_ff.style.left=(dibujoB.x2+dibujoB.r).toString() + "px";
        }
    }
    


    
 }




//parte principal

var cargar=document.querySelector(".formulario");
cargar.addEventListener("submit",function(){

    var cf=t_direccion("cf1","cf2","cf3");

    var carga1=document.querySelector("#carga1");
    var carga2=document.querySelector("#carga2");
    var carga3=document.querySelector("#carga3");
    var distancia=document.querySelector("#distancia");
    

    var contenedor=document.querySelector("#contenedor1");
    if(cf=="c1"){
        

        var vq1=carga1.value;
        var vq2=carga2.value;
        var vq3=carga3.value;
        var dt=distancia.value;

        var t_cargas1=t_carga("pos1","neg1");
        var t_cargas2=t_carga("pos2","neg2");
        var t_cargas3=t_carga("pos3","neg3");

    

        if(vq3>vq2){
            if(t_cargas2 != t_cargas3){
                contenedor.style.display="block";
                var fuerzaf;
                fuerzaf= fuerzac3(vq1*1e-6,vq2*1e-6,vq3*1e-6,dt/100);
                var canvas=document.querySelector("#plano1 canvas");
                var c=canvas.getContext("2d");

                var dibujoB= dibujar2(c,fuerzaf.distancia1,fuerzaf.distancia2,dt/100,t_cargas1,t_cargas2,t_cargas3,1);
                llenar(dibujoB,c,vq1,vq2,vq3,fuerzaf.fuerza1,fuerzaf.fuerza2,t_cargas1,t_cargas2,t_cargas3,1);
            }else if(t_cargas2 == t_cargas3){
                alert("polaridades de las cargas no permitidas ¡..POLARIDAD DE Q2 Y Q3 DEBEN SER DE DIFERENTE TIPO TIPO!..")
            }
        }else{
            alert("valores de las cargas no permitidas ¡..El valor de Q3 debe se mayor al de Q2!..")
        }
        

    }
    if(cf=="c2"){
        

        var vq1=carga1.value;
        var vq2=carga2.value;
        var vq3=carga3.value;
        var dt=distancia.value;

        var t_cargas1=t_carga("pos1","neg1");
        var t_cargas2=t_carga("pos2","neg2");
        var t_cargas3=t_carga("pos3","neg3");

        if(t_cargas1==t_cargas3){
            contenedor.style.display="block";
            var fuerzaf;
            if(vq1==vq3){
                fuerzaf= fuerzac1(vq1*1e-6,vq2*1e-6,vq3*1e-6,dt/100);
            }else if(vq1!=vq3){
                fuerzaf= fuerzac2(vq1*1e-6,vq2*1e-6,vq3*1e-6,dt/100);
            }
            var canvas=document.querySelector("#plano1 canvas");
            var c=canvas.getContext("2d");

            var dibujoB= dibujar(c,fuerzaf.distancia1,fuerzaf.distancia2,dt/100,t_cargas1,t_cargas2,t_cargas3,2);
                
            llenar(dibujoB,c,vq1,vq2,vq3,fuerzaf.fuerza1,fuerzaf.fuerza2,t_cargas1,t_cargas2,t_cargas3,2);
        }else{// si las polaridades no son adecuadas para que la carga  este en equilibrio 
            alert("polaridades de las cargas no permitidas ¡..POLARIDAD DE Q1 Y Q3 DEBEN SER DEL MISMO TIPO!..")
            }


    }
    if(cf=="c3"){
        var vq1=carga1.value;
        var vq2=carga2.value;
        var vq3=carga3.value;
        var dt=distancia.value;

        var t_cargas1=t_carga("pos1","neg1");
        var t_cargas2=t_carga("pos2","neg2");
        var t_cargas3=t_carga("pos3","neg3");

    

        if(vq1>vq2){
            if(t_cargas1 != t_cargas2){
                contenedor.style.display="block";
                var fuerzaf;
                fuerzaf= fuerzac4(vq1*1e-6,vq2*1e-6,vq3*1e-6,dt/100);
                var canvas=document.querySelector("#plano1 canvas");
                var c=canvas.getContext("2d");

                var dibujoB= dibujar2(c,fuerzaf.distancia1,fuerzaf.distancia2,dt/100,t_cargas1,t_cargas2,t_cargas3,3);
                llenar(dibujoB,c,vq1,vq2,vq3,fuerzaf.fuerza1,fuerzaf.fuerza2,t_cargas1,t_cargas2,t_cargas3,3);
            }else if(t_cargas1 == t_cargas2){
                alert("polaridades de las cargas no permitidas ¡..POLARIDAD DE Q1 Y Q2 DEBEN SER DE DIFERENTE TIPO TIPO!..")
            }
        }else if(vq2>=vq1){
            alert("valores de las cargas no permitidas ¡..El valor de Q1 debe se mayor al de Q2!..")
        }


    }
})



 