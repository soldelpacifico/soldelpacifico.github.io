$(document).ready(function(){
  $(".closeAviso").click(function() {
    $(".aviso").css("display","none")
  });

  $('.open-popup-link').magnificPopup({
    type:'inline',
    midClick: true // Allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source in href.
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

function changeBg(elemento){
    $(elemento).fadeOut(0);
    $(elemento).fadeIn(2200);
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