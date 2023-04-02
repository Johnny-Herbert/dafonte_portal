$(document).ready(function(){
    var ua = window.navigator.userAgent;
    var msie = ua.indexOf("MSIE ");

    if (msie > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./))
    {
        // var $body = $('body')
        // $body.empty()
        // $body.css({'backgroundImage': 'url(static/images/default-header-darken.jpg)', 'backgroundRepeat': 'no-repeat', 'overflow': 'hidden'})
        // $body.append('<div style="padding-top: 100px; text-align: center"><img src="static/images/logo-white.png" alt="da Fonte logo" /></div>')
        // $body.append('<h1 style="margin-top: 75px; text-align: center">Esse site é melhor visualizado nos navegadores Chrome, Firefox e Safari.</h1>')
    }
})
