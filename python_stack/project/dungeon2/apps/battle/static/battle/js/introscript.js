$(document).ready(function(){
    $('.fight').hide()
    $('.fadeout').delay(1000).fadeOut(500)
    $('.fadein1').delay(1500).fadeIn(500).delay(1000).fadeOut(500)
    $('.fadein2').delay(3500).fadeIn(500).delay(1000).fadeOut(500)
    $('.intro').delay(5500).fadeOut(200)
    setTimeout(submit, 6000);
    function submit() {
        $('form').submit();
    }
});