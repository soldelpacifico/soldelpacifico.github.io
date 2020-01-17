$(document).ready(function(){
  $(".closeAviso").click(function() {
    $(".aviso").css("display","none")
  });

  $('.open-popup-link').magnificPopup({
    type:'inline',
    midClick: true
  });
  $('input[type=radio][name=zona]').change(function() {
    if (this.value == 'calera') {
      $(".calera").css("display","block");
      $(".concon").css("display","none");
      $("#btnCalera a").css("background","#f99600");
      $("#btnConcon a").css("background","#ffffff");
      $('html, body').animate({
        scrollTop: ($('#Calera').offset().top)
    },500);
    }
    else {
      $(".calera").css("display","none");
      $(".concon").css("display","block");
      $("#btnCalera a").css("background","#ffffff");
      $("#btnConcon a").css("background","#f99600");
      $('html, body').animate({
        scrollTop: ($('#Costa').offset().top)
    },500);
    }
});
  
  $("#btnCalera").click(function() {
    
  });
  $("#btnConcon").click(function() {

  });
  $(function() {
		$('#main-menu').smartmenus({
			subMenusSubOffsetX: 1,
			subMenusSubOffsetY: -8
		});
  });
    var pathname = window.location.pathname;
    $('#main-menu > li a[href="'+pathname+'"]').addClass('active');

    $('.popup').magnificPopup({type:'image'});
});

function desdeChange(){
  $("#hacia").val('');
  $('#buscarTarifa form').submit()
}

function toggleMenu(){
  $("nav").toggleClass("mostrarMenu")
}

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

function home() {
  window.location = '/';
}