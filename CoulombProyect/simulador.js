'use strict'

window.addEventListener("load", function(){

    var bStart=this.document.getElementById("start");/* boton start */
    var ley=this.document.getElementById("coulomb");/* imagen de ley de coulomb */
    var nCargas=this.document.getElementById("ncargas");/* formulario del numero de cargas */
    var contenedor=this.document.getElementById("contenedor");/* contenedor del curpo del index */



    bStart.addEventListener("click",function(){
        bStart.style.display="none";
        ley.style.display="block";
        nCargas.style.display="block";
        document.body.style.backgroundImage = "url('fondo2.png')";
        document.body.style.backgroundRepeat = "repeat-x";
        document.body.style.backgroundRepeat = "repeat-y";
        document.body.style.backgroundPosition = "center";


        nCargas.addEventListener("submit", function(){
            var cargas=document.getElementById("cargas").value;/* valor de numero de cargas */
            
            //funciones sobre las cargas de coulomb

            

            if(cargas==2){ //si cargas es igual a 2
                window.location.href="cargas2.html";//carga la ventana de 2 cargas  
            }
            if(cargas==3){
                window.location.href="cargas30.html";
            }
            if(cargas==4){
                window.location.href="cargas4.html";

            }
            if(cargas==5){
                window.location.href="cargas5.html";

            }
        })
    })


})
