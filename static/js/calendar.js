$(document).ready(function(){
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav'
      });
      $('.slider-nav').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: true,
        centerMode: false,
        focusOnSelect: true
      });
      $('.publication-slicker').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        centerMode: false,
        focusOnSelect: true
      });
  });