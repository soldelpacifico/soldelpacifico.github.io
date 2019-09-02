function mostrar(){
    $("nav").toggleClass("show")
}

function about(){
    $('html, body').animate({
        scrollTop: $("#about").offset().top
    }, 2000);
    footerColor();
}

function footerColor(){
    $("footer").animate({
		backgroundColor: "#ffffff"
    }, 1000 );
    $("footer").animate({
		backgroundColor: "#212121"
	}, 1000 );
}