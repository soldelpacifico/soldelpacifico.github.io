$(document).ready(function(){
  $("#despInfo").click(function(){
    if($(window).width()<1100) {
    $("#liCont1").toggleClass("show");
    if ($("#liCont1").hasClass("show")) {
      $("#despInfo").css("background","#000000");
      $("#despInfo a").css("color","#ffffff");
    }else{
      $("#despInfo").css("background","#e9e9e9");
      $("#despInfo a").css("color","#000000");
    }}
  });
  $("#despComu").click(function(){
    if($(window).width()<1100) {
    $("#liCont2").toggleClass("show");
    if ($("#liCont2").hasClass("show")) {
      $("#despComu").css("background","#000000");
      $("#despComu a").css("color","#ffffff");
    }else{
      $("#despComu").css("background","#e9e9e9");
      $("#despComu a").css("color","#000000");
    }}
  });
});

function mostrar(){
    $("nav").toggleClass("show")
}

function menuDesp(mostrar, cambiarEst){
  $(mostrar).toggleClass("show")
  $(cambiarEst).css("background","#000000")
  $(cambiarEst+' a').css("color","#ffffff")
}

function changeBg(elemento){
    $(elemento).fadeOut(0);
    $(elemento).fadeIn(2200);
}

function irhacia(id){
    $('html, body').animate({
        scrollTop: $(id).offset().top
    }, 1500);
}

function about(){
    irhacia("#about");
    changeBg("#about");
}

function tarifas(){
    irhacia("#tarifas");
    changeBg("#tarifas");
}

function pases(){
    irhacia("#pases");
    changeBg("#pases");
}

function horarios(){
    irhacia("#horarios");
    changeBg("#horarios");
}

window.onscroll = function() {arrastrarPagina()};

function arrastrarPagina() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("btnSubir").style.display = "block";
  } else {
    document.getElementById("btnSubir").style.display = "none";
  }
}

function subir() {
  document.body.scrollTop = 0; // Para Safari
  document.documentElement.scrollTop = 0; // Para Chrome, Firefox, IE and Opera
}