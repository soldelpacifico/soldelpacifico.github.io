function mostrar(){
    $("nav").toggleClass("show")
}

function changeBg(elemento ,colorUno, ColorDos){
    $(elemento).animate({
		backgroundColor: colorUno
    }, 500 );
    $(elemento).animate({
		backgroundColor: ColorDos
	}, 1000 );
}

function irhacia(id){
    $('html, body').animate({
        scrollTop: $(id).offset().top
    }, 1500);
}

function about(){
    irhacia("#about");
    changeBg("#about","#ffffff", "#212121");
}

function tarifas(){
    irhacia("#tarifas");
    changeBg("#tarifas", "#000000", "#ffffff");
}

function pases(){
    irhacia("#pases");
    changeBg("#pases", "#000000", "#ffffff");
}

function horarios(){
    irhacia("#horarios");
    changeBg("#horarios", "#000000", "#ffffff");
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