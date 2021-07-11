$("#search-icon").click(function () {
	$(".nav").toggleClass("search");
	$(".nav").toggleClass("no-search");
	$(".search-input").toggleClass("search-active");
});


$('.menu-toggle').click(function () {
	console.log('btn clicked');
	$(".nav").toggleClass("mobile-nav");
	$(this).toggleClass("is-active");
});

$(document)
    .mousemove(function(e) {
		
        $('.cursor')
        .eq(0)
        .css({
            left: e.pageX - 10+"px",
            top: e.pageY -10+"px"
        });
        setTimeout(function() {
        $('.cursor')
            .eq(1)
            .css({
            left: e.pageX - 10+"px",
            top: e.pageY - 10+"px"
            });
        }, 100);
    })

$(".slides").slick({
	asNavFor: '.captions',
	infinite: false,
	speed: 2000,
	arrows: false,
	autoplay: false,
	// fade: true,
})


$(".never-about-us-slider").slick({
	speed: 15000,
	autoplay: true,
	autoplaySpeed: 0,
    cssEase: 'linear',
    // autoplay: true,
    // autoplaySpeed: 6000,
	infinite: true,
	pauseOnHover: false,
	pauseOnFocus: false,
	arrows: false,
	slidesToShow: 2,
	responsive: [
		{
			breakpoint: 1025,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 1,
			}
		},
		{
			breakpoint: 992,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1,
			}
		},
	]

})



$(".captions").slick({
	asNavFor: '.slides',
	infinite: false,
	speed: 2000,
	// fade: true,
	dots: false,
	autoplay: false,
	arrows: false,
	responsive: [

		{
			breakpoint: 480,
			settings: {
				dots: true,
			}
		}
		// You can unslick at a given breakpoint now by adding:
		// settings: "unslick"
		// instead of a settings object
	]
})

window.onscroll = function () { myFunction() };
var navbar = document.getElementById("navbar");
function myFunction() {
	if (document.body.onscroll > 0) {
		$(navbar).addClass("full-height");
	} else {
		$(navbar).addClass("");
	}
}

$.fn.isInViewport = function () {
	var elementTop = $(this).offset().top;
	var elementBottom = elementTop + $(this).outerHeight();
	var viewportTop = $(window).scrollTop();
	var viewportBottom = viewportTop + $(window).height();
	return elementBottom > viewportTop && elementTop < viewportBottom;
};

var lastPageScroll = 0;
var scrollDirection=undefined;
$(window).on('resize scroll', function () {
	var pageScroll = $(window).scrollTop();
	if (pageScroll > lastPageScroll) {
		scrollDirection="DOWN";
	}else{
		scrollDirection="UP";
	}
	lastPageScroll = pageScroll;
});