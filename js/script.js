function mostrar(){
    $("nav").toggleClass("show")
}

function about(){
    $('html, body').animate({
        scrollTop: $("#about").offset().top
    }, 1000);
}