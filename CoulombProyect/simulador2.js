var limpia;

const Ke=9*Math.pow(10,9);/* constante ke */
            
function fuerza(q1, q2, r){ //funcuan de la fuerza
    r=r/100;
    var F=(Ke*(q1*q2))/Math.pow(r,2);
    return F;   
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

function t_direccion(id1,id2){ //funcion que evalua los radio button
    var dir;
    if(document.getElementById(id1).checked){
        dir="c1";
    }
    if(document.getElementById(id2).checked){
        dir="c2";
    }
    return dir;
}




window.addEventListener("load", function(){

    /* inicio */
    var inicio=document.querySelector("#inicio");
    /*inicio.addEventListener("click",function(){
            href="index.html";

    })*/
    
    /* ------ */
    var f_cargas=document.getElementById("ingreso2"); //formulario de 2 cargas
    f_cargas.addEventListener("submit",function(){
        var carga1=document.getElementById("q1").value //obtenemos la carga 1
        var carga2=document.getElementById("q2").value //obtenemos la carga 2
        var distancia=document.getElementById("distancia").value //obtenemos la distancia entre cargas
        var canvas=document.querySelector("canvas");
        var dibujo=document.querySelector("#dibujo");

        var t_cargas1=t_carga("pos1","neg1");//polaridad de las cargas
        var t_cargas2=t_carga("pos2","neg2");


        var cEjerce=t_direccion("ejerce1","ejerce2");//sobre q carga se ejerce la fuerza

    
        var flecha;

        if((cEjerce=="c1") && (t_cargas1 == t_cargas2)){
            flecha=1;
        }

        if((cEjerce=="c1") && (t_cargas1 != t_cargas2)){
            flecha=2;
        }

        if((cEjerce=="c2") && (t_cargas1 != t_cargas2)){
            flecha=3;
        }
        if((cEjerce=="c2") && (t_cargas1 == t_cargas2)){
            flecha=4;
        }

        dibujo.style.display="block";

        canvas.width="900"
        canvas.height="500"

        var c=canvas.getContext("2d");

        var x=450;
        var x1=x-250;
        var x2=x+250;
        var y=180;
        var y2=260;
        r=45;

        
        c.moveTo(x1,y);
        c.lineTo(x2,y);
        c.lineWidth=1;
        c.strokeStyle="black";
        c.stroke();

        var arreglox=[x1,x2];// dibuja la forma de las cargas
        arreglox.forEach(function(elemento){
            c.beginPath();
            c.arc(elemento, y, r, 0, 2 * Math.PI);
            c.fillStyle = 'red';
            c.fill();
        })

        c.moveTo(x1,y2); //dibuja la segunda
        c.lineTo(x2,y2);
        c.strokeStyle="black";
        c.lineWidth=1;
        c.stroke();

        arreglox.forEach(function(elemento){//dibuja los puntos  de linea
            c.beginPath();
            c.moveTo(elemento,y2);
            c.lineTo(elemento,y2-10);
            c.lineTo(elemento,y2+10);
            c.lineWidth=1.5;
            c.strokeStyle="black";
            c.stroke(); 
        })


        var cx=500/distancia;
      

        for(var i=x1;i<=x2;i=i+cx){ //dibuja los centimetros
            c.beginPath();
            c.moveTo(i,y2);
            c.lineTo(i,y2-5);
            c.lineWidth=1;
            c.strokeStyle="black";
            c.stroke(); 
        }




        tamaño=150+r;
        var color;
        var color1="#ff0e0e";
        var color2="#0e6dff"
        if(flecha==1){
            if(t_cargas2=="+"){
                color="#ff0e0e";
            }else{
                color="#0e6dff";
            }

            c.beginPath();// dibuja las fuerzas 1
            c.moveTo(x1-r,y);
            c.lineTo(x1-tamaño,y);
            c.lineTo(x1-tamaño+10,y-10);
            c.moveTo(x1-tamaño,y);
            c.lineTo(x1-tamaño+10,y+10);
            c.lineWidth=5;
            c.strokeStyle=color;
            c.stroke();    
            
   
        }
        if(flecha==2){
            if(t_cargas2=="+"){
                color="#ff0e0e";
            }else{
                color="#0e6dff";
            }

            c.beginPath();// dibuja las fuerzas 1
            c.moveTo(x1+r,y);
            c.lineTo(x1+tamaño,y);
            c.lineTo(x1+tamaño-10,y-10);
            c.moveTo(x1+tamaño,y);
            c.lineTo(x1+tamaño-10,y+10);
            c.lineWidth=5;
            c.strokeStyle=color;
            c.stroke();    
            
        }
        if(flecha==3){
            if(t_cargas1=="+"){
                color="#ff0e0e";
            }else{
                color="#0e6dff";
            }

            c.beginPath();// dibuja las fuerzas 1
            c.moveTo(x2-r,y);
            c.lineTo(x2-tamaño,y);
            c.lineTo(x2-tamaño+10,y-10);
            c.moveTo(x2-tamaño,y);
            c.lineTo(x2-tamaño+10,y+10);
            c.lineWidth=5;
            c.strokeStyle=color;
            c.stroke();    
            

            
        }
        if(flecha==4){
            if(t_cargas1=="+"){
                color="#ff0e0e";
            }else{
                color="#0e6dff";
            }
            c.beginPath();// dibuja las fuerzas 1
            c.moveTo(x2+r,y);
            c.lineTo(x2+tamaño,y);
            c.lineTo(x2+tamaño-10,y-10);
            c.moveTo(x2+tamaño,y);
            c.lineTo(x2+tamaño-10,y+10);
            c.lineWidth=5;
            c.strokeStyle=color;
            c.stroke();  

               
        }


    
    var convertiry =(y).toString() + "px";
    var convertirx1 =(x1).toString() + "px";
    var convertirx2 =(x2).toString() + "px";

    var span1=document.querySelector(".plano .dcarga1");
    span1.innerHTML=t_cargas1;
    span1.style.top=(y-r).toString()+"px";
    span1.style.left=(x1-r).toString()+"px";
    if(t_cargas1=="+"){
        span1.style.backgroundColor="#ff0e0e"
        
    }else{
        span1.style.backgroundColor="#0e6dff"
    }
    
    var span2=document.querySelector(".plano .dcarga2");
    span2.innerHTML=t_cargas2;
    span2.style.top=(y-r).toString()+"px";
    span2.style.left=(x2-r).toString()+"px";
    if(t_cargas2=="+"){
        span2.style.backgroundColor="#ff0e0e"
    }else{
        span2.style.backgroundColor="#0e6dff"
    }

    
    var span3=document.querySelector(".plano .cq1");
    span3.innerHTML="("+(carga1).toString()+"x10^-6)C";
    span3.style.top=(y-r-25).toString()+"px";
    span3.style.left=(x1-40).toString()+"px";

    var span3=document.querySelector(".plano .cq2");
    span3.innerHTML="("+(carga2).toString()+"x10^-6)C";
    span3.style.top=(y-r-25).toString()+"px";
    span3.style.left=(x2-40).toString()+"px";

    /* ponemos fr */
    var span4=document.querySelector(".plano .f span");

    var fx;
    if(flecha==1){
        fx=x1-r-75;
        span4.innerHTML="21"
    }
    if(flecha==2){
        fx=x1+r+75;
        span4.innerHTML="21"
    }
    if(flecha==3){
        fx=x2-r-75;
        span4.innerHTML="12"
    }
    if(flecha==4){
        fx=x2+r+75;
        span4.innerHTML="12"
    }
    var span4=document.querySelector(".plano .f");
    span4.style.top=(y-20).toString()+"px";
    span4.style.left=(fx).toString()+"px";

    var span5=document.querySelector(".plano .d");
    span5.innerHTML=(distancia/100).toString()+"m";
    span5.style.top=(y2+20).toString()+"px";
    span5.style.left=(x).toString()+"px";


    var fr=fuerza(carga1*Math.pow(10,-6),carga2*Math.pow(10,-6),distancia);
    /* fuerza resultante */
    var span5=document.querySelector(".plano .fr");
    span5.innerHTML="Fr: "+(fr.toFixed(2)).toString()+"N";
    span5.style.top=(y2+100).toString()+"px";
    span5.style.left=(x-50).toString()+"px";

    

//movimiento
    var cajam=document.querySelector(".cajamovimiento");
   if(cEjerce=="c1"){
   cajam.style.top=(y-126).toString()+"px";
    cajam.style.left=(x1-126).toString()+"px";
   }

   if(cEjerce=="c2"){
   cajam.style.top=(y-126).toString()+"px";
    cajam.style.left=(x2-126).toString()+"px";
   }
       
    })


})