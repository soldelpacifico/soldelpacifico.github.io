$(document).ready(function(){
  $("#despInfo").click(function(){
    if($(window).width()<1100) {
      $("#liCont1").toggleClass("show");
      $("#despInfo").toggleClass("clicked");
    }
  });
  $("#despComu").click(function(){
    if($(window).width()<1100) {
      $("#liCont2").toggleClass("show");
      $("#despComu").toggleClass("clicked");
    }
  });
  $("#despCont").click(function(){
    if($(window).width()<1100) {
      $("#liCont3").toggleClass("show");
      $("#despCont").toggleClass("clicked");
    }
  });

  $(".login").click(function(){
      $("#Login").toggleClass("show");
  });


  $("#btnCalera").click(function() {
    $(".calera").css("display","block");
    $(".concon").css("display","none");
    $("#btnCalera a").css("background","#f99600");
    $("#btnConcon a").css("background","#ffffff")
  });
  $("#btnConcon").click(function() {
    $(".calera").css("display","none");
    $(".concon").css("display","block");
    $("#btnCalera a").css("background","#ffffff");
    $("#btnConcon a").css("background","#f99600")
  });
  $(function() {
		$('#main-menu').smartmenus({
			subMenusSubOffsetX: 1,
			subMenusSubOffsetY: -8
		});
  });
    var pathname = window.location.pathname;
    $('#main-menu > a[href="'+pathname+'"]').addClass('active');

    $('.popup').magnificPopup({type:'image'});
});

function mostrar(){
    $("nav").toggleClass("show")
}

function toggleMenu(){
  $("nav").toggleClass("mostrarMenu")
}

function menuDesp(mostrar, cambiarEst){
  $(mostrar).toggleClass("show");
  $(cambiarEst).css("background","#000000");
  $(cambiarEst+' a').css("color","#ffffff");
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